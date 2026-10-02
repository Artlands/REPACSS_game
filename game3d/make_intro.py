"""Photon Dash intro (~46 s): clips cut from the Photons to Tokens render, timed to the game_intro narration.
Usage (after `node render.mjs video` has produced build/REPACSS_photons_to_tokens_nomusic.mp4):
  .venv-tts/bin/python narration.py game_intro      # narration + timeline_game_intro.json
  .venv-tts/bin/python game3d/make_intro.py          # cut + narration -> music.py -> game3d/intro.mp4 (720p)
"""
import json, shutil, subprocess, sys

SRC = "build/REPACSS_photons_to_tokens_nomusic.mp4"
# clip id -> source segments [(start s, length s or None = whatever is left of the clip)]
CLIPS = {
    "c_sun": [(9.8, None)],                    # the Sun, a photon crossing to Earth
    "c_dive": [(26.3, None)],                  # zoom into West Texas
    "c_site": [(34.4, None)],                  # GLEAMM aerial, array and building
    "c_energy": [(108.0, None)],               # microgrid: a cloud passes, the battery discharges
    "c_photon": [(150.4, None)],               # photovoltaic conversion in the cell
    "c_compute": [(189.6, 3.4), (245.0, None)],  # the REPACSS racks, then H100 tensor cores
    "c_outro": [(410.8, None)],                # end card with the REPACSS logo
}

tl = json.load(open("timeline_game_intro.json"))
parts, labels = [], []
for sc in tl["scenes"]:
    left = sc["dur"]
    for start, length in CLIPS[sc["id"]]:
        n = min(left, length or left); left -= n
        k = len(parts)
        parts.append(f"[0:v]trim=start={start}:duration={n:.3f},setpts=PTS-STARTPTS,scale=1280:720,fps=30[v{k}]")
        labels.append(f"[v{k}]")
    assert left < 1e-6, f"{sc['id']}: segments are {left:.2f} s short"
T = tl["total"]
graph = ";".join(parts) + f";{''.join(labels)}concat=n={len(labels)}:v=1:a=0,fade=in:st=0:d=0.6,fade=out:st={T - .8:.3f}:d=0.8[v]"
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", SRC, "-i", "build/narration_game_intro.wav", "-i", "build/captions_game_intro.srt",
                "-filter_complex", graph, "-map", "[v]", "-map", "1:a", "-map", "2:s", "-c:s", "mov_text", "-metadata:s:s:0", "language=eng",
                "-c:v", "libx264", "-preset", "slow", "-crf", "24", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart",
                "build/REPACSS_game_intro_nomusic.mp4"], check=True)
subprocess.run([sys.executable, "music.py", "game_intro"], check=True)
shutil.copy("build/REPACSS_game_intro.mp4", "game3d/intro.mp4")
print("game3d/intro.mp4")  # captions for the page: INTRO_CUES in game3d/index.html, from build/captions_game_intro.srt
