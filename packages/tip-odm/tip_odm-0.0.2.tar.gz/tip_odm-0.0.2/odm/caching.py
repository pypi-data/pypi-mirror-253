import dataclasses
import datetime
import threading
import time
from functools import wraps
from typing import Callable
import schedule
from .logger import log_info, log_exception, log_error
from .utils import timer

type JobType = schedule.Job | list[schedule.Job] | str | list[str]


@dataclasses.dataclass
class CacheItem:
    cache_key: str
    name: str
    recreate: bool
    func: Callable
    data_dict: dict[str, any]

    is_invalidated: bool = False
    last_refresh: datetime.datetime | None = None

    def create(self, key_param: str, *args, **kwargs):
        text = f"Cache [{self.cache_key}] wurde neu erstellt"
        data = timer(text, lambda: self.func(*args, **kwargs))

        self.data_dict[key_param] = data
        self.is_invalidated = False
        self.last_refresh = datetime.datetime.now()
        log_info(f"Cache [{self.cache_key}] erstellt")

        return data

    def get_or_create(self, key_param: str, *args, **kwargs):
        data = self.data_dict.get(key_param, None)

        if data is None or self.is_invalidated:
            data = self.create(key_param, *args, **kwargs)

        return data

    def invalidate(self):
        self.is_invalidated = True

        if self.recreate:
            recreate_list.append(self)
            log_info(f"Cache [{self.cache_key}] zur Neuerstellung vorgemerkt")
        else:
            log_info(f"Cache [{self.cache_key}] invalidiert")
            self.data_dict.clear()


cache: dict[str, CacheItem] = {}
recreate_list: list[CacheItem] = []


def data_cache(cache_key: str, name: str, jobs: JobType = None, recreate: bool = True):
    """
    Liefert die Daten aus dem Cache oder erstellt diesen neu
    :param cache_key: Key des Caches
    :param name: Name des Caches
    :param jobs: Uhrzeit, Jobs, Liste von Uhrzeit oder Liste von JObs
    :param recreate: Angabe, ob nach Invalidierung des Cache der Cache direkt neu berfüllt werden soll. 
    Funktioniert nur mit Methoden ohne Parameter!
    :return: Ergebnis der dekorierten Methode
    """
    if jobs is None:
        jobs = ["02:00"]
    if isinstance(jobs, str):
        jobs = [jobs]
    if isinstance(jobs, schedule.Job):
        jobs = [jobs]
    if isinstance(jobs, list):
        jobs = [job if isinstance(job, schedule.Job) else schedule.every().day.at(job) for job in jobs]

    def decorator(func):
        cache_item = CacheItem(cache_key=cache_key, name=name, recreate=recreate, func=func, data_dict={})
        cache[cache_key] = cache_item

        @wraps(func)
        def wrapper(*args, **kwargs):
            params = (*args, *kwargs.items())
            key_param = f"{params}"

            if recreate and len(params) > 0:
                log_error(f"Cache [{cache_key}] kann nicht neu erstellt werden, da die Methode Parameter hat")
                return None

            return cache_item.get_or_create(key_param, *args, **kwargs)

        for job in jobs:
            job.do(cache_item.invalidate)

        return wrapper

    return decorator


def get_cached_data(cache_key: str, *args, **kwargs):
    """
    Liefert die Daten aus dem Cache oder erstellt diesen neu
    :param cache_key: Key des Caches
    :return: Ergebnis der dekorierten Methode
    """

    cache_item = cache.get(cache_key, None)
    if cache_item is None:
        log_error(f"Cache [{cache_key}] nicht gefunden")
        return None

    params = (*args, *kwargs.items())
    key_param = f"{params}"

    return cache_item.get_or_create(key_param, *args, **kwargs)


def invalidate_cached_data(cache_key: str):
    """
    Invalidiert den Cache
    :param cache_key: Key des Caches
    :return: None
    """

    cache_item = cache.get(cache_key, None)
    if cache_item is None:
        log_error(f"Cache [{cache_key}] nicht gefunden")
        return

    cache_item.invalidate()


def run_scheduler():
    stop_event = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not stop_event.is_set():
                schedule.run_pending()
                cls.recreate()
                time.sleep(5)

        @classmethod
        def recreate(cls):
            while len(recreate_list) > 0:
                cache_item = recreate_list.pop()

                try:
                    cache_item.get_or_create("()")
                except Exception:
                    log_exception(f"Cache [{cache_item.cache_key}] konnte nicht neu erstellt werden")

    schedule_thread = ScheduleThread()
    schedule_thread.start()

    return stop_event


run_scheduler()
