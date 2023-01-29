from fastapi import APIRouter, Response, Cookie, HTTPException
from .models.board import Board

movesRouter = APIRouter(prefix="/moves")
import logging
import chess

from .board import boards_repo

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@movesRouter.post("/")
async def make_move(response: Response, game_id: str = Cookie(default=None)):
    board = boards_repo.get(game_id, None)

    if board is None:
        raise HTTPException(status_code=404, detail="Game not found.")

    chess_board = chess.Board(board.board)
    chess_board.turn = board.player_color

    return {"moves": list(chess_board.legal_moves)}
