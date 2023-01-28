import chess
import logging
from fastapi import FastAPI

logger = logging.getLogger(__name__)
logFormatter = logging.Formatter("[%(asctime)s] [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
logger.setLevel(logging.DEBUG)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
