"""Horde variant of chess."""

from collections.abc import Iterator

from ..board import (
    FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR,
    ChessBoard,
    Color,
    GameStatus,
    Piece,
)


class HordeBoard(ChessBoard):
    """A chess board to play Horde."""

    CHECK_FOR_INSUFFICIENT_MATERIAL = False

    def __init__(
        self,
        fen: str | None = None,
        epd: str | None = None,
        pgn: str | None = None,
        *,
        empty: bool = False,
        import_fields: bool = True,
    ) -> None:
        """Create a HordeBoard."""
        fen_ = (
            "rnbqkbnr/pppppppp/8/1PP2PP1/PPPPPPPP/PPPPPPPP/PPPPPPPP/PPPPPPPP w qk - 0 1"
            if fen is None and not empty
            else fen
        )
        super().__init__(
            fen=fen_, epd=epd, pgn=pgn, empty=True, import_fields=import_fields
        )
        self.fields["Variant"] = "Horde"

    def _pawn_pseudolegal_squares(
        self,
        initial_square: str,
        piece: Piece,
        *,
        capture_only: bool = False,
    ) -> Iterator[str]:
        yield from super()._pawn_pseudolegal_squares(
            initial_square, piece, capture_only=capture_only
        )
        if not capture_only and not piece.has_moved:
            step_func = FORWARD_STEP_FUNCTIONS_BY_PAWN_COLOR[piece.color]
            if (
                (sq := step_func(initial_square, 1)) is not None
                and self._grid[sq] is None
                and (sq := step_func(initial_square, 2)) is not None
                and self._grid[sq] is None
            ):
                yield sq

    def is_checkmate(
        self, *, kings_known_in_check: tuple[Color, ...] | None = None
    ) -> bool:
        """Check if either color's king is checkmated."""
        pieces = self.pieces
        if all(pieces[pc].color == "black" for pc in pieces):
            self._moves[-1] = f"{self._moves[-1].replace('+', '')}#"
            self._status = GameStatus(
                game_over=True, winner="black", description="all_pieces_captured"
            )
            return True
        if (
            (
                (kings_known_in_check is not None and "black" in kings_known_in_check)
                or self.king_is_in_check("black")
            )
            and not self.can_block_or_capture_check("black")
            and not self.king_can_escape_check("black")
        ):
            self._status = GameStatus(
                game_over=True,
                winner="white",
                description="checkmate",
            )
            return True
        return False
