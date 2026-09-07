"""
Video 273: Decimals -- Numbers & Arithmetic (L1 Foundations, Video 8/14)

The decimal point: where it lives, and why the places to its right are
place value marching past the ones place. Tenths/hundredths/thousandths,
decimals as fractions with power-of-ten denominators (0.7 = 7/10),
comparing decimals place by place (the 0.5 vs 0.45 trap), money as the
decimal system's native habitat, lining up the points to add, x10 as one
step up the chart, and a repeating-decimal cliffhanger (1/3 = 0.333...).
Connects back to Video 272 (Fractions -- "the line cut into ten equal
parts, forever") and forward to Video 274 (Exponents -- the powers of
ten behind the place-value columns).

Based on competitive analysis (improvements.md, Sep 2026): Math Antics
owns decimal procedure (4.7M + 6.5M views); we differentiate with the
serial number-line story (272 -> 273), the decimal-is-a-fraction
identity as the SPINE (competitors bury it in fine print), and a
repeating-decimal teaser competitors skip.

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


class Video273_Decimals(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_place_value()
        self.scene3_ten_cuts()
        self.scene4_fraction_identity()
        self.scene5_comparing()
        self.scene6_money()
        self.scene7_addition()
        self.scene8_scale_by_ten()
        self.scene9_repeating()
        self.scene10_summary()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _bar(self, parts, shaded, width=8.0, height=0.55,
             line_color=PRIMARY, fill_color=ACCENT):
        """A unit bar cut into `parts` equal cells, first `shaded` filled.

        Returns VGroup(cells, shades) -- cells carry the outline,
        shades overlay the filled portion.
        """
        w = width / parts
        cells = VGroup(*[
            Rectangle(width=w, height=height, color=line_color,
                      stroke_width=2.5 if parts <= 12 else 1.2)
            for _ in range(parts)
        ]).arrange(RIGHT, buff=0)
        shades = VGroup(*[
            Rectangle(width=w, height=height, stroke_width=0,
                      fill_color=fill_color, fill_opacity=0.85)
            .move_to(cells[i])
            for i in range(shaded)
        ])
        return VGroup(cells, shades)

    # ------------------------------------------------------------------
    # Scene 1: Hook - the dot is everywhere
    # ------------------------------------------------------------------
    def scene1_hook(self):
        """Hook: the world speaks in decimals; the point stops being mysterious."""
        self.add_subcaption(
            "Last time, we cut one whole into quarters and filled the gap "
            "between the integers. But the line between zero and one hides "
            "a deeper pattern. Look at any price tag: three dollars and "
            "fifty cents. Any thermometer: thirty-seven point five "
            "degrees. Any race time: nine point five eight seconds. The "
            "world speaks in tenths and hundredths, in numbers written "
            "with a single mysterious dot. That dot is the decimal point, "
            "and today it stops being mysterious. We will discover where "
            "it lives, why the places to its right continue the place "
            "value chart you already trust, and how every decimal is "
            "secretly a fraction in a brand new costume. The number line "
            "is about to get crowded again.",
            duration=44.4,
        )
        play_intro(self, "Decimals", "Numbers & Arithmetic")

        title = self.ly.title("The Mysterious Dot")

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
        self.play(Create(gap), run_time=NORMAL)

        dot = MathTex(r"0.\,?", font_size=TITLE_SIZE, color=ACCENT)
        self.ly.safe_place(dot, direction=UP, anchor=gap, buff=0.35)
        self.play(Write(dot), run_time=NORMAL)
        self.wait(6)

        prompt = Text(
            "tenths and hundredths: the world's favorite numbers",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(prompt, direction=DOWN, anchor=line, buff=0.6)
        self.play(FadeIn(prompt, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(28.1)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 2: Place value marches past the ones place
    # ------------------------------------------------------------------
    def scene2_place_value(self):
        """The chart grows a mirror: tenths, hundredths, thousandths."""
        self.add_subcaption(
            "Start with a number you already know: three hundred "
            "sixty-five. Three hundreds, six tens, five ones. Place value "
            "says each step to the left multiplies by ten, and each step "
            "to the right divides by ten. So here is the question nobody "
            "thinks to ask: why should dividing stop at the ones place? "
            "It should not. Keep marching right, past the ones, and place "
            "value keeps its promise. The next columns hold tenths, then "
            "hundredths, then thousandths, and so on forever. A dot "
            "called the decimal point marks the border: digits to its "
            "left count whole things, digits to its right count parts of "
            "things. Three point six five: three wholes, six tenths, and "
            "five hundredths. Same chart, same rule, new territory.",
            duration=48.4,
        )
        self.ly.section_divider(1, "Past the Ones Place")
        title = self.ly.title("Same Chart, New Territory")

        def _col(head, digit, head_color, digit_color):
            h = Text(head, font_size=LABEL_SIZE, color=head_color, font=SANS)
            d = Text(digit, font_size=HEADING_SIZE, color=digit_color,
                     font=MONO, weight=BOLD)
            return VGroup(h, d).arrange(DOWN, buff=0.3)

        int_cols = VGroup(
            _col("hundreds", "3", DIM, WHITE),
            _col("tens", "6", DIM, WHITE),
            _col("ones", "5", DIM, WHITE),
        ).arrange(RIGHT, buff=0.7)

        point = Text(".", font_size=HEADING_SIZE, color=ACCENT,
                     font=MONO, weight=BOLD)

        dec_cols = VGroup(
            _col("tenths", "6", PRIMARY, ACCENT),
            _col("hundredths", "5", PRIMARY, ACCENT),
        ).arrange(RIGHT, buff=0.7)

        chart = VGroup(int_cols, point, dec_cols).arrange(RIGHT, buff=0.45)
        self.ly.center_in_content(chart)
        self.play(FadeIn(int_cols, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)

        self.play(FadeIn(point, scale=0.5), run_time=NORMAL)
        self.play(FadeIn(dec_cols, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(5)

        note = Text(
            "left of the point: wholes.  right of the point: parts.",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=chart, buff=0.55)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(32.6)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 3: Ten equal cuts - the promise from Video 272, kept
    # ------------------------------------------------------------------
    def scene3_ten_cuts(self):
        """Cut [0,1] into ten; park on 0.7 = seven tenths."""
        self.add_subcaption(
            "Now the promise from last time, kept. Here is the gap "
            "between zero and one, cut not into quarters but into ten "
            "equal segments. Each cut point is a number. The first is "
            "one tenth, written zero point one. The second, two tenths. "
            "Count upward: three tenths, four tenths, on to nine tenths, "
            "and ten tenths lands exactly on one. Ten tenths is one "
            "whole, just as four quarters was. Now park on seven tenths: "
            "zero point seven. In everyday speech you will hear zero "
            "point seven, and that is fine. But seven tenths is the "
            "honest name, because it says exactly what the number is: "
            "seven of the ten equal parts of one whole.",
            duration=43.8,
        )
        self.ly.section_divider(2, "Ten Equal Cuts")
        title = self.ly.title("Counting by Tenths")

        line = NumberLine(
            x_range=[0, 1.02, 0.1], length=12,
            color=PRIMARY, include_numbers=False,
            include_ticks=True, tick_size=0.1,
        )
        self.ly.center_in_content(line)
        self.play(Create(line), run_time=SLOW)

        zero = MathTex("0", font_size=LABEL_SIZE, color=WHITE)
        one = MathTex("1", font_size=LABEL_SIZE, color=WHITE)
        zero.next_to(line.n2p(0), DOWN, buff=0.25)
        one.next_to(line.n2p(1), DOWN, buff=0.25)
        ends = VGroup(zero, one)
        self.play(FadeIn(ends), run_time=FAST)

        labels = VGroup(*[
            MathTex(
                r"\tfrac{" + str(k) + r"}{10}",
                font_size=LABEL_SIZE, color=PRIMARY,
            ).next_to(line.n2p(k / 10), UP, buff=0.22)
            for k in range(1, 10)
        ])
        self.play(FadeIn(labels, lag_ratio=0.15), run_time=SLOW)
        self.wait(6)

        seven = MathTex(r"0.7", font_size=HEADING_SIZE, color=ACCENT)
        seven.next_to(line.n2p(0.7), DOWN, buff=0.5)
        marker = Dot(line.n2p(0.7), color=ACCENT, radius=0.09)
        self.play(FadeIn(marker, scale=0.5), Write(seven), run_time=NORMAL)
        self.wait(30.6)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 4: Every decimal is a fraction in a base-ten costume
    # ------------------------------------------------------------------
    def scene4_fraction_identity(self):
        """0.7 = 7/10 on the bar; 0.25 = 25/100; 0.62 = 62/100."""
        self.add_subcaption(
            "Which reveals the secret every decimal carries. Zero point "
            "seven is just seven tenths wearing a dot. Zero point two "
            "five is twenty-five hundredths: cut each tenth into ten "
            "finer parts, one hundred in the whole, and take twenty-five "
            "of them. Zero point six two? Sixty-two hundredths: sixty-two "
            "parts out of one hundred. Every decimal is a fraction whose "
            "denominator is ten, one hundred, one thousand: a power of "
            "ten. Nothing new was invented. The dot is a machine for "
            "writing certain fractions quickly, without stacking a "
            "numerator over a denominator. Fractions never left. "
            "Decimals are their base-ten costume, and the number line "
            "settles every dispute: zero point seven and seven tenths "
            "mark one and the same point.",
            duration=49.2,
        )
        self.ly.section_divider(3, "Two Names, One Number")
        title = self.ly.title("A Fraction in Costume")

        bar = self._bar(10, 7, width=8.0)
        left = MathTex(r"0.7", font_size=HEADING_SIZE, color=ACCENT)
        right = MathTex(r"\tfrac{7}{10}", font_size=HEADING_SIZE, color=SECONDARY)
        left.next_to(bar, LEFT, buff=0.5)
        right.next_to(bar, RIGHT, buff=0.5)
        row = VGroup(left, bar, right)
        self.ly.center_in_content(row)
        self.play(FadeIn(row, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(6)

        chain = MathTex(
            r"0.25 = \tfrac{25}{100} \qquad 0.62 = \tfrac{62}{100}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        self.ly.safe_place(chain, direction=DOWN, anchor=row, buff=0.6)
        self.play(Write(chain), run_time=NORMAL)
        self.wait(5)

        note = Text(
            "under every decimal: a power of ten",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=chain, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(33.7)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 5: The longer-is-bigger trap
    # ------------------------------------------------------------------
    def scene5_comparing(self):
        """0.5 vs 0.45: length lies, place value decides."""
        self.add_subcaption(
            "Here is where decimals trick almost everyone. Which is "
            "bigger: zero point five, or zero point four five? Your eyes "
            "say zero point four five, because forty-five beats five. "
            "But watch the con. Zero point five is five tenths, which is "
            "fifty hundredths. Fifty hundredths against forty-five "
            "hundredths: zero point five wins. Length is a lie. Place "
            "value is the truth. To compare decimals honestly, ignore "
            "how long they look and read from the left: compare tenths "
            "first. Five tenths beats four tenths, and the contest is "
            "already over. The zero in zero point five is not "
            "decoration. Written as zero point five zero, it is the "
            "placeholder that says: zero hundredths, nothing extra.",
            duration=47.7,
        )
        self.ly.section_divider(4, "The Length Trap")
        title = self.ly.title("Which Is Bigger?")

        bar_a = self._bar(10, 5, width=8.5, fill_color=ACCENT)
        la = MathTex(r"0.5", font_size=LABEL_SIZE, color=ACCENT)
        la.next_to(bar_a, LEFT, buff=0.4)
        row_a = VGroup(la, bar_a)

        bar_b = self._bar(100, 45, width=8.5, fill_color=SECONDARY)
        lb = MathTex(r"0.45", font_size=LABEL_SIZE, color=SECONDARY)
        lb.next_to(bar_b, LEFT, buff=0.4)
        row_b = VGroup(lb, bar_b)

        stacked, _overflow = self.ly.stack_down(
            [row_a, row_b], start_from=title, spacing=0.5,
        )
        self.play(FadeIn(stacked[0], shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(4)
        self.play(FadeIn(stacked[1], shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(6)

        verdict = MathTex(
            r"\tfrac{50}{100} > \tfrac{45}{100}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(verdict, direction=DOWN, anchor=stacked, buff=0.5)
        self.play(Write(verdict), run_time=NORMAL)
        self.wait(5)

        rule = Text(
            "read from the left: tenths decide it first",
            font_size=BODY_SIZE, color=WHITE, font=SANS,
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=verdict, buff=0.4)
        self.play(FadeIn(rule, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(26.7)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 6: Money - decimals you can jingle in your pocket
    # ------------------------------------------------------------------
    def scene6_money(self):
        """$1.23: dollar, dimes are tenths, pennies are hundredths."""
        self.add_subcaption(
            "You have been using decimal place value since childhood, "
            "every time you touch money. One dollar twenty-three. The "
            "one counts whole dollars. The two sits in the tenths place, "
            "and indeed a dime is one tenth of a dollar. The three sits "
            "in the hundredths place, and a penny is one hundredth of a "
            "dollar. That is the entire secret of the coins: dimes and "
            "pennies are decimal place values you can jingle in your "
            "pocket. One point two three dollars is one whole, two "
            "tenths, and three hundredths. Price tags, gas pumps, bank "
            "statements: money is the decimal system's native habitat, "
            "rehearsing you daily for the mathematics.",
            duration=40.0,
        )
        self.ly.section_divider(5, "In Your Pocket")
        title = self.ly.title("One Dollar Twenty-Three")

        dollar = VGroup(
            Rectangle(width=1.5, height=0.85, color=SECONDARY, stroke_width=2.5),
            Text("$1", font_size=LABEL_SIZE, color=SECONDARY, font=MONO),
        )
        dollar[1].move_to(dollar[0])
        dime = VGroup(
            Circle(radius=0.42, color=PRIMARY, stroke_width=2.5),
            Text("10\u00a2", font_size=LABEL_SIZE, color=PRIMARY, font=MONO),
        )
        dime[1].move_to(dime[0])
        penny = VGroup(
            Circle(radius=0.34, color=RED, stroke_width=2.5),
            Text("1\u00a2", font_size=LABEL_SIZE, color=RED, font=MONO),
        )
        penny[1].move_to(penny[0])

        coins = VGroup(
            dollar, dime.copy(), dime.copy(),
            penny.copy(), penny.copy(), penny.copy(),
        ).arrange(RIGHT, buff=0.45)
        self.ly.center_in_content(coins)
        self.play(FadeIn(coins, lag_ratio=0.15), run_time=SLOW)
        self.wait(6)

        breakdown = MathTex(
            r"\$1.23 = 1 + \tfrac{2}{10} + \tfrac{3}{100}",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(breakdown, direction=DOWN, anchor=coins, buff=0.55)
        self.play(Write(breakdown), run_time=NORMAL)
        self.wait(5)

        note = Text(
            "dimes are tenths.  pennies are hundredths.",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=breakdown, buff=0.4)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(22.9)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 7: Addition - line up the points
    # ------------------------------------------------------------------
    def scene7_addition(self):
        """0.7 + 0.25: rename to hundredths, then the columns line up."""
        self.add_subcaption(
            "Adding decimals has one famous rule, and now you can see "
            "why it is true. Add zero point seven plus zero point two "
            "five. The trap: seven plus twenty-five looks tempting, and "
            "it is nonsense, because seven tenths and twenty-five "
            "hundredths count different-sized parts. So rename. Seven "
            "tenths is seventy hundredths. Now the parts match: seventy "
            "hundredths plus twenty-five hundredths is ninety-five "
            "hundredths. Zero point nine five. In column form this is "
            "the rule you have heard: line up the decimal points. When "
            "the points align, every column holds the same-sized part, "
            "ones over ones, tenths over tenths, hundredths over "
            "hundredths, and ordinary addition takes over. Line up the "
            "points, not the digits.",
            duration=47.3,
        )
        self.ly.section_divider(6, "Line Up the Points")
        title = self.ly.title("Adding Tenths to Hundredths")

        r1 = MathTex(r"0.70", font_size=HEADING_SIZE, color=WHITE)
        r2 = MathTex(r"+\;0.25", font_size=HEADING_SIZE, color=WHITE)
        bar = Line(LEFT * 0.9, RIGHT * 0.9, color=DIM, stroke_width=2)
        r3 = MathTex(r"0.95", font_size=HEADING_SIZE, color=ACCENT)
        col = VGroup(r1, r2, bar, r3).arrange(DOWN, buff=0.28).align_to(r1, LEFT)
        self.ly.center_in_content(col)
        self.play(Write(r1), run_time=NORMAL)
        self.play(Write(r2), run_time=NORMAL)
        self.wait(4)

        self.play(Create(bar), run_time=FAST)
        self.play(Write(r3), run_time=NORMAL)
        self.wait(4)

        # one accent dot per row at the point's x position
        marks = VGroup(*[
            Dot([col.get_center()[0] + 0.62, m.get_center()[1], 0],
                color=ACCENT, radius=0.05)
            for m in (r1, r2, r3)
        ])
        self.play(FadeIn(marks, lag_ratio=0.2), run_time=NORMAL)
        self.wait(4)

        rule = Text(
            "points aligned: every column holds the same-sized part",
            font_size=BODY_SIZE, color=SECONDARY, font=SANS,
        )
        self.ly.safe_place(rule, direction=DOWN, anchor=col, buff=0.5)
        self.play(FadeIn(rule, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(27.5)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 8: Multiplying and dividing by ten
    # ------------------------------------------------------------------
    def scene8_scale_by_ten(self):
        """x10: every digit steps one place up the chart."""
        self.add_subcaption(
            "Multiplying by ten has a beautiful meaning here: it is one "
            "step up the chart. Take two point seven five and multiply "
            "by ten. Every digit climbs one place. The two ones become "
            "two tens, the seven tenths become seven ones, the five "
            "hundredths become five tenths: twenty-seven point five. "
            "Divide by ten, and every digit steps back down: two point "
            "seven five becomes zero point two seven five. Each step of "
            "ten slides the point one place, and you can take as many "
            "steps as you like. The chart runs forever in both "
            "directions, and ten never gets tired.",
            duration=37.8,
        )
        self.ly.section_divider(7, "Steps of Ten")
        title = self.ly.title("The Sliding Point")

        eq1 = self.ly.formula_box(
            MathTex(r"2.75 \times 10 = 27.5",
                    font_size=HEADING_SIZE, color=ACCENT)
        )
        self.ly.center_in_content(eq1)
        self.play(Write(eq1[0]), run_time=NORMAL)
        self.play(Create(eq1[1]), run_time=FAST)
        self.wait(5)

        eq2 = self.ly.formula_box(
            MathTex(r"2.75 \div 10 = 0.275",
                    font_size=HEADING_SIZE, color=SECONDARY)
        )
        self.ly.safe_place(eq2, direction=DOWN, anchor=eq1, buff=0.6)
        self.play(Write(eq2[0]), run_time=NORMAL)
        self.play(Create(eq2[1]), run_time=FAST)
        self.wait(5)

        note = Text(
            "one step of ten: the point slides one place",
            font_size=BODY_SIZE, color=DIM, font=SANS,
        )
        self.ly.safe_place(note, direction=DOWN, anchor=eq2, buff=0.45)
        self.play(FadeIn(note, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(21.1)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 9: The number that will not sit still
    # ------------------------------------------------------------------
    def scene9_repeating(self):
        """1/3 = 0.333...: the remainder returns forever. Teaser."""
        self.add_subcaption(
            "One more gift, and a mystery to close. Divide one by "
            "three. One whole, cut into three equal parts: each is one "
            "third. But in decimal form, watch the division. Ten tenths "
            "divided by three gives three tenths, with one tenth left "
            "over. Divide the leftover: three hundredths, and one "
            "hundredth left over. Again: three thousandths, and the "
            "same remainder returns. That remainder will keep coming "
            "back forever, so the threes never stop: zero point three, "
            "three, three, on and on. We write it with a bar: zero "
            "point three repeating. One third and zero point three "
            "repeating are the same number, seen from the fraction "
            "world and the decimal world. Why do some fractions repeat "
            "and others stop? A story for another day.",
            duration=49.4,
        )
        self.ly.section_divider(8, "The Won't-Sit-Still Number")
        title = self.ly.title("One Third, in Decimals")

        digits = MathTex(
            r"1 \div 3 = 0.3333\ldots",
            font_size=TITLE_SIZE, color=ACCENT,
        )
        self.ly.center_in_content(digits)
        self.play(Write(digits), run_time=SLOW)
        self.wait(6)

        overline = MathTex(
            r"\tfrac{1}{3} = 0.\overline{3}",
            font_size=HEADING_SIZE, color=SECONDARY,
        )
        self.ly.safe_place(overline, direction=DOWN, anchor=digits, buff=0.55)
        self.play(Write(overline), run_time=NORMAL)
        self.wait(4)

        cousin = MathTex(
            r"\tfrac{1}{7} = 0.\overline{142857}",
            font_size=BODY_SIZE, color=DIM,
        )
        self.ly.safe_place(cousin, direction=DOWN, anchor=overline, buff=0.4)
        self.play(Write(cousin), run_time=NORMAL)
        self.wait(5)

        tease = Text(
            "some decimals repeat forever. some stop. why?",
            font_size=BODY_SIZE, color=RED, font=SANS,
        )
        self.ly.safe_place(tease, direction=DOWN, anchor=cousin, buff=0.4)
        self.play(FadeIn(tease, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(27.9)  # pacing: extends previous caption slot
        self.ly.clear()

    # ------------------------------------------------------------------
    # Scene 10: Summary + outro
    # ------------------------------------------------------------------
    def scene10_summary(self):
        """Recap decimals; tease exponents (the powers of ten)."""
        self.add_subcaption(
            "Let us recap. The decimal point marks the border between "
            "wholes and parts: to its right, place value continues as "
            "tenths, hundredths, thousandths, and beyond. Every decimal "
            "is a fraction with a power of ten underneath: zero point "
            "seven is seven tenths. To compare decimals, ignore length "
            "and compare place by place from the left, so zero point "
            "five beats zero point four five. To add, line up the "
            "decimal points so every column holds equal parts. "
            "Multiplying by ten steps every digit one place up the "
            "chart. And some decimals, like one third, repeat forever. "
            "Next time: exponents, the shorthand hiding inside the ten, "
            "hundred, and one thousand columns we marched across "
            "today. See you then.",
            duration=48.8,
        )
        self.ly.section_divider(9, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("The point splits wholes from parts: tenths, hundredths, thousandths",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Every decimal is a fraction: 0.7 = 7/10",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Compare place by place: 0.5 > 0.45",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Line up the points to add: 0.70 + 0.25 = 0.95",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("x10 slides the point; 1/3 = 0.333... forever",
                 font_size=BODY_SIZE, color=RED, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(36.9)
        self.ly.clear()
        play_outro(self, next_video="Exponents", next_playlist="Numbers & Arithmetic")
