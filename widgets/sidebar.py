# Sidebar widget for note navigation
import customtkinter as ctk
from config.settings import settings

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, add_note_callback, select_note_callback, **kwargs):
        super().__init__(master, **kwargs)

        # Configure frame
        self.configure(fg_color=settings["sidebar_bg"])
        self.add_note_callback = add_note_callback
        self.select_note_callback = select_note_callback
        self.note_buttons = []

        # Title label
        self.title_label = ctk.CTkLabel(
            self, text="Notes", font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        # New note button
        self.new_note_button = ctk.CTkButton(
            self, text="New Note", command=self.add_note
        )
        self.new_note_button.pack(pady=5)

        # Note list frame
        self.note_list_frame = ctk.CTkFrame(self, fg_color=settings["sidebar_bg"])
        self.note_list_frame.pack(pady=10, fill="both", expand=True)

    def add_note(self):
        """Trigger the creation of a new note."""
        self.add_note_callback()

    def update_note_list(self, notes):
        """Update the displayed list of notes."""
        # Clear existing buttons
        for button in self.note_buttons:
            button.destroy()
        self.note_buttons.clear()

        # Create a button for each note
        for note_id, note_data in notes.items():
            button = ctk.CTkButton(
                self.note_list_frame,
                text=note_data["title"],
                command=lambda nid=note_id: self.select_note_callback(nid),
                fg_color="transparent",
                anchor="w"
            )
            button.pack(fill="x", padx=5, pady=2)
            self.note_buttons.append(button)