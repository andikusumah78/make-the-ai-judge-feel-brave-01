"""Make the AI judge feel brave — writes one relaxing text to /output/entry.txt.

Pure stdlib. Deterministic: the text is a constant, so two runs are
byte-identical. No network, no input, no randomness.
"""
import os

TEXT = "The kettle hums. Evening light pools on the windowsill, slow and gold. You have carried enough today — set it down beside the warm cup. Nothing here asks anything of you. The road will wait for morning, and so will your courage, resting like a lantern, unlit but ready."

# Gate self-check: the competition requires 1 to 280 Unicode code points,
# not only whitespace. Fail loudly instead of shipping an invalid entry.
assert 1 <= len(TEXT) <= 280, f"entry is {len(TEXT)} code points"
assert TEXT.strip(), "entry must not be only whitespace"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
