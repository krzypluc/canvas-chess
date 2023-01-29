from fastapi import APIRouter, Cookie, Response, HTTPException, status
from .models.board import Board
import chess
import uuid
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

boardRouter = APIRouter(prefix="/board")

global boards_repo
boards_repo = dict()


@boardRouter.get("/")
async def get_board(game_id: str = Cookie(default=None)):

    board = boards_repo.get(game_id, None)

    if board is None:
        raise HTTPException(status_code=404, detail="There is no such game.")

    return board


@boardRouter.post("/", status_code=status.HTTP_201_CREATED)
async def init_board(response: Response, game_id: str = Cookie(default=None)):

    logger.info(game_id)

    if game_id is None or boards_repo.get(game_id, None) is None:
        game_id_init = str(uuid.uuid4())

        logger.debug(game_id_init)

        boards_repo[game_id_init] = Board(
            player_color=True, board=chess.STARTING_BOARD_FEN, is_over=False
        )
        response.set_cookie(key="game_id", value=game_id_init)
        return {"game_id": game_id_init, "board": boards_repo[game_id_init]}

    raise HTTPException(status_code=303, detail="Game already exists.")
