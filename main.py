#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse (make.fun).

Writes one sick-day excuse, under 200 characters, to /output/entry.txt.

The joke is the medium: the dentist banned talking for 24 hours after pulling
a wisdom tooth, so the excuse itself arrives as a text message instead of a
phone call. The sender obeys the order by texting. One named image (the wisdom
tooth), one hard anchor (24 hours), and the twist lands in the final clause,
where the act of texting proves the excuse. Stdlib only.
"""

import os

MAX_CHARS = 199

ENTRY = (
    "Dentist pulled my wisdom tooth yesterday and banned talking for "
    "24 hours. I'm obeying him by texting you this instead of calling."
)


def looks_like_a_text(line: str) -> bool:
    """A real sick-day text: one breath, no line breaks, ends on the twist."""
    return (
        line
        and "\n" not in line
        and line[0].isupper()
        and line.endswith(".")
        and "texting" in line
    )


def twist_lands_last(line: str) -> bool:
    """The laugh must arrive near the end: the final clause names the call
    that never happened, so the punchline is the last thing read."""
    final_clause = line.rsplit(". ", 1)[-1]
    return "instead of calling" in final_clause


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} characters"
    # The dentist's order is the anchor: the excuse only works for 24 hours.
    assert "24 hours" in text, "entry must name the 24-hour ban"
    # The named image: the tooth that got pulled.
    assert "wisdom tooth" in text, "entry must name the wisdom tooth"
    # The twist: the message itself is sent by texting, not calling.
    assert looks_like_a_text(text), "entry must read as one sent text message"
    assert twist_lands_last(text), "entry must land its twist in the final clause"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
