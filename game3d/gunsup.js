// Texas Tech "Guns Up": index finger out, thumb up, the other three fingers curled.
// `w` is one hand's 21 MediaPipe world landmarks (meters, hand-centered), so the test works whichever way the hand points,
// including straight at the camera. Thresholds are the tuning knobs. A classic script (not a module) so the game still opens from file://.
const GUNS = { indexOut: 1.55, curled: 1.3, thumbOut: 0.75 };
const d = (a, b) => Math.hypot(a.x - b.x, a.y - b.y, a.z - b.z);
function isGunsUp(w) {
  const reach = (mcp, tip) => d(w[0], w[tip]) / d(w[0], w[mcp]);   // ~2 straight, ~1 folded into the palm
  return reach(5, 8) > GUNS.indexOut
    && reach(9, 12) < GUNS.curled && reach(13, 16) < GUNS.curled && reach(17, 20) < GUNS.curled
    && d(w[4], w[13]) / d(w[0], w[9]) > GUNS.thumbOut;   // thumb tip well away from the ring knuckle, not tucked across the fist
}

// self-check: node game3d/gunsup.js
if (globalThis.process?.argv?.[1]?.endsWith('gunsup.js')) {
  const P = (x, y, z = 0) => ({ x, y, z });
  // a right hand, palm facing the camera, fingers up the y axis; each finger is [mcp, pip, dip, tip]
  const straight = (x) => [P(x, .09), P(x, .13), P(x, .155), P(x, .175)];
  const folded = (x) => [P(x, .09), P(x, .115, .02), P(x, .095, .04), P(x, .075, .03)];
  const hand = (thumb, index, mid, ring, pinky) => [P(0, 0), ...thumb, ...index(.025), ...mid(0), ...ring(-.02), ...pinky(-.038)];
  const thumbUp = [P(.025, .02), P(.045, .04), P(.06, .07), P(.065, .095)];
  const thumbTucked = [P(.025, .02), P(.035, .04), P(.02, .07, .04), P(.005, .09, .045)];
  const cases = [
    ['guns up', hand(thumbUp, straight, folded, folded, folded), true],
    ['fist', hand(thumbTucked, folded, folded, folded, folded), false],
    ['open hand', hand(thumbUp, straight, straight, straight, straight), false],
    ['pointing, thumb tucked', hand(thumbTucked, straight, folded, folded, folded), false],
    ['peace sign', hand(thumbTucked, straight, straight, folded, folded), false],
  ];
  // pointing at the camera: rotate the guns-up hand 90° about x so the index runs along z
  const rot = (p) => P(p.x, -p.z, p.y);
  cases.push(['guns up, pointing at camera', cases[0][1].map(rot), true]);
  let bad = 0;
  for (const [name, w, want] of cases) { const ok = isGunsUp(w) === want; bad += !ok; console.log(`${ok ? 'ok  ' : 'FAIL'} ${name}`); }
  process.exitCode = bad ? 1 : 0;
}
