"""Part B: physics check. TODO 3."""
from __future__ import annotations

import math

from avsim import core

G = 9.81


def is_feasible(p: dict) -> bool:
    """TODO 3. False for scenarios no real road user could produce. Reject if ANY of:

    - the lane change needs more sideways grip than the road has: the cosine lane change of 3.5 m over
      p["cutDur"] seconds peaks at a_lat = (pi / cutDur)^2 * 3.5 / 2; reject if a_lat > mu * g;
    - the post-merge braking p["cutBrake"] exceeds mu * g;
    - the pedestrian runs: p["pedV"] > 2.5 m/s;
    - the cut-in speed p["cutV"] is not in (0, 22] m/s.
    mu is p["mu"]. A search that keeps infeasible scenarios reports failures that cannot happen.
    """
    d = core.DEFAULTS
    mu = float(p.get("mu", d["mu"]))
    grip = mu * G
    cut_dur = float(p.get("cutDur", d["cutDur"]))
    if cut_dur <= 0 or (math.pi / cut_dur) ** 2 * 3.5 / 2 > grip:
        return False
    if float(p.get("cutBrake", d["cutBrake"]) or 0.0) > grip:
        return False
    if float(p.get("pedV", d["pedV"])) > 2.5:
        return False
    cut_v = float(p.get("cutV", d["cutV"]))
    if not 0.0 < cut_v <= 22.0:
        return False
    return True
