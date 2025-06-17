# ui/sidebar.py
import customtkinter as ctk
import os
from config.settings import NOTES_DIR
import tkinter.messagebox as messagebox

class SidebarFrame(ctk.CTkFrame):
    def __init__(self, parent, note_manager, load_note_callback, delete_note_callback):
        super().__init__(parent)
        self.note_manager = note_manager
        self.load_note_callback = load_note_callback
        self.delete_note_callback = delete_note_callback

        # Configure sidebar
        self.configure(fg_color="#2B2B2B")
        self.grid_rowconfigure(2, weight=1)

        # New note entry and button
        self.new_note_entry = ctk.CTkEntry(self, placeholder_text="New Note Title")
        self.new_note_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        
        self.new_note_button = ctk.CTkButton(self, text="Create", command=self.create_note)
        self.new_note_button.grid(row=0, column=1, padx=10, pady=5)

        # Scrollable frame for notes
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="#2B2B2B")
        self.scroll_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # Delete button
        self.delete_button = ctk.CTkButton(self, text="Delete Selected", command=self.delete_selected_note, state="disabled")
        self.delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.selected_note = None
        self.note_buttons = []
        self.update_note_list()

    def create_note(self):
        """Create a new note if title is valid."""
        title = self.new_note_entry.get().strip()
        if not title:
            messagebox.showerror("Error", "Note title cannot be empty.")
            return
        if any(c in title for c in '<>:"/\\|?*'):
            messagebox.showerror("Error", "Title contains invalid characters.")
            return
        if title in self.note_manager.get_note_list():
            messagebox.showerror("Error", "Note title already exists.")
            return
        self.note_manager.create_note(title)
        self.new_note_entry.delete(0, "end")
        self.update_note_list()
        self.load_note_callback(title)

    def update_note_list(self):
        """Update the list of notes as buttons."""
        # Clear existing buttons
        for button in self.note_buttons:
            button.destroy()
        self.note_buttons = []

        # Add new buttons
        notes = sorted(self.note_manager.get_note_list())
        for note in notes:
            button = ctk.CTkButton(
                self.scroll_frame,
                text=note,
                fg_color="#3B3B3B",
                hover_color="#4B4B4B",
                command=lambda n=note: self.select_note(n)
            )
            button.pack(fill="x", padx=5, pady=2)
            self.note_buttons.append(button)
        self.delete_button.configure(state="disabled")
        self.selected_note = None

    def select_note(self, note_title):
        """Handle note selection."""
        self.selected_note = note_title
        self.delete_button.configure(state="normal")
        self.load_note_callback(note_title)

    def delete_selected_note(self):
        """Delete the selected note after confirmation."""
        if self.selected_note and messagebox.askyesno("Confirm", f"Delete '{self.selected_note}'?"):
            self.delete_note_callback(self.selected_note)
            self.delete_button.configure(state="disabled")
            self.selected_note = None