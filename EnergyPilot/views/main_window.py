import customtkinter as ctk

class MainWindows(ctk.CTk) :
    def __init__(self):
        super().__init__()

        self.title("Energy Pilot")
        self.geometry("1100x700")
        self.configure(fg_color="#F3F5F7")