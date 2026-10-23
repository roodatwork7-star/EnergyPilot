import customtkinter as ctk
from views.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self,parent):
        super().__init__(parent, title="Dashboard")
