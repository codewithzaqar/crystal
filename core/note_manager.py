import os
from config.settings import NOTES_DIR

class NoteManager:
    def __init__(self):
        if not os.path.exists(NOTES_DIR):
            os.makedirs(NOTES_DIR)

    def create_note(self, title):
        """Create a new note file."""
        file_path = os.path.join(NOTES_DIR, f"{title}.txt")
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("")

    def save_note(self, title, content):
        """Save content to a note file."""
        file_path = os.path.join(NOTES_DIR, f"{title}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def load_note(self, title):
        """Load content from a note file."""
        file_path = os.path.join(NOTES_DIR, f"{title}.txt")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        return ""
    
    def get_note_list(self):
        """Get a list of all note titles."""
        return [f.replace(".txt", "") for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]