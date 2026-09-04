r"""
Video 249: Information Theory and Physics
Information Theory playlist, video 9/10.

Covers: thermodynamic entropy, Landauer's principle, Bekenstein bound,
the deep connection between information and physics.

v2: LayoutEngine, progressive_reveal, Source Sans 3, dot grid background.

Render:  manim -ql scripts/graduate/video-249-information-physics.py Video249_InformationPhysics
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


class Video249_InformationPhysics(Scene):
    """Information Theory and Physics."""

    def construct(self):
        self.camera.background_color = BG
        self.ly = LayoutEngine(self)
        self._bg_dots, self._bg_gradient = setup_background(self)

        self.scene1_hook()
        self.scene2_boltzmann()
        self.scene3_shannon_boltzmann()
        self.scene4_landauer()
        self.scene5_bekenstein()
        self.scene6_black_holes()
        self.scene7_summary()

    def scene1_hook(self):
        self.add_subcaption(
            "Information is physical. Erasing a bit of information costs energy. "
            "Black holes have entropy proportional to their surface area. "
            "The universe itself may be fundamentally computational."
            "Information theory connects to the deepest questions in physics.",
            duration=18,
        )
        play_intro(self, "Information Theory and Physics", "Information Theory")

        title = self.ly.title("Information is Physical")
        items = [
            Text("Erasing bits costs energy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Black holes have entropy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("The universe computes", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(4)
        self.ly.clear()

    def scene2_boltzmann(self):
        self.ly.section_divider(1, "Boltzmann Entropy")

        self.add_subcaption(
            "In 1877, Boltzmann defined thermodynamic entropy as S = k "
            "times log W, where W is the number of microstates. "
            "This is essentially Shannon entropy, decades before Shannon. "
            "Boltzmann's formula measures the uncertainty in a physical system.",
            duration=20,
        )
        title = self.ly.title("Boltzmann Entropy")
        boltz_formula = MathTex(r"S = k \log W", font_size=HEADING_SIZE, color=PRIMARY)
        boxed = self.ly.formula_box(boltz_formula, color=PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(boxed), run_time=NORMAL)
        items = [
            Text("W = number of microstates", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Shannon entropy, 70 years earlier", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.wait(17)
        self.ly.clear()

    def scene3_shannon_boltzmann(self):
        self.add_subcaption(
            "Shannon entropy and thermodynamic entropy are the same concept. "
            "Shannon chose the name entropy on John von Neumann's advice. "
            "Von Neumann said nobody knows what entropy really is, "
            "so in a debate you will always win.",
            duration=16,
        )
        title = self.ly.title("Shannon Meets Boltzmann")
        items = [
            Text("Same formula, different contexts", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Shannon: communication", font_size=BODY_SIZE, color=PRIMARY, font=SANS),
            Text("Boltzmann: thermodynamics", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(9)
        self.ly.clear()

    def scene4_landauer(self):
        self.ly.section_divider(2, "Landauer's Principle")

        self.add_subcaption(
            "Landauer's principle says erasing one bit of information "
            "dissipates at least k T ln 2 of energy. "
            "This links information theory directly to thermodynamics. "
            "It means there is a minimum energy cost to computation.",
            duration=16,
        )
        title = self.ly.title("Landauer's Principle")
        items = [
            Text("Erasing 1 bit costs energy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            MathTex(r"E \geq k_B T \ln 2", font_size=HEADING_SIZE, color=PRIMARY),
            Text("Minimum energy cost of computation", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(9)
        self.ly.clear()

    def scene5_bekenstein(self):
        self.ly.section_divider(3, "Bekenstein Bound")

        self.add_subcaption(
            "The Bekenstein bound says the maximum information in a region "
            "of space is proportional to its surface area, not volume. "
            "This is holographic: information lives on the boundary. "
            "It connects information theory to quantum gravity.",
            duration=16,
        )
        title = self.ly.title("Bekenstein Bound")
        items = [
            Text("Max info proportional to surface area", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Holographic principle", font_size=BODY_SIZE, color=ACCENT, font=SANS),
            Text("Connects to quantum gravity", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(9)
        self.ly.clear()

    def scene6_black_holes(self):
        self.ly.section_divider(4, "Black Hole Entropy")

        self.add_subcaption(
            "Black hole entropy, discovered by Bekenstein and Hawking, "
            "equals one quarter of the horizon area in Planck units. "
            "This is pure information: it counts the number of ways "
            "to form the black hole. Physics is information.",
            duration=17,
        )
        title = self.ly.title("Black Hole Entropy")
        bh_formula = MathTex(
            r"S_{BH} = \frac{k_B A}{4 \ell_P^2}",
            font_size=HEADING_SIZE, color=PRIMARY,
        )
        boxed = self.ly.formula_box(bh_formula, color=PRIMARY)
        self.ly.safe_place(boxed, direction=DOWN, anchor=title, buff=0.5)
        self.play(Write(boxed), run_time=NORMAL)
        items = [
            Text("A = horizon area", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Physics is fundamentally about information", font_size=BODY_SIZE, color=ACCENT, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=boxed)
        self.wait(13)
        self.ly.clear()

    def scene7_summary(self):
        self.add_subcaption(
            "Boltzmann entropy and Shannon entropy are the same idea. "
            "Landauer's principle links erasure to energy. "
            "Black hole entropy suggests physics is information. "
            "Next, we summarize the entire Information Theory playlist.",
            duration=17,
        )
        title = self.ly.title("Key Takeaways")
        items = [
            Text("Boltzmann = Shannon (same formula)", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Erasing bits costs energy", font_size=BODY_SIZE, color=WHITE, font=SANS),
            Text("Black holes encode information", font_size=BODY_SIZE, color=SECONDARY, font=SANS),
        ]
        self.ly.progressive_reveal(items, start_from=title)
        self.wait(7)

        play_outro(self, next_video="Information Theory Summary", next_playlist="Information Theory")
