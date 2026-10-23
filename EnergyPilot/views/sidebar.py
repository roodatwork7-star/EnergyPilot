import customtkinter as ctk

from config import theme

MENU = [
    ("dashboard", "Tableau de bord"),
    ("sources", "Sources d'énergie"),
    ("readings", "Relevés"),
]

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, on_navigate):
        super().__init__(
            parent,
            fg_color=theme.SIDEBAR_COLOR,
            corner_radius=0,
            width=theme.SIDEBAR_WIDTH
        )

        self.on_navigate = on_navigate
        self.buttons = {}

        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

        self._build_title()
        self._build_menu()

    def _build_title(self):
        ctk.CTkLabel(
            self,
            text="Energy Pilot",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=theme.TITRE_TEXT_COLOR
        ).grid(row=0, column=0, padx=20, pady=(25, 20), sticky="w")

    def _build_menu(self):
        for i, (key, label) in enumerate(MENU, start=1):
            bouton_menu = ctk.CTkButton(
                self,
                text=label,
                font=ctk.CTkFont(weight="bold"),
                anchor="w",
                height=40,
                corner_radius=48,
                fg_color="transparent",
                hover_color=theme.SIDEBAR_HOVER_COLOR,
                text_color=theme.TEXT_COLOR,
                command=lambda k=key: self._on_click(k)
            )
            bouton_menu.grid(row=i, column=0, padx=15, pady=4, sticky="ew")
            self.buttons[key] = bouton_menu

    def _on_click(self, key):
        self.set_active(key)
        self.on_navigate(key)

    def set_active(self, key):
        for button_key, button_object in self.buttons.items():
            if button_key == key:
                button_object.configure(fg_color=theme.ACCENT_COLOR)
            else:
                button_object.configure(fg_color="transparent")

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("600x400")
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    def test_navigate(key):
        print("navigation vers :", key)

    barre = Sidebar(app, on_navigate=test_navigate)
    barre.grid(row=0, column=0, sticky="ns")
    barre.set_active("dashboard")
    app.mainloop()