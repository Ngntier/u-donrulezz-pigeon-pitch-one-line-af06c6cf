"""Entry program for the Pigeon Pitch, One Line bounty.

Joke angle: the pitch sells pigeons as an advertising network, leaning on
ad-tech language (impressions, blocking, swiping) and then undercutting the
slick startup framing with the bird's own obsession -- the investor's lunch.
The voice stays a city pigeon's throughout: the product, the audience, and
the punchline could only belong to a bird that lives on statues and crumbs.
"""

import os

ENTRY = (
    "Our ad network is four million pigeons \u2014 the only screens you "
    "can't swipe past, can't block, and can't ignore, because one of them "
    "is staring at your sandwich right now."
)


def main() -> None:
    line = ENTRY
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    # Byte budget is the real constraint at the sealed gate (the file is
    # written as bytes), so check it directly too — the entry contains an
    # em dash, so its UTF-8 length exceeds its char count.
    if len(line.encode("utf-8")) > 200:
        raise ValueError("entry exceeds the 200-byte budget")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must have no leading or trailing whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(line.encode("utf-8"))


if __name__ == "__main__":
    main()
