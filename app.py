# Main application class to initialize and manage the app
import customtkinter as ctk
from widgets.sidebar import Sidebar
from widgets.note_editor import NoteEditor
from config.settings import settings

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Basic window setup
        self.title("Crystal")
        self.geometry("800x600")
        ctk.set_appearance_mode(settings["theme"])  # Set theme from config

        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)  # Note editor expands
        self.grid_rowconfigure(0, weight=1)  # Full height for both widgets

        # Note storage
        self.notes = {}
        self.current_note_id = None

        # Initialize widgets
        self.sidebar = Sidebar(
            master=self, 
            width=250,
            add_note_callback=self.add_note,
            select_note_callback=self.select_note
        )
        self.note_editor = NoteEditor(self, save_note_callback=self.save_note)

        # Place widgets in grid
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.note_editor.grid(row=0, column=1, sticky="nsew")

        # Add a default note
        self.add_note("Welcome Note")

    def add_note(self, title="New Note"):
        """Add a new note with a unique ID."""
        note_id = len(self.notes)
        self.notes[note_id] = {"title": title, "content": ""}
        self.sidebar.update_note_list(self.notes)
        self.select_note(note_id)

    def select_note(self, note_id):
        """Display the selected note in the editor."""
        self.current_note_id = note_id
        self.note_editor.load_note(self.notes[note_id]["title"], self.notes[note_id]["content"])

    def save_note(self, title, content):
        """Save the current note's content and update the sidebar."""
        if self.current_note_id is not None:
            self.notes[self.current_note_id] = {"title": title, "content": content}
            self.sidebar.update_note_list(self.notes)

    def run(self):
        self.mainloop() 