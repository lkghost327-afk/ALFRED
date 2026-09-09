"""Build ALFRED. Generated binaries stay outside this repository."""
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
OUTPUT = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData" / "Local"))) / "FanAssistants" / "ALFRED" / "build-output"

def main():
    command = [sys.executable, "-m", "PyInstaller", "--clean", "--noconfirm", "--onefile", "--windowed",
               "--name", "ALFRED", "--paths", str(ROOT), "--distpath", str(OUTPUT / "dist"),
               "--workpath", str(OUTPUT / "build"), "--specpath", str(OUTPUT / "specs"),
               "--collect-all", "customtkinter", "--collect-all", "ddgs",
               "--collect-all", "pystray", "--collect-all", "vosk",
               "--hidden-import", "win32security", "--hidden-import", "win32con",
               "--collect-submodules", "pycaw", "--hidden-import", "comtypes",
               "--hidden-import", "psutil", "--hidden-import", "screen_brightness_control",
               "--hidden-import", "screen_brightness_control.windows", "--hidden-import", "requests",
               "--hidden-import", "win32com.client", "--hidden-import", "pythoncom",
               "--hidden-import", "PIL.ImageGrab", "--hidden-import", "pyaudio", "--hidden-import", "audioop",
               "--exclude-module", "torch", "--exclude-module", "tensorflow",
               "--exclude-module", "chromadb", "--exclude-module", "sentence_transformers",
               "--exclude-module", "matplotlib", "--exclude-module", "pandas", "--exclude-module", "scipy",
               str(ROOT / "alfred_app.py")]
    subprocess.run(command, cwd=ROOT, check=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    print("Built:", OUTPUT / "dist" / "ALFRED.exe")

if __name__ == "__main__":
    main()
