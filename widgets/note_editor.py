# Note editor widget for writing and editing notes
import customtkinter as ctk
from config.settings import settings

class NoteEditor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configure frame
        self.configure(fg_color=settings["editor_bg"])

        # Text area for editing notes
        self.text_area = ctk.CTkTextbox(
            self,
            font=("Helvetica", settings["font_size"]),
            wrap="word",
        )
        self.text_area.pack(pady="10", padx=10, fill="both", expand=True)

        # Placeholder text
        self.text_area.insert("1.0", "Start typing your note here...")