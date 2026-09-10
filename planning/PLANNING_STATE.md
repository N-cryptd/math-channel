# Math Channel — Planning State

Last updated: 2026-09-10 (SP pacing campaign notes; full per-video detail in planning/improvement-tracker.md)

## Completed Videos
- Videos 1-24: Calculus I/II (scripts in scripts/pre-university/)
- Videos 25-29: Linear Algebra (scripts in scripts/undergraduate/)
- Videos 30-109: Various (see filesystem)
- Videos 100-110: Real Analysis I (12 videos)
  - All scripts in scripts/undergraduate/video-10*.py
  - All plans in planning/video-10*.md
- Videos 111-113: Abstract Algebra I (Videos 1-3)
  - Video 111: Groups — Definition and Examples (competitive analysis done, script done)
  - Video 112: Subgroups and Cyclic Groups (script done)
  - Video 113: Permutation Groups (script done)

## In Progress
- Video 114: Cosets and Lagrange's Theorem (Abstract Algebra I, Video 5 of 12)
  - Plan: planning/video-114-cosets-and-lagranges-theorem.md — DONE
  - Script: scripts/undergraduate/video-114-cosets-and-lagranges-theorem.py — DONE (9 scenes, compile-checked)
  - Render: PENDING

## Completed Playlists
- Calculus I: Limits & Derivatives
- Calculus II: Integrals & Series
- Linear Algebra
- Real Analysis I: COMPLETE (all content done)

## Active Playlists
- Abstract Algebra I (in progress, Videos 111-114 done, 115+ remaining)
- Complex Analysis (in progress, Videos 126-129 done)

## Active Playlists
|- Topology (in progress, Videos 139-140 done)
  - Video 139: Introduction to Topology — plan + script + render done
  - Video 140: Connectedness — plan + script + render done (2026-07-31)
  - Scripts in scripts/graduate/
|- Measure Theory (in progress, Videos 151-155 done)
  - Video 151: Measure Theory Introduction — plan + script + render done
  - Video 152: Sigma-Algebras — plan + script + render done
  - Video 153: Measures — plan + script + render done
  - Video 154: Lebesgue Measure — plan + script + render done
  - Video 155: Lebesgue Measurable Functions — plan + script + render done (2026-08-03)
  - Scripts in scripts/graduate/

## Upcoming Playlists
|- Calculus III (Multivariable)

## Complex Analysis Progress
|- Video 126: Complex Numbers Revisited — plan + script done
|- Video 127: Complex Functions — plan + script done
|- Video 128: Limits and Continuity in C — plan + script done
|- Video 129: Complex Differentiation — plan + script done
|- Video 130-138: Contour Integrals through Conformal Mappings — all done

## PDE Playlist (Videos 184-193)
|- Video 184: What is a PDE? — plan + script done
|- Video 185: The Heat Equation — plan + script done
|- Video 186: The Wave Equation — plan + script done
|- Video 187: Laplace's Equation — plan + script done (2026-08-12)
  - Plan: planning/video-187-laplaces-equation.md (7 scenes)
  - Script: scripts/graduate/video-187-laplaces-equation.py (285 lines, compile-checked)
  - Render: PENDING
- Video 188: Separation of Variables -- plan + script + render done (2026-08-15)
  - Plan: planning/video-188-separation-of-variables.md (8 scenes)
  - Script: scripts/graduate/video-188-separation-of-variables.py (324 lines)
  - Render: DONE (480p15, 95.6s, 3.3MB, 171 animations, 8 TTS segments)
- Video 189: Sturm-Liouville Theory -- plan + script done (2026-08-12)
  - Plan: planning/video-189-sturm-liouville.md (8 scenes)
  - Script: scripts/graduate/video-189-sturm-liouville.py (328 lines)
  - Render: PENDING
- Video 190: Green's Functions -- plan + script done (2026-08-12)
  - Plan: planning/video-190-greens-functions.md (7 scenes)
  - Script: scripts/graduate/video-190-greens-functions.py (7 scenes, compile-checked)
  - Render: PENDING
- Video 191-193: PDE remaining (plans + scripts done)

## Differential Geometry Playlist (Videos 194-206) — COMPLETE
|- Video 194: Curves in R^n — plan + script + render done
|- Video 195: Arc Length and Curvature — plan + script + render done (2026-08-14)
  - Plan: planning/video-195-arc-length-curvature.md (8 scenes)
  - Script: scripts/graduate/video-195-arc-length-curvature.py (8 scenes, compile-checked)
  - Render: 480p15, 96.6s, 166 animations, 15 TTS segments
|- Video 196: Frenet-Serret Frame — plan + script + render done
|- Video 197: Surfaces in R^3 — plan + script + render done
|- Video 198: First Fundamental Form — plan + script + render done
|- Video 199: Second Fundamental Form — plan + script + render done
|- Video 200: Gaussian Curvature — plan + script + render done
|- Video 201: Geodesics — plan + script + render done
|- Video 202: Gauss-Bonnet Theorem — plan + script done, render pending
|- Video 203: Manifolds Introduction — plan + script done, render pending
|- Video 204: Tangent Spaces and Vector Fields — plan + script done, render pending
|- Video 205: Differential Forms — plan + script done, render pending
|- Video 206: Stokes on Manifolds (FINALE) — plan + script + render done (2026-08-15)
  - Script: scripts/graduate/video-206-stokes-on-manifolds.py (387 lines)
  - Render: 480p15, ~65s, 2.3MB
  - Note: Fixed LaTeX \oiint → \oint\!\!\!\oint for esint compat

## Algebraic Topology Playlist (Videos 207+)
|- Video 207: Homotopy — plan + script + render done (2026-08-17)
  - Plan: planning/video-207-homotopy.md (7 scenes)
  - Script: scripts/graduate/video-207-homotopy.py (432 lines, compile-checked)
  - Render: 480p15
|- Video 208: The Fundamental Group — plan + script done (2026-08-17)
  - Script: scripts/graduate/video-208-fundamental-group.py (616 lines, compile-checked)
  - Render: PENDING

## Pacing Campaign Notes (updated 2026-09-10)

NOTE: this file was restored from an Aug-15 git revision on Sep 10 (after the Video 264 completion run corrupted it with a runaway prepend loop). Per-video progress lives in planning/improvement-tracker.md — that file is authoritative.

- Pre-Aug-2026 render pacing audit (t_475b35a7): Videos 25-29, 99-125 all measured; 30 defective videos FIXED and verified Sep 5-6. Full table: improvement-tracker.md "2026-09-05" section.
- Number Theory cohort (251-265): pacing campaign COMPLETE Sep 8-10 — every video fixed (declareds → natural+0.7 + block-final wait bumps), re-rendered, verified (0 speedup warnings, 0 skips, dot QA pass, md5-matched copies in rendered/).
- Stochastic Processes cohort (229-240, in progress):
  - 229 Random Walks FIXED Sep 10 (t_7106ac20): 20 declareds → natural+0.7 + 22 wait edits (2 passes; caption→gap attribution off-by-one found and corrected), 219.5s render verified clean, md5 19305cd7 → rendered/.
  - 230 Markov Chains FIXED Sep 10 (t_0a5efeb8): 21 declareds → natural+0.7 + 21 wait bumps (single pass using the 229 attribution lesson), post-fix render verified end-to-end: 226.8s (3:47), 21/21 narrated, 0 speedup warnings, 0 skips, slot usage 0.777-0.956x (every span ≥ natural+0.3s), audio -20.4 dB mean / -2.3 dB peak, dot QA PASS 227/227 frames, md5 b15d8e09 → rendered/Video230_MarkovChains_narrated.mp4 (render 10:50 > script 10:47).
  - 231 Classification of States VERIFIED healthy Sep 10 (t_37af286a): NO fix needed — naturals 71.5s vs spans ≥ natural+2.8s (ratios 0.49-0.77x); fresh 113.5s render verified, 8/8 narrated, dot QA PASS 113/113, md5 4e090106 → rendered/ copy refreshed (shipped SRT had been lost to media/ cleanup; baseline re-render regenerated it).
  - 232 Stationary Distributions FIXED Sep 10 (t_597e1f2b): single borderline slot cap4 (0.97x — passed span<natural+0.3 by 27ms, failed the 0.93 healthy gate), cap4 declared 9→9.94 + scene4 final wait NORMAL(1.2)→2.2, 92.1s render verified clean (0/7 defects, every span ≥ natural+1.29s), md5 cd292f74 → rendered/.
  - 233 Poisson Processes FIXED Sep 10 (t_ba3f396e): cap2/cap6 borderline ratios (0.955x/0.956x) + hidden third gate — 3 under-declared clips (cap1 flagged 1.106x speedup on first fix render; slot = declared − 0.3s gap), 3 declareds → natural+0.7 (11.43/11.04/9.84) + 2 scene-final wait bumps (1.2→1.8/1.9), 91.06s render verified end-to-end (7/7 narrated, 0 warnings, 0 skips, 0/7 defects, every span ≥ natural+1.06s, ratios 0.575-0.907x, audio -21.4 dB, dot QA PASS 91/91), md5 c45283bc → rendered/Video233_PoissonProcesses_narrated.mp4.
  - 234 Continuous-Time Markov Chains FIXED Sep 10 (t_4c2b649d): 5/7 defective — FIRST OVERLAPPING-slots case (cap4's declared 9s end ran 3.2s past cap5's start; narrate capped the slot at 5.47s for an 8.18s natural → 1.496x speedup, near the 1.5x atempo limit) + 3 silent sub-threshold speedups never logged (cap3 1.030x, cap6 1.067x, cap7 1.044x — all under the 1.08 warn line) + cap2 razor-thin usage 0.994x. Fix: 5 declareds → natural+0.7 (9.65/11/8.88/9.24/11.14) + scene4 final wait NORMAL→5.0 (+3.8s). 83.3s render verified end-to-end (7/7 narrated, 0 warnings, 0 skips, 0/7 defects, every span ≥ natural+1.35s, ratios 0.657-0.858x, usage ≤0.958x, audio -20.9 dB, dot QA PASS 89% coverage with all 17 dips mapped to ly.clear() transitions — known-FP pattern), md5 b418a13a → rendered/Video234_ContinuousTimeMarkovChains_narrated.mp4. LESSON: measure usage = natural/min(declared_end, next_start−0.3) ≤ 0.97 per caption — sub-1.08x speedups never hit the warnings log.
- NEXT: SP cohort 235-240 pacing audits — measure naturals with DIRECT single-clip edge-tts (en-US-AndrewNeural --rate=-5%) vs shipped SRT spans; THREE gates (233 lesson): span < natural+0.3 (defect), ratio natural/span ≤ 0.93 (healthy), declared ≥ natural per caption (else narrate speedup — check media/narration_speedup_warnings.log on every render) PLUS the 234 usage check (natural/min(declared_end, next_start−0.3) ≤ 0.97 — catches overlapping declared ends and silent sub-1.08x speedups); fix recipe + caption→gap attribution rules in improvement-tracker.md SP audit section (2026-09-10). If shipped SRT is missing from media/ (cleanup), re-render baseline FIRST to regenerate it (231 protocol).
- Kanban DB: the malformed board was quarantined (kanban.db.corrupt7.bak) and RESET Sep 10 ~midday; fresh board is operational (task creation + dispatch verified with the 233 cycle). Filesystem (improvement-tracker.md + this file + git log) remains the authoritative record.
