"""King of the hill chess."""

from ..board import COLORS, ChessBoard, Color, GameStatus


class KingOfTheHillBoard(ChessBoard):
    """King of the hill chessboard."""

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
        """Create a KingOfTheHillBoard."""
        super().__init__(
            fen=fen, epd=epd, pgn=pgn, empty=empty, import_fields=import_fields
        )
        self.fields["Variant"] = "King of the Hill"

    @property
    def moves(self) -> str:
        """Export moves as string."""
        for i in range(len(self._moves[:-1])):
            self._moves[i] = self._moves[i].replace("#", "")
        return super().moves

    def is_checkmate(
        self, *, kings_known_in_check: tuple[Color, ...] | None = None
    ) -> bool:
        """Check if either color's king is checkmated."""
        for color in COLORS:
            if self._kings[color] in ("d4", "d5", "e4", "e5"):
                self._moves[-1] = (
                    self._moves[-1].replace("+", "").replace("#", "") + "#"
                )
                self._status = GameStatus(
                    game_over=True, winner=color, description="king_reached_hill"
                )
                return True
        return super().is_checkmate(kings_known_in_check=kings_known_in_check)
