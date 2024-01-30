"""
MISCELLANEOUS helper functions
"""

from typing import NamedTuple, List, Dict

from .readwrite import read_csv
from .constants import STATE_FIPS


class Assignment(NamedTuple):
    geoid: str
    district: int | str


def load_plan(plan_file: str) -> List[Assignment]:
    """Read a precinct-assignment file."""

    raw_assignments: List[Dict[str, str | int]] = read_csv(plan_file, [str, int])
    assignments: List[Assignment] = [
        Assignment(geoid=str(p["GEOID"]), district=p["DISTRICT"])
        for p in raw_assignments
    ]

    return assignments


def starting_seed(xx: str, N: int, K: int = 1) -> int:
    fips: str = STATE_FIPS[xx]
    start: int = K * N * int(fips)

    return start


### END ###
