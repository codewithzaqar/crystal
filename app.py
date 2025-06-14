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

        # Initialize widgets
        self.sidebar = Sidebar(master=self, width=250)
        self.note_editor = NoteEditor(self)

        # Place widgets in grid
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.note_editor.grid(row=0, column=1, sticky="nsew")

    def run(self):
        self.mainloop() 