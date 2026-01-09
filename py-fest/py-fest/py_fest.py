# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

print(lineup)
remove_band = lineup.pop(0)
lineup.append(remove_band)
print(lineup)
remove_band = lineup.pop(1)
print(lineup)
for band in lineup:
    print(f"{band[0]} - {band[1]} ({band[2]} mins)")
# Continue the logic below...