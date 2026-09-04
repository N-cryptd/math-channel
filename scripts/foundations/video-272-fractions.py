"""
Video 272: Fractions -- Numbers & Arithmetic (L1 Foundations, Video 7/14)

The gap between the integers: cutting one whole into equal parts,
numerator/denominator vocabulary, counting parts past one whole,
fractions as numbers on the number line, equivalent fractions as the
same point, division creating fractions (3 / 4 = 3/4, tying back to
Video 270), improper vs mixed numbers, and fractions in the wild.
Connects back to Video 271 (Negative Numbers) and forward to
Video 273 (Decimals).

Based on competitive analysis (improvements.md, Sep 2026): Math Antics
owns the static-whiteboard fraction space; we differentiate with the
serial number-line story (271 -> 272), a rectangle/line model instead
of pies, and a division payoff competitors skip.

Follows v2 template quality rules.
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


class Video272_Fractions(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_equal_parts()
        self.scene3_vocabulary()
        self.scene4_counting_parts()
        self.scene5_fractions_are_numbers()
        self.scene6_equivalent()
        self.scene7_division_payoff()
        self.scene8_past_one_whole()
        self.scene9_in_the_wild()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _bar(self, parts, shaded, width=7.0, height=0.6,
             line_color=PRIMARY, fill_color=ACCENT):
        """A unit bar cut into `parts` equal cells, first `shaded` filled.

        Returns VGroup(cells, shades) -- cells carry the outline,
        shades overlay the filled portion.
        """
        w = width / parts
        cells = VGroup(*[
            Rectangle(width=w, height=height, color=line_color,
                      stroke_width=2.5)
            for _ in range(parts)
        ]).arrange(RIGHT, buff=0)
        shades = VGroup(*[
            Rectangle(width=w, height=height, stroke_width=0,
                      fill_color=fill_color, fill_opacity=0.85)
            .move_to(cells[i])
            for i in range(shaded)
        ])
        return VGroup(cells, shades)

    def _bar_label(self, bar_group, top, bottom, color=ACCENT):
        """Fraction label placed to the right of a bar group."""
        tex = MathTex(
            r"\tfrac{" + str(top) + r"}{" + str(bottom) + r"}",
            font_size=HEADING_SIZE, color=color,
        )
        tex.next_to(bar_group, RIGHT, buff=0.4)
        return tex

    # ------------------------------------------------------------------
    # Scene 1: Hook - the empty middle
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: the number line has a hole between 0 and 1."""
        self.add_subcaption(
            "Last time, the number line grew to the left of zero, and "
            "every integer found a home. But look closely between zero "
            "and one: the line is empty. No counting number lives "
            "there, no integer at all. And yet the gap is real. Cut an "
            "apple in two, and you are holding something strictly "
            "between nothing and one: half the apple. Pour half a "
            "glass of juice, walk half a mile, wait half an hour. "
            "Whatever the whole is, we constantly deal with parts of "
            "it, and the integers are helpless to name them. Today we "
            "fix that. We will cut one whole into equal parts, learn "
            "the two numbers that name a fraction, discover that "
            "fractions are genuine numbers with homes on the number "
            "line, and prove that division itself creates them. Let "
            "us fill the gap.",
            duration=57,
        )
        play_intro(self, "Fractions", "Numbers & Arithmetic")

        title = self.ly.title("The Empty Middle")

        line = NumberLine(
            x_range=[0, 3, 1], length=11,
            color=DIM, include_numbers=True, font_size=LABEL_SIZE,
        )
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=SLOW)

        gap = Line(
            line.n2p(0), line.n2p(1),
            color=ACCENT, stroke_width=9,
        )
        qmark = MathTex(r"?", font_size=HEADING_SIZE, color=ACCENT)
        qmark.next_to(gap, UP, buff=0.25)
        self.play(Create(gap), run_time=NORMAL)
        self.play(Write(qmark), run_time=FAST)
        self.wait(6)

        prompt = Text(
            "No integer lives between 0 and 1 -- yet we hold half an apple",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(prompt, direction=DOWN, anchor=line, buff=0.6)
        self.play(FadeIn(prompt, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(33)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Cutting one whole into equal parts
    # ------------------------------------------------------------------
    def scene2_equal_parts(self):
        """Halves, thirds, quarters from one chocolate bar."""
        self.add_subcaption(
            "Start with one whole: a single chocolate bar, one "
            "unbroken unit. Cut it into two equal pieces. Each piece "
            "is one half, written as a one over a two. Equal is the "
            "magic word: the pieces must be identical in size, or the "
            "name is a lie. Now take a fresh bar and cut it into three "
            "equal pieces. Each piece is one third, one over three. "
            "And a third bar, cut into four equal pieces: each piece "
            "is one quarter, one over four. Notice the pattern: the "
            "bottom number counts the equal parts the whole was split "
            "into. Two parts, three parts, four parts: halves, thirds, "
            "quarters. The whole never changed. We only changed how "
            "finely we sliced it, and each slice got a name.",
            duration=58,
        )
        self.ly.section_divider(1, "Cutting One Whole")
        title = self.ly.title("One Bar, Many Slices")

        half = self._bar(2, 1)
        half_label = self._bar_label(half, 1, 2, color=PRIMARY)
        half.add(half_label)

        third = self._bar(3, 1)
        third_label = self._bar_label(third, 1, 3, color=SECONDARY)
        third.add(third_label)

        quarter = self._bar(4, 1)
        quarter_label = self._bar_label(quarter, 1, 4, color=ACCENT)
        quarter.add(quarter_label)

        stacked, _overflow = self.ly.stack_down(
            [half, third, quarter], start_from=title, spacing=0.55,
        )
        for grp in stacked:
            self.play(FadeIn(grp, shift=LEFT * 0.15), run_time=NORMAL)
            self.wait(4)
        self.wait(31)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Numerator and denominator
    # ------------------------------------------------------------------
    def scene3_vocabulary(self):
        """The two numbers of a fraction and their jobs."""
        self.add_subcaption(
            "Every fraction carries two numbers, and each has a job. "
            "On top sits the numerator: it counts how many parts we "
            "have taken. Below sits the denominator: it says how many "
            "equal parts make one whole. Here is three quarters. The "
            "whole was cut into four equal parts; that is the "
            "denominator. We hold three of them; that is the "
            "numerator. A memory trick that has saved students for "
            "centuries: denominator begins with D, like down, and it "
            "is always the bottom number. The denominator names the "
            "size of the pieces, and the numerator counts them. "
            "Change the denominator and you change the size of every "
            "piece. Change the numerator and you change how many "
            "pieces you hold. That is the entire grammar of "
            "fractions.",
            duration=56,
        )
        self.ly.section_divider(2, "Two Numbers, Two Jobs")
        title = self.ly.title("Numerator and Denominator")

        fb = self.ly.formula_box(
            MathTex(r"\dfrac{3}{4}", font_size=TITLE_SIZE, color=ACCENT)
        )
        self.play(Write(fb[0]), run_time=NORMAL)
        self.play(Create(fb[1]), run_time=FAST)
        self.wait(3)

        top_note = Text(
            "Numerator (top): how many parts we hold",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(top_note, direction=DOWN, anchor=fb, buff=0.45)
        self.play(FadeIn(top_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)

        bottom_note = Text(
            "Denominator (down): equal parts in the whole",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(bottom_note, direction=DOWN, anchor=top_note, buff=0.3)
        self.play(FadeIn(bottom_note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(23)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Counting parts, filling up, passing one
    # ------------------------------------------------------------------
    def scene4_counting_parts(self):
        """1/4 to 4/4 = 1, then a fifth piece from a fresh bar."""
        self.add_subcaption(
            "Fractions count parts, so let us count. Our bar is cut "
            "into quarters. One shaded piece: one quarter. Two pieces: "
            "two quarters. Three: three quarters. And four shaded "
            "pieces, the complete bar: four quarters, which fills "
            "exactly one whole. Four quarters and one whole are two "
            "names for the same amount. Now reach for a fifth piece "
            "from a fresh bar: five quarters, more than one whole. "
            "This is worth pausing on. A fraction is not a broken "
            "thing, a fragment stuck below one. It is a count of "
            "equal pieces, and counts can pass one, ten, or a hundred. "
            "Nothing breaks when we cross the whole: the pieces simply "
            "keep stacking.",
            duration=47,
        )
        self.ly.section_divider(3, "Counting Parts")
        title = self.ly.title("Filling Up Quarters")

        bar = self._bar(4, 0)
        self.ly.center_in_content(bar)
        self.play(Create(bar[0]), run_time=NORMAL)

        shades = [
            Rectangle(width=bar[0][0].width, height=0.6, stroke_width=0,
                      fill_color=ACCENT, fill_opacity=0.85)
            .move_to(bar[0][i])
            for i in range(4)
        ]
        label = MathTex(r"\tfrac{1}{4}", font_size=HEADING_SIZE, color=ACCENT)
        self.ly.safe_place(label, direction=DOWN, anchor=bar, buff=0.45)

        self.play(FadeIn(shades[0]), run_time=FAST)
        self.play(Write(label), run_time=FAST)
        self.wait(2)
        for i in range(1, 4):
            new_label = MathTex(
                r"\tfrac{" + str(i + 1) + r"}{4}",
                font_size=HEADING_SIZE, color=ACCENT,
            ).move_to(label)
            self.play(FadeIn(shades[i]), run_time=FAST)
            self.play(Transform(label, new_label), run_time=FAST)
            self.wait(2)

        fb = self.ly.formula_box(
            MathTex(r"\tfrac{4}{4} = 1", font_size=HEADING_SIZE, color=SECONDARY)
        )
        self.ly.safe_place(fb, direction=DOWN, anchor=label, buff=0.4)
        self.play(Write(fb[0]), run_time=NORMAL)
        self.play(Create(fb[1]), run_time=FAST)
        self.wait(9)
        self.ly.clear()

        # Fifth piece from a fresh bar
        title2 = self.ly.title("Past One Whole")
        whole = self._bar(4, 4, width=5.0)
        extra_cell = Rectangle(
            width=5.0 / 4, height=0.6, color=PRIMARY, stroke_width=2.5,
        )
        row = VGroup(whole, extra_cell).arrange(RIGHT, buff=0.25)
        self.ly.center_in_content(row)
        self.play(FadeIn(whole, shift=LEFT * 0.15), run_time=NORMAL)
        self.play(FadeIn(extra_cell, scale=0.6), run_time=NORMAL)

        more = MathTex(
            r"\tfrac{5}{4} > 1", font_size=HEADING_SIZE, color=RED,
        )
        self.ly.safe_place(more, direction=DOWN, anchor=row, buff=0.4)
        self.play(Write(more), run_time=NORMAL)
        self.wait(20)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: Fractions are numbers on the line
    # ------------------------------------------------------------------
    def scene5_fractions_are_numbers(self):
        """Quarter ticks between 0 and 1; counting past 1."""
        self.add_subcaption(
            "Here is the idea that turns slices into mathematics. "
            "Draw the line from zero to one, and cut that unit "
            "interval exactly the way we cut the bar: into four equal "
            "segments. The cut points are numbers. One quarter sits "
            "here, two quarters there, three quarters next, and four "
            "quarters lands precisely on one. Fractions do not just "
            "describe parts of bars: they are numbers, with addresses "
            "on the number line, parked between the integers that "
            "once looked so alone. And there is nothing special about "
            "stopping at one. Keep counting by quarters past one: "
            "five quarters, six quarters. Between any two integers, "
            "the fractions are waiting. The line is officially full.",
            duration=49,
        )
        self.ly.section_divider(4, "Fractions Are Numbers")
        title = self.ly.title("Addresses on the Line")

        line = NumberLine(
            x_range=[0, 2, 0.25], length=12,
            color=PRIMARY, include_numbers=False,
            include_ticks=True, tick_size=0.1,
        )
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=SLOW)

        unit = Line(
            line.n2p(0), line.n2p(1),
            color=ACCENT, stroke_width=7,
        )
        self.play(Create(unit), run_time=NORMAL)

        int_labels = VGroup(*[
            MathTex(str(i), font_size=LABEL_SIZE, color=WHITE)
            .next_to(line.n2p(i), DOWN, buff=0.25)
            for i in range(3)
        ])
        self.play(FadeIn(int_labels, lag_ratio=0.2), run_time=NORMAL)
        self.wait(5)

        frac_labels = VGroup(*[
            MathTex(r"\tfrac{" + str(k) + r"}{4}",
                    font_size=LABEL_SIZE, color=ACCENT)
            .next_to(line.n2p(k / 4), UP, buff=0.25)
            for k in (1, 2, 3)
        ])
        self.play(FadeIn(frac_labels, lag_ratio=0.3), run_time=NORMAL)
        self.wait(7)

        past = VGroup(*[
            MathTex(r"\tfrac{" + str(4 + k) + r"}{4}",
                    font_size=LABEL_SIZE, color=RED)
            .next_to(line.n2p(1 + k / 4), UP, buff=0.25)
            for k in (1, 2)
        ])
        self.play(FadeIn(past, lag_ratio=0.3), run_time=NORMAL)
        self.wait(25)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Equivalent fractions
    # ------------------------------------------------------------------
    def scene6_equivalent(self):
        """1/2 = 2/4: same shaded amount, same point."""
        self.add_subcaption(
            "Take half a bar. Now take a fresh bar, cut it into "
            "quarters, and shade two of them. Compare the shaded "
            "amounts: they match exactly. One half and two quarters "
            "are two names for one and the same number, because they "
            "mark one and the same point on the line. We say they are "
            "equivalent. Cut finer still: three sixths, four eighths, "
            "all landing on that same point. Multiplying the top and "
            "bottom of a fraction by the same number never moves the "
            "point; it only renames it. Two quarters is one half seen "
            "in finer resolution. This is not a trick to memorize for "
            "a test: it is one quantity measured in different units, "
            "and it will power everything from simplifying fractions "
            "to adding them.",
            duration=54,
        )
        self.ly.section_divider(5, "Same Point, Different Name")
        title = self.ly.title("Half, Sliced Finer")

        bar_a = self._bar(2, 1)
        la = self._bar_label(bar_a, 1, 2, color=PRIMARY)
        bar_a.add(la)

        bar_b = self._bar(4, 2)
        lb = self._bar_label(bar_b, 2, 4, color=SECONDARY)
        bar_b.add(lb)

        stacked, _ = self.ly.stack_down(
            [bar_a, bar_b], start_from=title, spacing=0.5,
        )
        self.play(FadeIn(stacked[0], shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(3)
        self.play(FadeIn(stacked[1], shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(7)

        eq = MathTex(
            r"\tfrac{1}{2} = \tfrac{2}{4}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq, direction=DOWN, anchor=stacked, buff=0.45)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(6)

        chain = MathTex(
            r"= \tfrac{3}{6} = \tfrac{4}{8}",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(chain, direction=RIGHT, anchor=eq, buff=0.4)
        self.play(Write(chain), run_time=NORMAL)
        self.wait(22)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Division creates fractions
    # ------------------------------------------------------------------
    def scene7_division_payoff(self):
        """3 bars, 4 friends: each gets 3/4. Division = fraction."""
        self.add_subcaption(
            "Now the payoff, and a promise kept. Three chocolate "
            "bars, four hungry friends, and every bar must be shared "
            "fairly. Here is the fair cut: slice every bar into four "
            "equal quarters. That gives twelve identical pieces. Deal "
            "them out: each friend receives three quarters. No "
            "scraps, no favorites, no arguments. Now read the recipe "
            "backwards. Three bars divided among four people gave "
            "every person three quarters, so three divided by four is "
            "three quarters. Every fraction is a division problem, "
            "and every division is a fraction: the top number is what "
            "you share, the bottom number is how many sharers there "
            "are. Division built the numbers between the integers.",
            duration=49,
        )
        self.ly.section_divider(6, "Sharing Fair")
        title = self.ly.title("Three Bars, Four Friends")

        bars = VGroup(
            self._bar(4, 0, width=5.0),
            self._bar(4, 0, width=5.0),
            self._bar(4, 0, width=5.0),
        )
        stacked, _ = self.ly.stack_down(
            list(bars), start_from=title, spacing=0.4,
        )
        self.play(FadeIn(stacked, lag_ratio=0.25), run_time=NORMAL)
        self.wait(6)

        # Deal: shade 3 of the 4 pieces in each bar
        deals = VGroup()
        for bar in stacked:
            for i in range(3):
                deals.add(
                    Rectangle(width=bar[0][i].width, height=0.6,
                              stroke_width=0, fill_color=ACCENT,
                              fill_opacity=0.85)
                    .move_to(bar[0][i])
                )
        self.play(FadeIn(deals, lag_ratio=0.12), run_time=SLOW)

        eq = MathTex(
            r"3 \div 4 = \tfrac{3}{4}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(eq, direction=DOWN, anchor=stacked, buff=0.4)
        self.play(Write(eq), run_time=NORMAL)
        self.wait(8)
        self.ly.clear()

        # General bridge
        title2 = self.ly.title("The Bridge")
        fb = self.ly.formula_box(
            MathTex(
                r"\dfrac{a}{b} = a \div b",
                font_size=HEADING_SIZE, color=ACCENT,
            )
        )
        self.ly.center_in_content(fb)
        self.play(Write(fb[0]), run_time=NORMAL)
        self.play(Create(fb[1]), run_time=FAST)

        note = Text(
            "Top: what you share.  Bottom: how many sharers.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=fb, buff=0.45)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(21)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Improper and mixed numbers
    # ------------------------------------------------------------------
    def scene8_past_one_whole(self):
        """5/4 as one whole plus one quarter."""
        self.add_subcaption(
            "Five quarters sounds strange until you see it. One full "
            "bar: four quarters. The fifth quarter sits beside it. So "
            "five quarters is one whole and one quarter more, which "
            "everyday speech calls one and a quarter. Both names are "
            "correct. As a fraction, five over four, it lives between "
            "one and two on the line; mathematicians call it "
            "improper, though it behaves perfectly well. In mixed "
            "form, one plus one quarter, it tells you at a glance how "
            "many wholes you have and what is left over. Musicians "
            "meet this constantly: five quarter notes fill one bar of "
            "music and one beat more. Whether you say five quarters "
            "or one and a quarter, the number line does not care: "
            "same point, same number, two costumes.",
            duration=51,
        )
        self.ly.section_divider(7, "Two Costumes")
        title = self.ly.title("Five Quarters")

        whole = self._bar(4, 4, width=4.6)
        extra_cell = Rectangle(
            width=4.6 / 4, height=0.6, color=PRIMARY, stroke_width=2.5,
        )
        row = VGroup(whole, extra_cell).arrange(RIGHT, buff=0.25)
        self.ly.center_in_content(row)
        self.play(FadeIn(whole, shift=LEFT * 0.15), run_time=NORMAL)
        self.play(FadeIn(extra_cell, scale=0.6), run_time=NORMAL)
        self.wait(6)

        improper = VGroup(
            MathTex(r"\tfrac{5}{4}", font_size=HEADING_SIZE, color=ACCENT),
            Text("improper fraction", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.2)
        mixed = VGroup(
            MathTex(r"= 1 + \tfrac{1}{4}", font_size=HEADING_SIZE, color=SECONDARY),
            Text("mixed number", font_size=LABEL_SIZE, color=DIM, font=SANS),
        ).arrange(DOWN, buff=0.2)
        pair = VGroup(improper, mixed).arrange(RIGHT, buff=1.2)
        self.ly.safe_place(pair, direction=DOWN, anchor=row, buff=0.5)

        self.play(Write(improper[0]), run_time=NORMAL)
        self.play(FadeIn(improper[1], shift=LEFT * 0.15), run_time=FAST)
        self.play(Write(mixed[0]), run_time=NORMAL)
        self.play(FadeIn(mixed[1], shift=LEFT * 0.15), run_time=FAST)
        self.wait(34)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: Fractions in the wild
    # ------------------------------------------------------------------
    def scene9_in_the_wild(self):
        """Clock, fuel gauge, recipes, sales, sports."""
        self.add_subcaption(
            "Once you look, fractions are everywhere. Half past two: "
            "the minute hand has covered one half of its circle. A "
            "quarter tank of fuel: the needle rests at one quarter. A "
            "recipe asks for half a cup of sugar; a carpenter cuts a "
            "board into thirds; a store screams seventy five percent "
            "off, which is three quarters of the price gone. Sport "
            "adds its own dialect: quarter finals whittle sixteen "
            "teams down to four, and halftime splits the match in "
            "two. Fractions are the everyday arithmetic of sharing, "
            "measuring, and waiting. You have been using them for "
            "years. Now you know exactly what they are.",
            duration=42,
        )
        self.ly.section_divider(8, "In the Wild")
        title = self.ly.title("You Already Speak Fractions")
        rows = [
            Text("Half past two -- minute hand covers half its circle",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Quarter tank of fuel -- needle rests at one quarter",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Half a cup of sugar, a board cut into thirds",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("75% off = three quarters of the price gone",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(rows, start_from=title)
        self.wait(31)
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary + outro
    # ------------------------------------------------------------------
    def scene10_summary(self):
        """Recap fractions; tease decimals."""
        self.add_subcaption(
            "Let us recap. A fraction names equal parts of one whole: "
            "the denominator, down below, says how many equal parts "
            "the whole was cut into, and the numerator counts how "
            "many we hold. Fractions are numbers too: cut the gap "
            "between zero and one, and every fraction takes its place "
            "on the number line. Equivalent fractions are the same "
            "point under finer slicing: multiply or divide top and "
            "bottom by the same number, and the value never moves. "
            "Division and fractions are the same operation in "
            "different clothes: three divided by four is three "
            "quarters. And past one whole, improper fractions and "
            "mixed numbers keep counting. Next time, we give these "
            "numbers a brand new costume: the decimal point, and the "
            "astonishing idea that the line can be cut into ten equal "
            "parts, forever. See you then.",
            duration=57,
        )
        self.ly.section_divider(9, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Denominator (down) = equal parts in the whole; numerator counts yours",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Fractions are numbers: they fill the line between the integers",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Same point, finer slicing: 1/2 = 2/4 = 3/6",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Division creates fractions: 3 ÷ 4 = 3/4",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Past one whole: 5/4 = 1 + 1/4",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(33)
        self.ly.clear()
        play_outro(self, next_video="Decimals", next_playlist="Numbers & Arithmetic")
