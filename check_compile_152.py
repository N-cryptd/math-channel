#!/usr/bin/env python3
"""Compile check helper."""
import py_compile
import sys
path = sys.argv[1] if len(sys.argv) > 1 else "scripts/graduate/video-152-sigma-algebras.py"
try:
    py_compile.compile(path, doraise=True)
    print(f"OK: {path}")
except py_compile.PyCompileError as e:
    print(f"ERROR: {e}")
    sys.exit(1)
