import customtkinter as ctk
from config import theme


class BasePage(ctk.CTkFrame):
    def __init__(self, parent, title):
        ctk.set_appearance_mode("light")
        super().__init__(parent, fg_color="transparent")

        ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont(size=theme.FONT_SIZE_TITLE,weight="bold"),
            text_color= theme.TEXT_COLOR,
        ).grid(row=0, column=0, padx=30,pady=30, sticky="w")