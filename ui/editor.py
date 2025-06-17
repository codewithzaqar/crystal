import customtkinter as ctk

class EditorFrame(ctk.CTkFrame):
    def __init__(self, parent, note_manager):
        super().__init__(parent)
        self.note_manager = note_manager
        self.current_note = None

        # Configure editor
        self.configure(fg_color="#1E1E1E")  # Dark editor background
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Note title label
        self.title_label = ctk.CTkLabel(self, text="No Note Selected", font=("Roboto", 16, "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Text area
        self.text_area = ctk.CTkTextbox(self, wrap="word", font=("Roboto", 12))
        self.text_area.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        # Save button
        self.save_button = ctk.CTkButton(self, text="Save", command=self.save_note)
        self.save_button.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        # Bind text changes to auto-save (optional)
        self.text_area.bind("<KeyRelease>", lambda e: self.save_note())

    def set_note_content(self, title, content):
        """Set the content of the editor for a given note."""
        self.current_note = title
        self.title_label.configure(text=title)
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", content)

    def save_note(self):
        """Save the current note content."""
        if self.current_note:
            content = self.text_area.get("1.0", "end-1c")
            self.note_manager.save_note(self.current_note, content)