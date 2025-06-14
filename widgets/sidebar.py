# Sidebar widget for note navigation
import customtkinter as ctk
from config.settings import settings

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configure frame
        self.configure(fg_color=settings["sidebar_bg"])

        # Title label
        self.title_label = ctk.CTkLabel(
            self, text="Notes", font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        # Placeholder for note list
        self.note_list = ctk.CTkLabel(
            self, text="Note list placeholder", text_color="grey"
        )
        self.note_list.pack(pady=10)