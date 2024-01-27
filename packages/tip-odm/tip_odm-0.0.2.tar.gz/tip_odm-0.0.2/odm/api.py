from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response, HTTPException
import os
import uvicorn
from .models_definition import DefinitionCompact, Definition
from .query import LoadOptions
from .logger import init_logger
from .settings import get_settings
from . import query

app = FastAPI()


@app.get("/api/query", response_model_exclude_none=True)
def get_queries() -> list[DefinitionCompact]:
    return query.get_queries()


@app.get("/api/query/{key}", response_model_exclude_none=True)
def get_queries(key: str) -> Definition:
    definition = query.get_query(key)
    if definition is None:
        raise HTTPException(status_code=404, detail="Query nicht vorhanden")

    return definition


@app.post("/api/data", response_model=list[list])
def get_query_result(options: LoadOptions):
    r = query.get_query_result(options)
    return Response(content=r, media_type="application/json")


def init():
    """
    Initialisiert die Umgebung
    :return: FastAPI
    """

    init_logger()
    load_dotenv()

    return app


def start():
    """
    Startet den Webserver
    :param api_key: Api-Key für das Abfragen der Definitionen und der Daten
    :return: None
    """

    api_key = os.getenv("API_KEY") or "TEST"

    @app.middleware("http")
    async def check_api_key(request: Request, call_next):
        if request.headers.get("X-Api-Key", "") != api_key:
            return Response(status_code=401, content="API Key ungültig")

        return await call_next(request)

    settings = get_settings()
    uvicorn.run(app, host=settings.host, port=settings.port, log_config={
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {}
    })
