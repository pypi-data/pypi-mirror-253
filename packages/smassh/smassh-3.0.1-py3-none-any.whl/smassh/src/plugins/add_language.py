from rich import print
import requests
from typing import Optional
from pathlib import Path

LANGUAGE_PACK_DIR = (
    Path.absolute(Path(__file__).parent.parent.parent) / "assets" / "languages"
)


class AddLanguage:
    """
    Plugin to add new languages to smassh
    """

    def log(self, message: str, color: str = "green") -> None:
        """Logs a message to the console"""
        print(f"=>[bold {color}] {message}[/bold {color}]")

    def get_pack(self, name: str) -> Optional[str]:
        """Checks if a language pack exists. If found, it returns its contents otherwise it returns None"""

        uri = f"https://raw.githubusercontent.com/monkeytypegame/monkeytype/master/frontend/static/languages/{name}.json"
        req = requests.get(uri)

        return req.text if (req.status_code == 200) else None

    def add(self, name: str) -> None:
        """Downloads a new language for smassh"""

        self.log("Checking if language pack exists...")
        pack = self.get_pack(name)

        if pack is None:
            return self.log("Language pack doesnt exist!", "red")

        self.log("Downloading language pack...")

        with open(LANGUAGE_PACK_DIR / f"{name}.json", "w") as f:
            f.write(pack)

        self.log("Successfully downloaded the language pack!")
