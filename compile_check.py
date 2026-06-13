import py_compile
import sys
path = sys.argv[1] if len(sys.argv) > 1 else "scripts/undergraduate/video-63-laplace-transforms.py"
py_compile.compile(path, doraise=True)
print("COMPILE OK")
