from __future__ import print_function

import json
from random import shuffle

with open("teams.json") as f:
    teams = json.load(f)

shuffle(teams)
print(", ".join(teams))
