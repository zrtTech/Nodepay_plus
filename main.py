import customtkinter as ctk
import asyncio
import json
import os

from core.utils.logger import *
from customtkinter_gui import BotGUI

SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    root = ctk.CTk()

    app = BotGUI(root)
    app.setup_logger()
    root.mainloop()
