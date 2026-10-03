# Photon Dash — a REPACSS game

*Photon Dash* is a 3D browser runner about **REPACSS** (REmotely-managed Power Aware Computing Systems and Services) at Texas Tech University, supported by NSF Award 2404438.

You ride one photon from the Sun, through the West Texas sky and into the 350 kW solar array at the GLEAMM microgrid. From there you travel down the power bus as an electron, through the REPACSS cluster, and out of the tensor cores as tokens. Each of the five stages opens with a real fact about the facility:

1. Leaving the Sun
2. The West Texas sky
3. Silicon to the power bus
4. Into the REPACSS cluster
5. Tensor cores to tokens

The game lives in `game3d/`. All of its code is in `index.html`, built with [three.js](https://threejs.org) (loaded from a CDN); the folder also holds the intro video and two logos.

## Play

Play online at **[claude.ai/artifact/N62dhZ5E4VnShD3HJtuEP6](https://claude.ai/artifact/N62dhZ5E4VnShD3HJtuEP6)**, or open `game3d/index.html` in a browser. It needs an internet connection for three.js and the fonts.

- **Steer:** mouse or touch, or the arrow keys / WASD.
- **Pause:** P or Esc. While paused, E ends the run.
- **Full screen:** the corner button or F.
- **Intro:** each time you press Launch on the start screen, it plays a 45-second narrated intro (`game3d/intro.mp4`, captioned). Skip it with the Skip button or Esc.
- **Practice a stage:** add `#stage1` … `#stage5` to the URL.
- **Scoreboard:** the start screen asks for a pilot name, and the start and end screens show a top-10 board. On the [online version](https://claude.ai/artifact/N62dhZ5E4VnShD3HJtuEP6), everyone who plays shares one board, with one best run per pilot name. When you open the game as a local file, the board is kept only on that device.

## The intro video

`game3d/intro.mp4` is cut from *REPACSS — From Photons to Tokens*, a 7-minute explainer video rendered from code. The video and its source live in [Artlands/REPACSS_animation](https://github.com/Artlands/REPACSS_animation). The pipeline that cut this intro (`game3d/make_intro.py` with the narration, render and music scripts) is in this repo's history at commit [`b28e7d4`](https://github.com/Artlands/REPACSS_game/tree/b28e7d4c5afa81811ab4bedb56f9ff3e28ff5812).

## Sources and credits

- Facility, cluster, node and network details come from REPACSS project materials. GLEAMM building and site layout follow REPACSS site photos and the [repacss.org gallery](https://www.repacss.org/gallery/).
- Earth imagery in the intro: NASA Visible Earth, *Blue Marble: Next Generation* (July 2004), including a 240 px/degree crop over West Texas. City lights, clouds and ocean mask come from the three.js example textures (NASA-derived).

## License

Code is released under the [MIT License](LICENSE). The REPACSS, Texas Tech and NSF names and logos in `game3d/` are trademarks of their owners and are not covered by this license. The Earth imagery in the intro is NASA public-domain data.
