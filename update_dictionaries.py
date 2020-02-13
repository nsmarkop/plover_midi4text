#!/usr/bin/env python

import os
import shutil
import tempfile
import urllib.request
import zipfile
from typing import NamedTuple

import requests


class DictionaryInfo(NamedTuple):
    url: str
    zip_file_name: str
    desired_path: str


MAIN = DictionaryInfo(
    "https://www.midi4text.com/NuovaCartella/Midi4Text%20main%20(eng).json.zip",
    "Midi4Text main (eng).json",
    "plover_midi4text/dictionaries/midi4text_main.json",
)

BRIEFS = DictionaryInfo(
    "https://www.midi4text.com/NuovaCartella/Midi4Text%20briefs%20(eng).json.zip",
    "Midi4Text briefs (eng).json",
    "plover_midi4text/dictionaries/midi4text_briefs.json",
)


def main() -> None:
    for dictionary in (MAIN, BRIEFS):
        with tempfile.TemporaryDirectory() as directory:
            print(f"created {directory}")
            zip_path = os.path.join(directory, "zip_file.zip")

            response = requests.get(dictionary.url, stream=True)
            with open(zip_path, "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            print(f"downloaded {dictionary.url} to {zip_path}")

            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(directory)
            print(f"extracted {zip_path}")

            dictionary_path = os.path.join(directory, dictionary.zip_file_name)
            shutil.copy(dictionary_path, dictionary.desired_path)
            print(f"copied {dictionary_path} to {dictionary.desired_path}")


if __name__ == "__main__":
    main()
