# ui/sidebar.py
import customtkinter as ctk
import os
from config.settings import NOTES_DIR

class SidebarFrame(ctk.CTkFrame):
    def __init__(self, parent, note_manager, load_note_callback):
        super().__init__(parent)
        self.note_manager = note_manager
        self.load_note_callback = load_note_callback

        # Configure sidebar
        self.configure(fg_color="#2B2B2B")  # Obsidian-like dark background
        self.grid_rowconfigure(1, weight=1)

        # New note entry and button
        self.new_note_entry = ctk.CTkEntry(self, placeholder_text="New Note Title")
        self.new_note_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        
        self.new_note_button = ctk.CTkButton(self, text="Create Note", command=self.create_note)
        self.new_note_button.grid(row=0, column=1, padx=10, pady=5)

        # Note list
        self.note_listbox = ctk.CTkTextbox(self, width=200, height=400, state="disabled")
        self.note_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # Populate note list
        self.update_note_list()

    def create_note(self):
        """Create a new note and update the list."""
        title = self.new_note_entry.get().strip()
        if title:
            self.note_manager.create_note(title)
            self.new_note_entry.delete(0, "end")
            self.update_note_list()
            self.load_note_callback(title)

    def update_note_list(self):
        """Update the list of notes in the sidebar."""
        self.note_listbox.configure(state="normal")
        self.note_listbox.delete("1.0", "end")
        notes = self.note_manager.get_note_list()
        for note in notes:
            self.note_listbox.insert("end", f"{note}\n")
        self.note_listbox.configure(state="disabled")
        self.note_listbox.bind("<Button-1>", self.on_note_click)

    def on_note_click(self, event):
        """Handle clicking on a note title in the list."""
        index = self.note_listbox.index("@%s,%s" % (event.x, event.y))
        line = int(float(index.split('.')[0]))
        note_title = self.note_manager.get_note_list()[line - 1]
        self.load_note_callback(note_title)