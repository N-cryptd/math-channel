"""
Video 266: What is Mathematics? -- Numbers & Arithmetic (L1 Foundations, Video 1/12)

Introduction to mathematics as a discipline: patterns, abstraction,
proof, and applications. No prerequisites -- the very first video
in the foundations track.

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


class Video266_WhatIsMathematics(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)
        self.scene1_hook()
        self.scene2_what_is_math()
        self.scene3_patterns_everywhere()
        self.scene4_abstraction()
        self.scene5_the_language_of_math()
        self.scene6_proof()
        self.scene7_applications()
        self.scene8_playlist_preview()
        self.scene9_summary()

    def scene1_hook(self):
        """Hook: a visual pattern that raises the question."""
        self.add_subcaption(
            "Look at these numbers. One, one, two, three, five, eight. "
            "Each number is the sum of the two before it. This is "
            "the Fibonacci sequence. But this is just one tiny corner of mathematics. "
            "What really is mathematics?",
            duration=20,
        )
        play_intro(self, "What is Mathematics?", "Numbers & Arithmetic")

        title = self.ly.title("A Pattern You Know")
        fib_nums = MathTex(
            r"1,\; 1,\; 2,\; 3,\; 5,\; 8,\; 13,\; 21,\; \ldots",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(fib_nums, DOWN, anchor=title, buff=0.5)
        self.play(Write(fib_nums), run_time=SLOW)
        self.wait(FAST)
        items = [
            Text("Each number = sum of the two before it",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Appears in sunflowers, pinecones, galaxies",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("But this is just one tiny corner of math",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=fib_nums)
        self.wait(5)
        self.ly.clear()

    def scene2_what_is_math(self):
        """Define mathematics broadly: patterns, structures, relationships."""
        self.add_subcaption(
            "Most people think mathematics is about numbers and equations. "
            "But mathematics is really the study of patterns, structures, "
            "and relationships. A geometer studies the patterns of shape. "
            "A number theorist studies patterns in whole numbers. "
            "An algebraist studies patterns of operations and symmetry. "
            "Every branch is about finding patterns and describing them precisely.",
            duration=30,
        )
        self.ly.section_divider(1, "What Is Mathematics?")
        title = self.ly.title("Not Just Numbers")
        items = [
            Text("Mathematics = the study of patterns,",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("structures, and relationships",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Geometry: patterns of shape and space",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Number theory: patterns in whole numbers",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Algebra: patterns of operations and symmetry",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(16)
        self.ly.clear()

    def scene3_patterns_everywhere(self):
        """Show patterns in nature and everyday life."""
        self.add_subcaption(
            "Patterns are everywhere once you know how to look. "
            "Bees build hexagonal honeycombs because hexagons tile a plane "
            "with minimal perimeter. Snowflakes have six-fold symmetry. "
            "In music, a perfect fifth has frequency ratio three to two, "
            "and an octave is two to one. Mathematics describes why.",
            duration=28,
        )
        self.ly.section_divider(2, "Patterns Everywhere")
        title = self.ly.title("Nature, Music, and More")
        items = [
            Text("Honeycombs: hexagons minimize perimeter",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Snowflakes: 6-fold symmetry from molecular bonds",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(6)
        self.ly.clear()

        title2 = self.ly.title("Math in Music")
        items2 = [
            Text("Perfect fifth: frequency ratio 3 : 2",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Octave: frequency ratio 2 : 1",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Math describes WHY, not just WHAT",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(8)
        self.ly.clear()

    def scene4_abstraction(self):
        """The power of abstraction: stripping away details to find universals."""
        self.add_subcaption(
            "The real power of mathematics is abstraction. "
            "Three apples, three cars, three ideas. The number three "
            "is the same in every case. Mathematics strips away the details "
            "to study the number itself. From counting we get numbers. "
            "From numbers we get arithmetic. From arithmetic we get algebra. "
            "Each level lets us solve harder problems.",
            duration=30,
        )
        self.ly.section_divider(3, "Abstraction")
        title = self.ly.title("Stripping Away Details")
        items = [
            Text("3 apples, 3 cars, 3 ideas",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The number 3 is the same in every case",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Abstraction: find what is common across situations",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(8)
        self.ly.clear()

        title2 = self.ly.title("A Chain of Abstraction")
        items2 = [
            Text("Counting  ->  Numbers  ->  Arithmetic  ->  Algebra",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Each level unlocks harder problems",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Each level reveals deeper connections",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(8)
        self.ly.clear()

    def scene5_the_language_of_math(self):
        """Mathematical notation as a precise language."""
        self.add_subcaption(
            "Mathematics has its own language of symbols. "
            "Ordinary language is ambiguous, but math notation eliminates "
            "ambiguity. When we write the sum from n equals one to one "
            "hundred of n, every mathematician understands exactly what we mean. "
            "Notation lets us express complex ideas compactly.",
            duration=26,
        )
        self.ly.section_divider(4, "The Language of Mathematics")
        title = self.ly.title("Why Symbols?")
        items = [
            Text("Ordinary language is ambiguous",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Math notation eliminates ambiguity",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Complex ideas become compact",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(8)
        self.ly.clear()

        title2 = self.ly.title("Example: Summation")
        sigma = MathTex(
            r"\sum_{n=1}^{100} n = \frac{100 \cdot 101}{2} = 5050",
            font_size=HEADING_SIZE, color=ACCENT,
        )
        self.ly.safe_place(sigma, DOWN, anchor=title2, buff=0.5)
        self.play(Write(sigma), run_time=SLOW)
        self.wait(FAST)
        item = Text(
            "One line says what would take a full English sentence",
            font_size=BODY_SIZE, color=PRIMARY, font=SANS,
        )
        self.ly.safe_place(item, DOWN, anchor=sigma, buff=0.4)
        self.play(FadeIn(item, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(6)
        self.ly.clear()

    def scene6_proof(self):
        """Proof as what makes math different from other disciplines."""
        self.add_subcaption(
            "What makes mathematics unique is proof. "
            "In science, theories are never proven, only not yet disproven. "
            "But in mathematics, once something is proved, it is true forever. "
            "Euclid proved there are infinitely many primes two thousand "
            "years ago, and that proof is still valid today. "
            "Here is a simple example. "
            "Claim: the sum of any two odd numbers is even. "
            "An odd number has the form two k plus one. "
            "So the sum of two m plus one and two n plus one equals "
            "two times m plus n plus one, which is clearly even.",
            duration=45,
        )
        self.ly.section_divider(5, "Proof")
        title = self.ly.title("What Makes Math Unique")
        items = [
            Text("Science: evidence, theories, always provisional",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Mathematics: proof, certainty, forever true",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(10)
        self.ly.clear()

        title2 = self.ly.title("Example Proof")
        claim = Text(
            "Claim: odd + odd = even",
            font_size=BODY_SIZE, color=ACCENT, font=SANS,
        )
        self.ly.safe_place(claim, DOWN, anchor=title2, buff=0.5)
        self.play(FadeIn(claim, shift=LEFT * 0.15), run_time=NORMAL)
        self.wait(FAST)
        items2 = [
            Text("Odd number: 2k + 1 for some integer k",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("(2m+1) + (2n+1) = 2(m+n+1) = even",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("QED  -- this will never be overturned",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=claim)
        self.wait(18)
        self.ly.clear()

    def scene7_applications(self):
        """Where math shows up in the real world."""
        self.add_subcaption(
            "Mathematics is not just abstract. It powers the modern world. "
            "Computers run on binary arithmetic and Boolean logic. "
            "Encryption relies on prime numbers and modular arithmetic. "
            "GPS uses the geometry of curved spacetime. "
            "Machine learning is built on linear algebra and calculus. "
            "The physicist Eugene Wigner called this the unreasonable "
            "effectiveness of mathematics.",
            duration=35,
        )
        self.ly.section_divider(6, "Applications")
        title = self.ly.title("Math Powers the Modern World")
        items = [
            Text("Computers: binary arithmetic, Boolean logic",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Encryption: prime numbers, modular arithmetic",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("GPS: geometry of curved spacetime",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(14)
        self.ly.clear()

        title2 = self.ly.title("The Unreasonable Effectiveness")
        items2 = [
            Text("Pure thought -> describes physical reality",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Art, music, AI, engineering all need math",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("(Eugene Wigner, 1960)",
                 font_size=BODY_SIZE, color=DIM, font=SANS),
        ]
        self.ly.progressive_reveal(items2, start_from=title2)
        self.wait(8)
        self.ly.clear()

    def scene8_playlist_preview(self):
        """Preview what this playlist covers."""
        self.add_subcaption(
            "In this playlist, Numbers and Arithmetic, we build your "
            "mathematical foundation from the ground up. We start with "
            "natural numbers and counting, then negative numbers. "
            "We learn fractions, decimals, and rational numbers. "
            "We cover the four operations, divisibility, and primes. "
            "By the end, you will have a rigorous understanding of "
            "the number systems all of mathematics is built on.",
            duration=32,
        )
        self.ly.section_divider(7, "This Playlist")
        title = self.ly.title("Numbers & Arithmetic")
        items = [
            Text("Natural numbers and counting",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Negative numbers and integers",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Fractions, decimals, and rationals",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Operations, order, properties",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Divisibility and prime numbers",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(16)
        self.ly.clear()

    def scene9_summary(self):
        """Key takeaways and outro."""
        self.add_subcaption(
            "Let us recap. Mathematics is the study of patterns, structures, "
            "and relationships. Its power comes from abstraction. "
            "It has its own precise language of symbols. "
            "Unlike any other field, math establishes truth through proof. "
            "And it is staggeringly useful. In this playlist, we start "
            "building that foundation from the very beginning: numbers. "
            "See you in the next video.",
            duration=30,
        )
        self.ly.section_divider(8, "Summary")
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Math = study of patterns, structures, relationships",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Abstraction: find universal truths",
                 font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Precise language of symbols",
                 font_size=BODY_SIZE, color=SECONDARY, font=SANS),
            Text("Proof gives certainty that lasts forever",
                 font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Staggeringly useful in the real world",
                 font_size=BODY_SIZE, color=WHITE, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(12)
        self.ly.clear()
        play_outro(self, next_video="Natural Numbers & Counting", next_playlist="Numbers & Arithmetic")
