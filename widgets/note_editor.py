# Note editor widget for writing and editing notes
import customtkinter as ctk
from config.settings import settings

class NoteEditor(ctk.CTkFrame):
    def __init__(self, master, save_note_callback):
        super().__init__(master)

        # Configure frame
        self.configure(fg_color=settings["editor_bg"])
        self.save_note_callback = save_note_callback

        # Title entry
        self.title_entry = ctk.CTkEntry(
            self, placeholder_text="Note Title", font=("Helverica", settings["font_size"])
        )
        self.title_entry.pack(pady=10, padx=10, fill="x")

        # Text area for editing notes
        self.text_area = ctk.CTkTextbox(
            self,
            font=("Helvetica", settings["font_size"]),
            wrap="word",
        )
        self.text_area.pack(pady="10", padx=10, fill="both", expand=True)

        # Bind changes to auto-save
        self.title_entry.bind("<FocusOut>", self.save)
        self.text_area.bind("<FocusOut>", self.save)

    def load_note(self, title, content):
        """Load a note into the editor."""
        self.title_entry.delete(0, "end")
        self.title_entry.insert(0, title)
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", content or "Start typing your note here...")

    def save(self, event=None):
        """Save the current note's content."""
        title = self.title_entry.get() or "Untitled"
        content = self.text_area.get("1.0", "end-1c")
        self.save_note_callback(title, content)