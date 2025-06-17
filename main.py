import customtkinter as ctk
from ui.app import CrystalApp

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = CrystalApp()
    app.mainloop()

if __name__ == "__main__":
    main()