"""Atomic chess."""

from collections.abc import Iterator
from typing import Literal, overload

from ..board import (
    CASTLING_FINAL_SQUARES,
    COLORS,
    PLAINTEXT_ABBRS,
    SIDES,
    ChessBoard,
    Color,
    GameStatus,
    MoveError,
    Piece,
    PieceType,
    Side,
    en_passant_final_square_from_file,
    get_adjacent_squares,
    king_navigable_squares,
    other_color,
)


class AtomicBoard(ChessBoard):
    """Atomic chessboard."""

    def __init__(
        self,
        fen: str | None = None,
        epd: str | None = None,
        pgn: str | None = None,
        *,
        empty: bool = False,
        import_fields: bool = True,
    ) -> None:
        """Create a Crazyhouse board."""
        super().__init__(
            fen=fen, epd=epd, pgn=pgn, empty=empty, import_fields=import_fields
        )
        self.fields["Variant"] = "Atomic"

    def promote_pawn(self, square: str, piece_type: PieceType) -> None:
        """Promote a pawn on the farthest rank from where it started."""
        if self[square] is None:
            self._double_forward_last_move = None
            self._must_promote_pawn = None
            updated_notation = f"{self._moves[-1]}={PLAINTEXT_ABBRS[piece_type]}"
            if self.king_is_in_check(oc := other_color(self.turn)):
                if (
                    self.is_checkmate(kings_known_in_check=(oc,))
                    or self.king_exploded()
                ):
                    updated_notation += "#"
                else:
                    updated_notation += "+"
            self._moves[-1] = updated_notation
            self._alternate_turn(reset_halfmove_clock=True)
        else:
            super().promote_pawn(square, piece_type)

    def king_is_in_check(self, color: Color) -> bool | None:
        """Whether king is in check."""
        if self._kings.get(color) is None:
            return None
        if self.king_exploded():
            return False
        if any(
            (pc := self[sq]) is not None
            and pc.piece_type == "king"
            and pc.color == other_color(color)
            for sq in king_navigable_squares(self._kings[color])
        ):
            return False
        return super().king_is_in_check(color)

    def is_checked_square(self, color: Color, square: str) -> bool:
        """Whether a square is threatened by an opposite color piece."""
        return (
            False
            if square in king_navigable_squares(self._kings[other_color(color)])
            else super().is_checked_square(color, square)
        )

    def _explode(self, final_square: str) -> None:
        """Create an atomic "explosion" after a capture."""
        for sq in self._explosion_dict(final_square):
            if (pc := self._grid[sq]) is not None and pc.piece_type == "king":
                self._status = GameStatus(
                    game_over=True,
                    winner=other_color(pc.color),
                    description="explosion",
                )
            self[sq] = None

    def _explosion_dict(self, final_square: str) -> dict[str, Piece | None]:
        """Return dict of explosion changes without actually exploding."""
        return {
            sq: None
            for sq in (final_square, *king_navigable_squares(final_square))
            if sq == final_square
            or ((pc := self._grid[sq]) is not None and pc.piece_type != "pawn")
        }

    def king_exploded(self) -> GameStatus | None:
        """Whether a king has exploded (ending the game)."""
        for color in COLORS:
            if self[self._kings[color]] is None:
                return GameStatus(
                    game_over=True, winner=other_color(color), description="explosion"
                )
        return None

    def can_explode_opponent_king(self, color: Color) -> bool:
        """Whether color can indirectly explode opponent's king."""
        return self.can_explode_piece(self._kings[other_color(color)])

    def can_explode_piece(self, square: str) -> bool:
        """Whether a piece can be removed by capturing an adjacent piece."""
        piece = self._get_piece_at_non_empty_square(square)
        unsafe_to_capture = [
            sq
            for sq in king_navigable_squares(self._kings[other_color(piece.color)])
            if (pc := self[sq]) is not None
        ]
        if_captured_then_piece_explodes = (
            [
                sq
                for sq in king_navigable_squares(square)
                if (pc := self[sq]) is not None
                and pc.color == piece.color
                and sq not in unsafe_to_capture
            ]
            if piece.piece_type != "pawn"
            else []
        )
        other_color_pieces = [
            sq
            for sq in self
            if (pc := self._grid[sq]) is not None
            and pc.color == other_color(piece.color)
        ]
        for square_ in other_color_pieces:
            if any(
                sq in if_captured_then_piece_explodes
                for sq in self._pseudolegal_squares(square_, capture_only=True)
                if self.can_move_piece(square_, sq, check_turn=False)
            ):
                return True
        return False

    def _king_pseudolegal_squares(
        self,
        initial_square: str,
        piece: Piece,
        *,
        check_castle: bool = False,
    ) -> Iterator[str]:
        """Get king pseudolegal squares (ignores king capture rules)."""
        yield from (
            sq
            for sq in king_navigable_squares(initial_square)
            if self._grid[sq] is None
        )
        if check_castle:
            yield from (
                CASTLING_FINAL_SQUARES[piece.color, side][1]
                for side in SIDES
                if self.can_castle(piece.color, side)
            )

    def can_explode_out_of_check(self, color: Color) -> bool:
        """Whether check can be resolved by exploding a threatening piece."""
        return all(
            self.can_explode_piece(sq)
            for sq, _ in self.get_threatening_pieces(self._kings[color], color).items()
        )

    @overload
    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        ignore_turn: bool = False,
        skip_checks: bool = False,
        no_disambiguator: bool = False,
        return_metadata: Literal[False],
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> None:
        ...

    @overload
    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        ignore_turn: bool = False,
        skip_checks: bool = False,
        no_disambiguator: bool = False,
        return_metadata: Literal[True],
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> dict[str, str | bool]:
        ...

    @overload
    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        ignore_turn: bool = False,
        skip_checks: bool = False,
        no_disambiguator: bool = False,
        return_metadata: bool = False,
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> dict[str, str | bool] | None:
        ...

    def _move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        allow_castle_and_en_passant: bool = True,
        ignore_turn: bool = False,
        skip_checks: bool = False,
        no_disambiguator: bool = False,
        return_metadata: bool = False,
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> dict[str, str | bool] | None:
        """Move a game piece."""
        if not game_over_checked:
            self._block_if_game_over()
        piece = self._get_piece_at_non_empty_square(initial_square)
        if not skip_checks and self._must_promote_pawn is not None:
            msg = (
                f"Must promote pawn at square '{self._must_promote_pawn}' "
                "before next move."
            )
            raise MoveError(msg)
        assert piece is not None
        if (
            not skip_checks
            and self._grid[final_square] is not None
            and (
                piece.piece_type == "king"
                or self._kings[piece.color] in king_navigable_squares(final_square)
            )
        ):
            msg = "Suicidal capture not allowed."
            raise MoveError(msg)
        if allow_castle_and_en_passant:
            # Try to castle if king is moving to a final castling square, or if rook is
            # jumping over a king.
            castle_side: Side = (
                "queenside" if final_square[0] in ("c", "d") else "kingside"
            )
            if (
                piece.piece_type == "king"
                and final_square in ("c1", "c8", "g1", "g8")
                and self.can_castle(piece.color, castle_side)
            ):
                self._castle(
                    piece.color,
                    castle_side,
                    skip_checks=True,
                    seconds_elapsed=seconds_elapsed,
                    glyphs=glyphs,
                )
                return (
                    {"move_type": "castle", "side": castle_side}
                    if return_metadata
                    else None
                )
            # Reroute to self.en_passant if pawn captures on empty final square.
            if (
                piece.piece_type == "pawn"
                and initial_square[0] != final_square[0]
                and self._grid[final_square] is None
            ):
                self._en_passant(
                    initial_square,
                    final_square,
                    seconds_elapsed=seconds_elapsed,
                    glyphs=glyphs,
                )
                return (
                    {"move_type": "en_passant", "capture": True}
                    if return_metadata
                    else None
                )

        if not skip_checks:
            # Check correct player's piece is being moved.
            if not ignore_turn and piece.color != self.turn:
                msg = f"It is {self.turn}'s turn."
                raise MoveError(msg)
            # Check piece can navigate to square.
            if final_square not in self._pseudolegal_squares(
                initial_square, check_castle=False
            ):
                msg = "Not a valid move."
                raise MoveError(msg)
            # Test if king would be in check if moved.
            king_would_be_in_check = False
            changes = {final_square: piece, initial_square: None}
            if self._grid[final_square] is not None:
                changes.update(self._explosion_dict(final_square))
            with self.test_position(changes):
                if self.king_is_in_check(self.turn):
                    king_would_be_in_check = True
            if king_would_be_in_check:
                msg = "Cannot move piece because king would be in check."
                raise MoveError(msg)

        # Add piece type notation, disambiguating if necessary.
        piece_at_final_square = self._grid[final_square]
        notation = (
            PLAINTEXT_ABBRS[piece.piece_type] if piece.piece_type != "pawn" else ""
        )
        notation += self._write_disambiguator(
            initial_square,
            final_square,
            piece,
            piece_at_final_square,
            no_disambiguator=no_disambiguator,
        )

        # Update clocks and notation to denote capture, and raise exceptions for illegal
        # captures.
        if piece_at_final_square is not None:
            if piece.piece_type == "pawn" and len(notation) == 0:
                notation += initial_square[0]
            notation += "x"
            is_capture = True
            if piece_at_final_square.color == piece.color:
                msg = "Cannot place piece at square occupied by same color piece."
                raise MoveError(msg)
            elif piece_at_final_square.piece_type == "king":
                msg = "Cannot capture king."
                raise MoveError(msg)
        else:
            is_capture = False
        notation += final_square

        # Update has_moved variables (used to determine castling availability).
        if piece.piece_type == "king":
            self._has_moved["king", piece.color, None] = True
        elif piece.piece_type == "rook":
            if initial_square == self._initial_squares.get(
                ("rook", piece.color, "kingside")
            ):
                side: Side | None = "kingside"
            elif initial_square == self._initial_squares.get(
                ("rook", piece.color, "queenside")
            ):
                side = "queenside"
            else:
                side = None
            if side is not None:
                self._has_moved["rook", piece.color, side] = True
        self._double_forward_last_move = (
            final_square
            if piece.piece_type == "pawn"
            and abs(int(initial_square[1]) - int(final_square[1])) == 2
            else None
        )

        # Move piece.
        self[initial_square] = None
        if not piece.has_moved and piece.piece_type == "pawn":
            piece = Piece(
                piece_type=piece.piece_type,
                color=piece.color,
                promoted=piece.promoted,
                has_moved=True,
            )
        self[final_square] = piece
        if is_capture:
            self._explode(final_square)

        # If pawn moving to final rank, require pawn promotion. Else, check for
        # check / checkmate, append moves, and return.
        if piece.piece_type == "pawn" and final_square[1] in ("1", "8"):
            self._must_promote_pawn = final_square
        else:
            self._must_promote_pawn = None
            if self.king_is_in_check(oc := other_color(self.turn)):
                if (
                    self.is_checkmate(kings_known_in_check=(oc,))
                    or self.king_exploded()
                ):
                    notation += "#"
                else:
                    notation += "+"
            self._alternate_turn(
                reset_halfmove_clock=(piece.piece_type == "pawn" or is_capture),
                seconds_elapsed=seconds_elapsed,
            )
        self._moves.append(notation)
        return (
            (
                {
                    "move_type": "normal",
                    "capture": is_capture,
                    "capture_piece_type": piece_at_final_square.piece_type,
                    "capture_piece_is_promoted": piece_at_final_square.promoted,
                }
                if piece_at_final_square is not None
                else {"move_type": "normal", "capture": is_capture}
            )
            if return_metadata
            else None
        )

    def _en_passant(
        self,
        initial_square: str,
        final_square: str,
        *,
        skip_checks: bool = False,
        game_over_checked: bool = False,
        seconds_elapsed: float | None = None,
        glyphs: str = "",
    ) -> None:
        """Capture an adjacent file pawn that has just made a double forward advance."""
        super()._en_passant(
            initial_square,
            final_square,
            skip_checks=skip_checks,
            game_over_checked=game_over_checked,
            seconds_elapsed=seconds_elapsed,
            glyphs=glyphs,
        )
        self._explode(final_square)
        self._moves[-1] = self._moves[-1].replace("+", "").replace("#", "")
        if self.king_is_in_check(self.turn):
            if (
                self.is_checkmate(kings_known_in_check=(self.turn,))
                or self.king_exploded()
            ):
                self._moves[-1] += "#"
            else:
                self._moves[-1] += "+"

    @property
    def status(self) -> GameStatus:
        """Check the board for a checkmate or draw."""
        if self.king_exploded():
            return self._status
        return super().status

    @overload
    def can_move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        check_turn: bool = True,
        navigability_already_checked: bool = False,
        return_explanation_if_false: Literal[False] = False,
    ) -> bool:
        ...

    @overload
    def can_move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        check_turn: bool = True,
        navigability_already_checked: bool = False,
        return_explanation_if_false: Literal[True],
    ) -> tuple[bool, str | None]:
        ...

    def can_move_piece(
        self,
        initial_square: str,
        final_square: str,
        *,
        check_turn: bool = True,
        navigability_already_checked: bool = False,
        return_explanation_if_false: bool = False,
    ) -> bool | tuple[bool, str | None]:
        """Check if a piece can be moved to final_square without castling/en passant."""
        piece = self._get_piece_at_non_empty_square(initial_square)
        piece_at_final_square = self._grid[final_square]
        if check_turn:
            self._check_turn(piece.color)
        if (
            not navigability_already_checked
            and final_square
            not in self._pseudolegal_squares(initial_square, check_castle=False)
        ):
            return (
                (
                    False,
                    f"Piece at '{initial_square}' cannot navigate to '{final_square}'.",
                )
                if return_explanation_if_false
                else False
            )
        if piece_at_final_square is not None and (
            (
                piece_at_final_square.piece_type == "king"
                and piece_at_final_square.color == piece.color
            )
            or piece.piece_type == "king"
        ):
            return (
                (False, "Cannot capture king.")
                if return_explanation_if_false
                else False
            )
        changes = {final_square: piece, initial_square: None}
        if piece_at_final_square is not None:
            changes.update(self._explosion_dict(final_square))
        with self.test_position(changes):
            if self.king_is_in_check(piece.color):
                return (
                    (
                        False,
                        f"Cannot move piece from '{initial_square}' to '{final_square}'"
                        " because player's king would be put in check.",
                    )
                    if return_explanation_if_false
                    else False
                )
        return (True, None) if return_explanation_if_false else True

    def is_checkmate(
        self, *, kings_known_in_check: tuple[Color, ...] | None = None
    ) -> bool:
        """Check if either color's king is checkmated."""
        if self.king_exploded():
            return True
        for color in COLORS:
            if (
                (
                    (kings_known_in_check is not None and color in kings_known_in_check)
                    or self.king_is_in_check(color)
                )
                and not self.can_block_or_capture_check(color)
                and not self.king_can_escape_check(color)
                and not self.can_explode_opponent_king(color)
                and not self.can_explode_out_of_check(color)
            ):
                self._status = GameStatus(
                    game_over=True, winner=other_color(color), description="checkmate"
                )
                return True
        return False

    @property
    def moves(self) -> str:
        """Export moves to string."""
        if self.is_checkmate():
            self._moves[-1] = f"{self._moves[-1].replace('+', '').replace('#', '')}#"
        return super().moves

    def checked_squares(self, color: Color) -> Iterator[str]:
        """Get all checked squares for a color."""
        oc = other_color(color)
        other_color_pieces = [
            sq for sq in self if (pc := self._grid[sq]) is not None and pc.color == oc
        ]
        protected_by_suicide_rule = king_navigable_squares(self._kings[oc])
        already_yielded: list[str] = []
        for init_sq in other_color_pieces:
            for sq in self._pseudolegal_squares(
                init_sq, capture_only=True, check_castle=False
            ):
                if sq not in already_yielded and sq not in protected_by_suicide_rule:
                    yield sq
                    already_yielded.append(sq)

    @overload
    def can_en_passant(
        self,
        initial_square: str | None = None,
        *,
        check_turn: bool = True,
        return_explanation_if_false: Literal[False] = False,
    ) -> bool:
        ...

    @overload
    def can_en_passant(
        self,
        initial_square: str | None = None,
        *,
        check_turn: bool = True,
        return_explanation_if_false: Literal[True],
    ) -> tuple[bool, str | None]:
        ...

    def can_en_passant(
        self,
        initial_square: str | None = None,
        *,
        check_turn: bool = True,
        return_explanation_if_false: bool = False,
    ) -> bool | tuple[bool, str | None]:
        """Check if an en passant capture is possible."""
        if self._double_forward_last_move is None:
            return (
                False
                if not return_explanation_if_false
                else (
                    False,
                    "En passant must follow a double forward pawn advance.",
                )
            )
        if initial_square is None:
            initial_square = self._infer_en_passant_initial_square()
            if initial_square is None:
                if return_explanation_if_false:
                    oc = other_color(self._grid[self._double_forward_last_move].color)  # type: ignore
                    return False, f"No {oc} pawns are able to capture by en passant."
                else:
                    return False
        capture_file = self._double_forward_last_move[0]
        piece = self._get_piece_at_non_empty_square(initial_square)
        if check_turn:
            self._check_turn(piece.color)
        if self._double_forward_last_move not in get_adjacent_squares(initial_square):
            return (
                False
                if not return_explanation_if_false
                else (
                    False,
                    "Capturing pawn must be directly adjacent to captured pawn.",
                )
            )
        color = piece.color
        final_sq = en_passant_final_square_from_file(capture_file, color)
        changes = {
            initial_square: None,
            final_sq: Piece("pawn", color),
            self._double_forward_last_move: None,
        }
        changes.update(self._explosion_dict(final_sq))
        with self.test_position(changes):
            if self.king_is_in_check(color):
                return (
                    False
                    if not return_explanation_if_false
                    else (
                        False,
                        "Cannot move because player's king would be put in check.",
                    )
                )
        return (True, None) if return_explanation_if_false else True
