import os, glob
files = [
    "/root/math-channel/compile_check.py",
    "/root/math-channel/import_check.py",
    "/root/math-channel/channel-analysis/search_probability.js",
    "/root/math-channel/channel-analysis/search_probability2.js",
    "/root/math-channel/channel-analysis/fetch_prob_meta.js",
]
for f in files:
    if os.path.exists(f):
        os.remove(f)
        print(f"Removed {f}")
print("Cleanup done")
