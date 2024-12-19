from fastapi import FastAPI
from pazer_logger_python import Logger

from Router.Main import route as main_route
from Router.Test import route as test_route


def Routing(app: FastAPI) -> None:
    Logger.info("Running Routing")
    app.include_router(main_route, tags=["Main"])
    app.include_router(test_route, prefix="/test", tags=["test"])
