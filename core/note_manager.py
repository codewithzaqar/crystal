import os
import json
import datetime
from config.settings import NOTES_DIR, METADATA_DIR

class NoteManager:
    def __init__(self):
        if not os.path.exists(NOTES_DIR):
            os.makedirs(NOTES_DIR)
        if not os.path.exists(METADATA_DIR):
            os.makedirs(METADATA_DIR)

    def create_note(self, title):
        """Create a new note file."""
        file_path = os.path.join(NOTES_DIR, f"{title}.md")
        meta_path = os.path.join(METADATA_DIR, f"{title}.json")
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            metadata = {"created": timestamp, "modified": timestamp}
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f)

    def save_note(self, title, content):
        """Save content to a note file."""
        file_path = os.path.join(NOTES_DIR, f"{title}.md")
        meta_path = os.path.join(METADATA_DIR, f"{title}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        metadata = self.get_note_metadata(title) or {"created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        metadata["modified"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f)

    def load_note(self, title):
        """Load content from a note file."""
        file_path = os.path.join(NOTES_DIR, f"{title}.md")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        return ""
    
    def delete_note(self, title):
        """Delete a note and its metadata."""
        file_path = os.path.join(NOTES_DIR, f"{title}.md")
        meta_path = os.path.join(METADATA_DIR, f"{title}.json")
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(meta_path):
            os.remove(meta_path)
    
    def get_note_list(self):
        """Get a list of all note titles."""
        return [f.replace(".md", "") for f in os.listdir(NOTES_DIR) if f.endswith(".md")]
    
    def get_note_metadata(self, title):
        """Load metadata for a note."""
        meta_path = os.path.join(METADATA_DIR, f"{title}.json")
        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None