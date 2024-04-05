chinese = ["heart", "diamond", "spade", "club"]
suits = chinese


nest = list(suits)

from unicodedata import lookup

[lookup("WHITE " + s.upper() + " SUIT") for s in suits]
