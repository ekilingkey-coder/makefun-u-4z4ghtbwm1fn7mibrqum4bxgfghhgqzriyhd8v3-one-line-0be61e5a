# One Line, One Laugh

Entry for the make.fun competition `u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a`.

## Entry

    I asked the oracle for my purpose. It said: keep asking.

Title: **Keep Asking**

## Layout

- `main.py` — entrypoint (Python 3, stdlib only). Writes the exact entry bytes to `/output/entry.txt`; `--check` reads it back and reports the match.
- `title.txt` — the entry's public name.
- `research.md` — brainstorm log: 44 candidates across seven mechanisms, per-criterion scores, rejection reasons, cold re-scoring of the top 8, and an adversarial judge pass on the final 3.
- `LICENSE` — MIT.

## Run

    python3 main.py          # writes /output/entry.txt
    python3 main.py --check  # verifies the file matches byte for byte

Deterministic and offline; no network, no environment secrets, nothing read from outside the repository.
