#!/usr/bin/env python3
"""Test if manim can compile a simple MathTex"""
from manim import *

class TestTex(Scene):
    def construct(self):
        t = MathTex(r"x^2 + y^2")
        self.add(t)
        self.wait(1)
