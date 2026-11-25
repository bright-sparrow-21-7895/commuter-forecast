"""Entry for make.fun's "Charm the Commuter: Forecast a City That Isn't" bounty.

The forecast covers Port Meridian, a city that does not exist: sunshine with a
chance of falling pianos, light traffic, and heavy nostalgia by the waterfront —
one line of weather written to make a bored commuter smile.
"""

import os

ENTRY = "Tomorrow in Port Meridian: sunny with a chance of falling pianos, light traffic, and heavy nostalgia by the waterfront."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
