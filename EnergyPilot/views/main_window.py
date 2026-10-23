import customtkinter as ctk

from config import theme
from views.Sources_Page import SourcesPage
from views.Readings_Page import ReadingsPage
from views.dashboard_page import DashboardPage
from views.sidebar import Sidebar

class MainWindows(ctk.CTk) :
    def __init__(self):
        super().__init__()

        self.title("Energy Pilot")
        self.geometry("1100x700")
        self.configure(fg_color="#F3F5F7")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self, on_navigate=self.show_page)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content=ctk.CTkFrame(self, fg_color=theme.CONTENT_BACKGROUND)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self.current_page = None
        self.pages = {
            "dashboard": DashboardPage(self.content),
            "sources": SourcesPage(self.content),
            "readings": ReadingsPage(self.content)
        }

        self.show_page("dashboard")
        self.sidebar.set_active("dashboard")

    def show_page(self, key):
        if self.current_page is not None:
            self.current_page.grid_forget()
        showpage = self.pages[key]
        showpage.grid(row=0, column=0, sticky="nsew")
        self.current_page = showpage

