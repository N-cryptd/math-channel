"""
Video 275: Roots and Radicals -- Numbers & Arithmetic (L1 Foundations, Video 10/14)

Inverse-pair spine (competitive analysis, improvements.md Sep 2026):
opens DIRECTLY on Video 274's closing teaser -- the ladder in reverse,
what undoes a square? -- framing roots as the fourth inverse pair
(- undoes +, / undoes x, sqrt undoes the power). Nobody in the niche
opens this way (they all open definition-first); the undo framing
continues the playlist's connected story. Then: radical/radicand named
AFTER the idea lands (Math Antics' proven ordering) -> the geometry of
the name (Domain of Science's 288K-on-the-name-alone beat: area -> side)
-> perfect-squares street (Mr. J's 1.5M pattern) -> the sandwich estimate
(3 < sqrt(10) < 4 on a number line; no competitor animates this) ->
sqrt(2) the irrational diagonal -> cube roots and the index (Khan's
negatives beat folded into scene 8) -> the x^2 = 9 vs sqrt(9) = 3
convention, stated once, after intuition -> the MindYourDecisions
superpower scene (cube root of 1728 in your head; their trick video is
the biggest in the entire space at 15.2M) -> Pythagoras payoff
(3-4-5, Math Antics' biggest video at 3.3M) -> summary + the Real
Number Line doorway (sqrt(2) has an address; curriculum row 11).

Scope discipline: simplifying-radicals technique (factoring out perfect
squares) is deliberately EXCLUDED -- Algebra Fundamentals material, not
Foundations row 10 (Math Antics' own catalog confirms the split).

Follows v2 template quality rules (5-item budget, LayoutEngine only,
progressive disclosure, SANS/MONO discipline, raw-string LaTeX).
"""

from manim import *
import sys, os
_template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "templates"))
if _template_dir not in sys.path:
    sys.path.insert(0, _template_dir)
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits


class Video275_RootsRadicals(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_meaning()
        self.scene3_geometry()
        self.scene4_perfect_squares()
        self.scene5_sandwich()
        self.scene6_irrational()
        self.scene7_cube_roots()
        self.scene8_negatives()
        self.scene9_pm_vs_root()
        self.scene10_mental_magic()
        self.scene11_habitat()
        self.scene12_summary()

    # ------------------------------------------------------------------
    # Scene 1: Hook - every operation has an undo
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Serial open on 274's teaser: what undoes a square?"""
        self.add_subcaption(
            "Last time ended with a question, so let us start there. "
            "Every operation you know has an undo. Addition builds up, "
            "subtraction takes it back. Multiplication repeats, division "
            "undoes it. These are inverse operations: partners walking "
            "the same road in opposite directions. Then came exponents, "
            "the jump. Two to the third leaps from two to eight in a "
            "single move. Multiplication was the slow walk; the exponent "
            "is the jump. And every jump raises the same question: what "
            "walks it backward? What number times itself makes nine? "
            "What undoes a square? That undo has a name and a symbol: it "
            "looks like a checkmark with a roof over its head, and it is "
            "called the root. Today we learn to read it, estimate with "
            "it, and discover which numbers it refuses to touch.",
            duration=50.5,
        )
        play_intro(self, "Roots and Radicals", "Numbers & Arithmetic")

        title = self.ly.title("The Undo Button")

        chain = MathTex(
            r"2^{3} = 8",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(chain)
        self.play(Write(chain), run_time=SLOW)
        self.wait(2)

        undo_line = MathTex(
            r"+ \leftrightarrow - \qquad \times \leftrightarrow \div"
            r" \qquad \left(\;\right)^{2} \leftrightarrow \, ?",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(undo_line, direction=DOWN, anchor=chain, buff=0.8)
        self.play(Write(undo_line), run_time=NORMAL)
        self.wait(2)

        question = MathTex(
            r"3^{2} = 9 \quad\Longrightarrow\quad \sqrt{9} = \, ?",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(question, direction=DOWN, anchor=undo_line, buff=0.7)
        self.play(FadeIn(question, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(34.8)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Meaning - what the radical asks, and its two names
    # ------------------------------------------------------------------
    def scene2_meaning(self):
        """sqrt(9) asks 'what times itself makes 9'; radical + radicand."""
        self.add_subcaption(
            "Here is the symbol in action: the square root of nine. It "
            "asks one question. What number, times itself, makes nine? "
            "Try three. Three times three is nine, so the square root of "
            "nine is three. The symbol itself is called the radical "
            "sign, and the number tucked underneath it is called the "
            "radicand. You will meet those two words in every math "
            "class from here to calculus, so let the names land now: "
            "the radical is the roof, and the radicand is what lives "
            "under it. Reading roots is now just a lookup. The square "
            "root of twenty-five asks, what times itself makes "
            "twenty-five? Five, because five times five is twenty-five. "
            "The square root of forty-nine is seven, because seven times "
            "seven is forty-nine. The radical turns every "
            "times-itself question into a clean, single answer.",
            duration=53.0,
        )
        self.ly.section_divider(1, "What the Symbol Asks")
        title = self.ly.title("The Question Under the Roof")

        root_q = MathTex(r"\sqrt{9} = \, ?", font_size=72, color=ACCENT)
        self.ly.center_in_content(root_q)
        self.play(Write(root_q), run_time=NORMAL)
        self.wait(2)

        answer = MathTex(r"\sqrt{9} = 3", font_size=72, color=ACCENT)
        answer.move_to(root_q)
        self.play(ReplacementTransform(root_q, answer), run_time=NORMAL)
        self.wait(2)

        rad_label = Text(
            "radical sign: the roof",
            font_size=LABEL_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(rad_label, direction=UP, anchor=answer, buff=0.4)
        radand_label = Text(
            "radicand: the number under it",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(radand_label, direction=DOWN, anchor=answer, buff=0.4)
        self.play(
            FadeIn(rad_label, shift=LEFT * 0.15),
            FadeIn(radand_label, shift=LEFT * 0.15),
            run_time=NORMAL,
        )
        self.wait(3)

        readings = MathTex(
            r"\sqrt{25} = 5 \qquad \sqrt{49} = 7",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.safe_place(readings, direction=DOWN, anchor=radand_label, buff=0.5)
        self.play(Write(readings), run_time=NORMAL)
        self.wait(37.1)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Geometry - the root of the square is its side
    # ------------------------------------------------------------------
    def scene3_geometry(self):
        """Why 'square': area 9 grid -> side 3; area 16 -> side 4."""
        self.add_subcaption(
            "Why is it called a square root? Draw it. A square with side "
            "three is a three by three grid, and it holds nine little "
            "cells. Three squared is nine: side three, area nine. Now "
            "run it backward. If a square holds nine cells, how long is "
            "its side? Three. The side is the root the square grew from. "
            "That is the whole name: the root of the square is the side "
            "that made it. Bigger squares, same story. A square of area "
            "sixteen has side four, because four times four is sixteen. "
            "A square of area twenty-five has side five. Area in, side "
            "out. Squaring goes from side to area, and the square root "
            "goes from area back to side. One direction builds, and the "
            "other direction asks how it was built.",
            duration=47.2,
        )
        self.ly.section_divider(2, "Why \u201cSquare\u201d?")
        title = self.ly.title("The Root of the Square")

        cells3 = VGroup(*[
            Square(side_length=0.5, stroke_color=PRIMARY, stroke_width=2,
                   fill_color=ACCENT, fill_opacity=0.35)
            for _ in range(9)
        ]).arrange_in_grid(rows=3, cols=3, buff=0.06)
        self.ly.center_in_content(cells3)
        self.play(FadeIn(cells3, lag_ratio=0.15), run_time=NORMAL)
        self.wait(2)

        labels3 = VGroup(
            MathTex(r"\text{side } 3", font_size=LABEL_SIZE, color=WHITE),
            MathTex(r"\text{area } 9", font_size=LABEL_SIZE, color=SECONDARY),
        ).arrange(RIGHT, buff=1.0)
        self.ly.safe_place(labels3, direction=DOWN, anchor=cells3, buff=0.45)
        self.play(FadeIn(labels3, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        self.play(FadeOut(cells3), FadeOut(labels3), run_time=FAST)

        cells4 = VGroup(*[
            Square(side_length=0.38, stroke_color=SECONDARY, stroke_width=2,
                   fill_color=ACCENT, fill_opacity=0.35)
            for _ in range(16)
        ]).arrange_in_grid(rows=4, cols=4, buff=0.06)
        self.ly.center_in_content(cells4)
        self.play(FadeIn(cells4, lag_ratio=0.1), run_time=NORMAL)
        self.wait(2)

        labels4 = VGroup(
            MathTex(r"\text{side } 4", font_size=LABEL_SIZE, color=WHITE),
            MathTex(r"\text{area } 16", font_size=LABEL_SIZE, color=SECONDARY),
        ).arrange(RIGHT, buff=1.0)
        self.ly.safe_place(labels4, direction=DOWN, anchor=cells4, buff=0.45)
        self.play(FadeIn(labels4, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(31.8)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Perfect squares - the two-way street
    # ------------------------------------------------------------------
    def scene4_perfect_squares(self):
        """5^2 = 25 <=> sqrt(25) = 5; the ten perfect squares."""
        self.add_subcaption(
            "Some numbers are famous enough to deserve their own street. "
            "Take five and square it, you get twenty-five. Take the "
            "square root of twenty-five, you are back to five. Squaring "
            "and rooting are a two-way street, and the perfect squares "
            "are the addresses where the trip lands exactly. Here are "
            "the first ten: one, four, nine, sixteen, twenty-five, "
            "thirty-six, forty-nine, sixty-four, eighty-one, one "
            "hundred. Each one is a whole number times itself. Know this "
            "row cold, and roots stop being mysterious: the square root "
            "of sixty-four is eight, the square root of eighty-one is "
            "nine, no calculator required. Every perfect square has a "
            "whole-number root. And numbers between them, like ten or "
            "fifty? Their roots are still perfectly good numbers, but "
            "they land between the addresses, and that is exactly where "
            "we go next.",
            duration=55.2,
        )
        self.ly.section_divider(3, "Perfect Squares")
        title = self.ly.title("The Two-Way Street")

        two_way = MathTex(
            r"5^{2} = 25 \qquad \sqrt{25} = 5",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.center_in_content(two_way)
        self.play(Write(two_way), run_time=SLOW)
        self.wait(2)

        arrows = MathTex(
            r"\text{square} \;\rightleftarrows\; \text{take the root}",
            font_size=LABEL_SIZE, color=DIM,
        )
        self.ly.safe_place(arrows, direction=DOWN, anchor=two_way, buff=0.5)
        self.play(FadeIn(arrows, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        chain = MathTex(
            r"1,\; 4,\; 9,\; 16,\; 25,\; 36,\; 49,\; 64,\; 81,\; 100",
            font_size=BODY_SIZE, color=ACCENT,
        )
        ensure_fits(chain)
        self.ly.safe_place(chain, direction=DOWN, anchor=arrows, buff=0.6)
        self.play(Write(chain), run_time=SLOW)
        self.wait(2)

        note = Text(
            "every perfect square has a whole-number root",
            font_size=LABEL_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=chain, buff=0.5)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(38.8)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: The sandwich - pin any root between perfect squares
    # ------------------------------------------------------------------
    def scene5_sandwich(self):
        """sqrt(10) between 3 and 4; sqrt(50) between 7 and 8; number line."""
        self.add_subcaption(
            "Where does the square root of ten land? Nine is three "
            "squared and sixteen is four squared, and ten sits between "
            "them, so the root of ten must sit between three and four. "
            "It is about three point one six, but the sandwich already "
            "tells us what we need: bigger than three, smaller than "
            "four. This trick pins any root without a calculator. The "
            "square root of fifty? Forty-nine is seven squared and "
            "sixty-four is eight squared, so the root of fifty is "
            "squeezed between seven and eight, just barely above seven. "
            "The root of twenty? Sixteen is four squared and twenty-five "
            "is five squared, so it lives between four and five. On the "
            "number line, every root has an address, and the perfect "
            "squares on either side bracket it like fence posts. No "
            "buttons pressed, and we are already within a hair of the "
            "truth.",
            duration=53.0,
        )
        self.ly.section_divider(4, "The Sandwich Trick")
        title = self.ly.title("Pin It Between Squares")

        row1 = MathTex(
            r"9 < 10 < 16 \;\Longrightarrow\; 3 < \sqrt{10} < 4",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(row1, direction=DOWN, anchor=title, buff=0.8)
        self.play(Write(row1), run_time=SLOW)
        self.wait(2)

        row2 = MathTex(
            r"49 < 50 < 64 \;\Longrightarrow\; 7 < \sqrt{50} < 8",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(row2, direction=DOWN, anchor=row1, buff=0.5)
        self.play(Write(row2), run_time=SLOW)
        self.wait(2)

        number_line = VGroup(
            NumberLine(
                x_range=[2.6, 4.4, 0.2], length=6.0,
                include_ticks=True, include_numbers=False,
                stroke_color=DIM, stroke_width=2, tick_size=0.06,
            ),
            MathTex(r"3", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"4", font_size=LABEL_SIZE, color=PRIMARY),
            MathTex(r"\sqrt{10}", font_size=LABEL_SIZE, color=ACCENT),
            Dot(color=ACCENT, radius=0.07),
        )
        line = number_line[0]
        number_line[1].next_to(line.number_to_point(3.0), DOWN, buff=0.15)
        number_line[2].next_to(line.number_to_point(4.0), DOWN, buff=0.15)
        number_line[3].next_to(line.number_to_point(3.2), UP, buff=0.15)
        number_line[4].move_to(line.number_to_point(3.162))
        self.ly.safe_place(number_line, direction=DOWN, anchor=row2, buff=0.8)
        self.play(FadeIn(number_line, lag_ratio=0.1), run_time=NORMAL)
        self.wait(39.7)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: The irrational - sqrt(2), the diagonal that never ends
    # ------------------------------------------------------------------
    def scene6_irrational(self):
        """Unit square diagonal: 1.4^2, 1.5^2, 1.4142...; irrational."""
        self.add_subcaption(
            "Now the most famous root of all. Draw a square with sides "
            "of length one, and measure its diagonal. The diagonal is "
            "the square root of two. So what is its value? Squeeze it. "
            "One point four squared is one point nine six, just under "
            "two. One point five squared is two point two five, just "
            "over. So the root sits between them. One point four one "
            "squared lands closer. One point four one four two, closer "
            "still. And here is the shock: the digits never stop and "
            "never repeat. Write the square root of two to a billion "
            "places, and no pattern ever emerges. It cannot be written "
            "as any fraction of whole numbers, and that earns it the "
            "name irrational. Not crazy, just outside the fraction "
            "world. Two simple numbers, one and one, build a diagonal "
            "that never simplifies.",
            duration=52.3,
        )
        self.ly.section_divider(5, "The Diagonal That Never Ends")
        title = self.ly.title("A Root With No Fraction")

        square = VGroup(
            Square(side_length=2.0, stroke_color=PRIMARY, stroke_width=3),
            Line(ORIGIN, RIGHT * 2 + UP * 2, color=ACCENT, stroke_width=3),
            MathTex(r"\sqrt{2}", font_size=LABEL_SIZE, color=ACCENT),
            MathTex(r"1", font_size=LABEL_SIZE, color=WHITE),
        )
        square[2].move_to(square[1].get_center() + UP * 0.35)
        square[3].next_to(square[0], DOWN, buff=0.15)
        self.ly.center_in_content(square)
        self.play(Create(square), run_time=SLOW)
        self.wait(2)

        digits = MathTex(
            r"\sqrt{2} = 1.4142\ldots \qquad"
            r" (1.4)^{2} = 1.96 \quad (1.5)^{2} = 2.25",
            font_size=BODY_SIZE, color=WHITE,
        )
        ensure_fits(digits)
        self.ly.safe_place(digits, direction=DOWN, anchor=square, buff=0.55)
        self.play(Write(digits), run_time=SLOW)
        self.wait(2)

        card = Text(
            "irrational: never ends, never repeats, no fraction",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(card, direction=DOWN, anchor=digits, buff=0.5)
        self.play(FadeIn(card, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(39.0)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Cube roots and the index
    # ------------------------------------------------------------------
    def scene7_cube_roots(self):
        """Undo a cube: cbrt(8)=2, cbrt(27)=3; the index; 4th root."""
        self.add_subcaption(
            "Roots are a family, and the small number tucked in the hook "
            "of the radical picks the member. The square root of eight "
            "is unremarkable, but the cube root of eight is delightful: "
            "what number times itself three times makes eight? Two, "
            "because two times two times two is eight. That little three "
            "is called the index, and it names the undo. Index two "
            "undoes squares, index three undoes cubes. Cubed means "
            "volume, so cube roots go from volume back to side: a cube "
            "of volume twenty-seven has side three. Push the index higher "
            "and the pattern holds. The fourth root of sixteen is two, "
            "because two to the fourth is sixteen. The index simply "
            "tells you how many equal factors you are hunting, and the "
            "radical rounds them up.",
            duration=48.7,
        )
        self.ly.section_divider(6, "Cube Roots and the Index")
        title = self.ly.title("Undoing Cubes")

        eq1 = MathTex(
            r"\sqrt[3]{8} = 2 \qquad \sqrt[3]{27} = 3",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(eq1)
        self.play(Write(eq1), run_time=SLOW)
        self.wait(2)

        index_label = Text(
            "the index: which power you are undoing",
            font_size=LABEL_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(index_label, direction=DOWN, anchor=eq1, buff=0.5)
        self.play(FadeIn(index_label, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        eq2 = MathTex(
            r"\sqrt[4]{16} = 2",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(eq2, direction=DOWN, anchor=index_label, buff=0.5)
        self.play(Write(eq2), run_time=NORMAL)
        self.wait(36.3)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Negative radicands - odd roots sail, even roots refuse
    # ------------------------------------------------------------------
    def scene8_negatives(self):
        """cbrt(-8) = -2; sqrt(-9) has no real answer."""
        self.add_subcaption(
            "Can a root be negative? For odd roots, absolutely. Minus "
            "two, times itself three times, is minus eight, so the cube "
            "root of minus eight is minus two. The cube root of minus "
            "twenty-seven is minus three. Negative in, negative out, no "
            "drama: an odd number of negative factors stays negative. "
            "Even roots are a different animal. What is the square root "
            "of minus nine? We need a number whose square is minus nine. "
            "Try three: nine. Try minus three: minus three times minus "
            "three is plus nine. Both signs square positive. No real "
            "number, no matter how far we search, squares to a negative. "
            "So the square root of a negative number has no answer among "
            "the numbers we know. It is not an error. It is a door, and "
            "it stays locked until a future video builds a whole new "
            "kind of number behind it.",
            duration=53.9,
        )
        self.ly.section_divider(7, "Odd Roots, Even Roots")
        title = self.ly.title("Negatives: A Divide")

        odd_row = MathTex(
            r"\sqrt[3]{-8} = -2 \qquad \sqrt[3]{-27} = -3",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(odd_row)
        self.play(Write(odd_row), run_time=SLOW)
        self.wait(2)

        even_q = MathTex(
            r"\sqrt{-9} = \, ?", font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(even_q, direction=DOWN, anchor=odd_row, buff=0.6)
        self.play(Write(even_q), run_time=NORMAL)
        self.wait(2)

        card = Text(
            "no real answer: both signs square positive",
            font_size=LABEL_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(card, direction=DOWN, anchor=even_q, buff=0.5)
        self.play(FadeIn(card, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(41.5)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: x^2 = 9 vs sqrt(9) - the principal root convention
    # ------------------------------------------------------------------
    def scene9_pm_vs_root(self):
        """x^2 = 9 -> x = +-3, but sqrt(9) = 3 only; the convention."""
        self.add_subcaption(
            "One careful distinction, and it settles a classic exam "
            "trap. Solve x squared equals nine. Two numbers work: three "
            "and minus three. So x equals plus or minus three. But the "
            "radical symbol is pickier. The square root of nine means "
            "exactly three, never minus three. Same equation, different "
            "questions. The equation asks for every possible suspect, "
            "and there are two. The radical asks for one specific "
            "number, and the convention says: the positive one. This is "
            "not an oversight that mathematicians forgot to fix. It is "
            "a definition, chosen so the square root always returns a "
            "single, dependable value, which is exactly what a function "
            "needs. So read carefully: x squared equals nine has two "
            "solutions, and the square root of nine is one number: "
            "three.",
            duration=52.5,
        )
        self.ly.section_divider(8, "Two Answers or One")
        title = self.ly.title("Equation vs Symbol")

        eq1 = MathTex(
            r"x^{2} = 9 \;\Longrightarrow\; x = \pm 3",
            font_size=HEADING_SIZE, color=WHITE,
        )
        self.ly.center_in_content(eq1)
        self.play(Write(eq1), run_time=SLOW)
        self.wait(2)

        eq2 = MathTex(
            r"\sqrt{9} = 3 \quad \text{only}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq2, direction=DOWN, anchor=eq1, buff=0.6)
        self.play(Write(eq2), run_time=NORMAL)
        self.wait(2)

        box = Text(
            "the radical always means the positive root",
            font_size=LABEL_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(box, direction=DOWN, anchor=eq2, buff=0.5)
        self.play(FadeIn(box, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(40.1)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Mental magic - cube root of 1728 in your head
    # ------------------------------------------------------------------
    def scene10_mental_magic(self):
        """MindYourDecisions superpower: last digit + size bracket."""
        self.add_subcaption(
            "Now the party trick. The cube root of one thousand seven "
            "hundred twenty-eight, in your head, in ten seconds. Step "
            "one: look at the last digit. It is an eight, and cubes "
            "ending in eight always come from numbers ending in two, so "
            "our answer ends in a two. Step two: bracket the size. Ten "
            "cubed is one thousand, and twenty cubed is eight thousand. "
            "Our number sits between them, so the answer sits between "
            "ten and twenty. One number between ten and twenty ends in "
            "a two: twelve. Check it. Twelve cubed is one hundred "
            "forty-four, and one hundred forty-four times twelve is one "
            "thousand seven hundred twenty-eight. Twelve. You just did, "
            "in your head, what looks like it needs a calculator, and "
            "the trick generalizes: the last digit gives the ending, "
            "and the easy cubes give the size.",
            duration=52.6,
        )
        self.ly.section_divider(9, "A Root in Your Head")
        title = self.ly.title("The Cube Root Trick")

        expr = MathTex(r"\sqrt[3]{1728} = \, ?",
                       font_size=HEADING_SIZE, color=ACCENT)
        self.ly.center_in_content(expr)
        self.play(Write(expr), run_time=SLOW)
        self.wait(2)

        step1 = Text(
            "last digit 8  \u2192  answer ends in 2",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(step1, direction=DOWN, anchor=expr, buff=0.5)
        self.play(FadeIn(step1, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        step2 = Text(
            "between 10\u00b3 = 1000 and 20\u00b3 = 8000",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(step2, direction=DOWN, anchor=step1, buff=0.4)
        self.play(FadeIn(step2, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(2)

        check = MathTex(
            r"12^{3} = 12 \cdot 12 \cdot 12 = 1728",
            font_size=BODY_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(check, direction=DOWN, anchor=step2, buff=0.4)
        self.play(Write(check), run_time=NORMAL)
        self.wait(36.9)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 11: Habitat - Pythagoras, the 3-4-5 triangle
    # ------------------------------------------------------------------
    def scene11_habitat(self):
        """Where roots live: 3-4-5 triangle, 9+16=25, sqrt(25)=5."""
        self.add_subcaption(
            "Where do roots earn their living? Everywhere lengths hide. "
            "Here is the most famous triangle in mathematics: legs of "
            "three and four meeting at a right angle. Square each leg "
            "and the squares hold nine and sixteen. Together they hold "
            "twenty-five, and the long side of the triangle, the "
            "hypotenuse, is the side of a square with area twenty-five. "
            "Its length is the square root of twenty-five, which is "
            "five. The three, four, five triangle, straight out of a "
            "root. That is the pattern in general. Area back to side, "
            "volume back to edge, diagonal back to length: roots convert "
            "measurements of space into lengths you can hold. Whenever "
            "geometry hands you a squared quantity and asks for a "
            "distance, the radical is the bridge. And that diagonal from "
            "earlier? The square root of two is about to send us "
            "somewhere new.",
            duration=53.8,
        )
        self.ly.section_divider(10, "Where Roots Live")
        title = self.ly.title("The Three Four Five")

        triangle = VGroup(
            Polygon(
                LEFT * 1.0 + DOWN * 0.75, RIGHT * 1.0 + DOWN * 0.75,
                RIGHT * 1.0 + UP * 0.75,
                stroke_color=PRIMARY, stroke_width=3,
                fill_color=PRIMARY, fill_opacity=0.12,
            ),
            MathTex(r"4", font_size=LABEL_SIZE, color=WHITE),
            MathTex(r"3", font_size=LABEL_SIZE, color=WHITE),
            MathTex(r"5", font_size=LABEL_SIZE, color=ACCENT),
        )
        triangle[1].next_to(triangle[0], DOWN, buff=0.15)
        triangle[2].next_to(triangle[0], RIGHT, buff=0.15)
        triangle[3].next_to(triangle[0].get_center(), UP, buff=0.35).shift(RIGHT * 0.6)
        self.ly.center_in_content(triangle)
        self.play(Create(triangle), run_time=SLOW)
        self.wait(2)

        pythag = MathTex(
            r"3^{2} + 4^{2} = 9 + 16 = 25",
            font_size=BODY_SIZE, color=WHITE,
        )
        self.ly.safe_place(pythag, direction=DOWN, anchor=triangle, buff=0.5)
        self.play(Write(pythag), run_time=NORMAL)
        self.wait(2)

        root_line = MathTex(
            r"\text{hypotenuse} = \sqrt{25} = 5",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(root_line, direction=DOWN, anchor=pythag, buff=0.5)
        self.play(Write(root_line), run_time=NORMAL)
        self.wait(41.4)  # pacing: extends caption slot to natural + 1.2
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 12: Summary + outro
    # ------------------------------------------------------------------
    def scene12_summary(self):
        """Recap the map; tease the Real Number Line."""
        self.add_subcaption(
            "Let us fold the map. A root is the undo of a power: the "
            "square root of nine asks what times itself makes nine, and "
            "the index picks which power you are undoing. Perfect "
            "squares have whole-number roots, and every other root "
            "hides neatly between them: sandwich it between neighboring "
            "squares. Cube roots undo volumes and happily take "
            "negatives, while even roots refuse them. The equation x "
            "squared equals nine has two answers, but the radical "
            "symbol itself always means the positive one. And some "
            "roots, like the square root of two, never become "
            "fractions: one point four one four two, on and on forever. "
            "Yet that endless decimal sits at a definite address on the "
            "number line, between one point four and one point five. "
            "Next time we map every address: the real number line. See "
            "you then.",
            duration=53.6,
        )
        self.ly.section_divider(11, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("A root undoes a power: sqrt(9) = 3 because 3x3 = 9",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Perfect squares give whole roots: sqrt(49) = 7",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Sandwich any root: 3 < sqrt(10) < 4",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Odd roots take negatives; even roots refuse them",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("sqrt(2) = 1.4142...: an address on the number line",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(42.7)  # pacing: last caption slot (incl. outro) >= natural + 2.0
        self.ly.clear()
        play_outro(self, next_video="The Real Number Line",
                   next_playlist="Numbers & Arithmetic")
