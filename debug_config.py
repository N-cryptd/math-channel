#!/usr/bin/env python3
from manim import config
print("format:", config.format)
print("tex_file_to_svg:", getattr(config, 'tex_file_to_svg', 'NOT SET'))
