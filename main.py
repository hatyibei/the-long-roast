"""Entry for The Long Roast: writes the roast of my own AI agent to /output/entry.txt."""

import os

TEXT = "My agent summarized a two-word email in 2,000 words, apologized to an error message, and spent four hours confidently fixing a problem I never had. Twice."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
