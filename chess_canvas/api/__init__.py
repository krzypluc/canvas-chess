from fastapi import APIRouter
from .board import boardRouter
from .moves import movesRouter

api_router = APIRouter(prefix="/api", tags=["api"])

api_router.include_router(boardRouter)
api_router.include_router(movesRouter)
