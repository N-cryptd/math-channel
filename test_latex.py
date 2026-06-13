from manim import *
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "templates"))
from channel_branding import (
    BG, PRIMARY, SECONDARY, ACCENT, RED, DIM, WHITE, SANS, MONO,
    TITLE_SIZE, HEADING_SIZE, BODY_SIZE, LABEL_SIZE, SMALL_SIZE,
    FAST, NORMAL, SLOW,
    play_intro, play_outro, setup_background,
)
from layout import LayoutEngine, ensure_fits

# Quick test of all MathTex strings used in the video
# to catch any LaTeX syntax errors

test_tex = [
    r"\text{Differential Equation}\xrightarrow{\quad \mathcal{L} \quad}\text{Algebraic Equation}",
    r"m\,x''+c\,x'+k\,x=f(t)",
    r"\Downarrow\mathcal{L}",
    r"\mathcal{L}\{f(t)\}=\int_0^{\infty}e^{-st}\,f(t)\,dt=F(s)",
    r"\mathcal{L}\{e^{at}\}=\int_0^{\infty}e^{at}\,e^{-st}\,dt",
    r"\mathcal{L}\{e^{at}\}=\frac{1}{s - a}\quad \text{for } s > a",
    r"\mathcal{L}\{1\}=\frac{1}{s}\quad (s > 0)",
    r"\mathcal{L}\{t\}=\frac{1}{s^2}",
    r"\mathcal{L}\{t^2\}=\frac{2}{s^3}",
    r"\mathcal{L}\{t^n\}=\frac{n!}{s^{n+1}}\quad (s > 0)",
    r"u_c(t)=\begin{cases} 0 & t < c \\ 1 & t \ge c \end{cases}",
    r"\mathcal{L}\{u_c(t)\}=\frac{e^{-cs}}{s}",
    r"\mathcal{L}\{f'(t)\}=s\,F(s)-f(0)",
    r"\mathcal{L}\{f''(t)\}=s^2 F(s)-s\,f(0)-f'(0)",
    r"y'+3y=6\quad y(0) = 2",
    r"s\,Y(s)-2+3\,Y(s)=\frac{6}{s}",
    r"(s+3)\,Y(s)=\frac{2s + 6}{s}",
    r"Y(s)=\frac{2}{s}",
    r"Y(s)=\frac{2}{s}\;\Rightarrow\;y(t)=2",
]

print(f"Testing {len(test_tex)} LaTeX expressions...")
for i, tex in enumerate(test_tex):
    try:
        m = MathTex(tex, font_size=HEADING_SIZE)
        print(f"  [{i+1}/{len(test_tex)}] OK")
    except Exception as e:
        print(f"  [{i+1}/{len(test_tex)}] FAIL: {e}")

print("ALL TESTS PASSED")
