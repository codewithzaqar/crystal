import customtkinter as ctk
import markdown2
import tkinter as tk
from core.note_manager import NoteManager

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

        # Metadata label (for timestamps)
        self.meta_label = ctk.CTkLabel(self, text="", font=("Roboto", 10, "italic"))
        self.meta_label.grid(row=1, column=0, padx=10, pady=2, sticky="w")

        # Text area
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        # Edit tab
        self.edit_tab = self.tabview.add("Edit")
        self.text_area = ctk.CTkTextbox(self.edit_tab, wrap="word", font=("Roboto", 12))
        self.text_area.pack(fill="both", expand=True, padx=5, pady=5)

        # Preview tab
        self.preview_tab = self.tabview.add("Preview")
        self.preview_text = tk.Text(self.preview_tab, wrap="word", font=("Roboto", 12), bg="#1E1E1E", fg="white", bd=0)
        self.preview_text.pack(fill="both", expand=True, padx=5, pady=5)
        self.preview_text.config(state="disabled")

        # Save button
        self.save_button = ctk.CTkButton(self, text="Save", command=self.save_note)
        self.save_button.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        # Bind text changes to auto-save (optional)
        self.text_area.bind("<KeyRelease>", lambda e: self.update_preview())
        self.text_area.bind("<KeyRelease>", lambda e: self.save_note())

    def set_note_content(self, title, content):
        """Set the content of the editor for a given note."""
        self.current_note = title
        self.title_label.configure(text=title)
        self.text_area.delete("1.0", "end")
        self.text_area.insert("1.0", content)
        self.update_preview()

        # Update metadata display
        metadata = self.note_manager.get_note_metadata(title)
        if metadata:
            created = metadata.get("created", "N/A")
            modified = metadata.get("modified", "N/A")
            self.meta_label.configure(text=f"Created: {created} | Modified: {modified}")
        else:
            self.meta_label.configure(text="")

    def update_preview(self):
        """Update the markdown preview."""
        content = self.text_area.get("1.0", "end-1c")
        html = markdown2.markdown(content)
        self.preview_text.config(state="normal")
        self.preview_text.delete("1.0", "end")
        self.preview_text.insert("1.0", html)
        self.preview_text.config(state="disabled")

    def save_note(self):
        """Save the current note content."""
        if self.current_note and self.current_note != "No Note Selected":
            content = self.text_area.get("1.0", "end-1c")
            self.note_manager.save_note(self.current_note, content)