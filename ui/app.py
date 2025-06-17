# ui/app.py
import customtkinter as ctk
from ui.sidebar import SidebarFrame
from ui.editor import EditorFrame
from core.note_manager import NoteManager

class CrystalApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Crystal")
        self.geometry("800x600")

        # Initialize note manager
        self.note_manager = NoteManager()

        # Create main layout with sidebar and editor
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = SidebarFrame(self, self.note_manager, self.load_note)
        self.sidebar.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

        # Editor
        self.editor = EditorFrame(self, self.note_manager)
        self.editor.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    def load_note(self, note_title):
        """Callback to load a note into the editor."""
        content = self.note_manager.load_note(note_title)
        self.editor.set_note_content(note_title, content)