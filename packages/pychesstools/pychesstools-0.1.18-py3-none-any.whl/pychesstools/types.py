"""Basic types for ChessBoard and subclasses."""

from collections.abc import Callable
from typing import Literal

PieceType = Literal["king", "queen", "rook", "bishop", "knight", "pawn"]
Color = Literal["white", "black"]
Side = Literal["kingside", "queenside"]
SquareGenerator = Callable[[str], tuple[str, ...]]
StepFunction = Callable[[str, int], str | None]
