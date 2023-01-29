import chess
import logging
from fastapi import FastAPI
from .api import api_router

logger = logging.getLogger(__name__)
logFormatter = logging.Formatter(
    "[%(asctime)s] [%(threadName)-12.12s] [%(name)s] [%(levelname)-5.5s]  %(message)s"
)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
logger.setLevel(logging.DEBUG)
logging.getLogger().addHandler(consoleHandler)

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def board():
    return {"board": str(board)}
