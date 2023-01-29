from pydantic import BaseModel


class Board(BaseModel):
    player_color: bool
    board: str
    is_over: bool
