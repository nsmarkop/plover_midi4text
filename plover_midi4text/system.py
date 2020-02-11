from typing import Dict, List, Optional, Tuple, Union

KEYS: Tuple[str, ...] = (
    "F-",
    "S-",
    "C-",
    "Z-",
    "P-",
    "N-",
    "R-",
    "X-",
    "I-",
    "U-",
    "-u",
    "-i",
    "-e",
    "-a",
    "-n",
    "-p",
    "-z",
    "-c",
    "-s",
    "-f",
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS: Tuple[str, ...] = ()

NUMBER_KEY: Optional[str] = None

NUMBERS: Dict[str, str] = {}

UNDO_STROKE_STENO: str = "U-"

ORTHOGRAPHY_RULES: List[Tuple[str, str]] = []

ORTHOGRAPHY_RULES_ALIASES: Dict[str, str] = {}

ORTHOGRAPHY_WORDLIST: Optional[str] = None

KEYMAPS: Dict[str, Dict[str, Union[str, Tuple[str, ...]]]] = {
    "Michela Keyboard": {
        "F-": "C2",
        "S-": "C#2",
        "C-": "D2",
        "Z-": "D#2",
        "P-": "E2",
        "N-": "F2",
        "R-": "F#2",
        "X-": "G2",
        "I-": "G#2",
        "U-": "A2",
        "-u": "D#3",
        "-i": "E3",
        "-e": "F3",
        "-a": "F#3",
        "-n": "G3",
        "-p": "G#3",
        "-z": "A3",
        "-c": "A#3",
        "-s": "B3",
        "-f": "C4",
    },
    "MIDI Keyboard": {
        "F-": "D#2",
        "S-": "E2",
        "C-": "F2",
        "Z-": "F#2",
        "P-": "G2",
        "N-": "G#2",
        "R-": "A2",
        "X-": "A#2",
        "I-": "B2",
        "U-": "C3",
        "-u": "E3",
        "-i": "F3",
        "-e": "F#3",
        "-a": "G3",
        "-n": "G#3",
        "-p": "A3",
        "-z": "A#3",
        "-c": "B3",
        "-s": "C4",
        "-f": "C#4",
    },
}

DICTIONARIES_ROOT: str = "asset:plover_midi4text:dictionaries"

DEFAULT_DICTIONARIES: Tuple[str, ...] = (
    "midi4text_briefs.json",
    "midi4text_main.json",
)
