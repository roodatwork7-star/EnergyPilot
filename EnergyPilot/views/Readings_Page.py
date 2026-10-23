import customtkinter as ctk
from views.base_page import BasePage

class ReadingsPage(BasePage):
    def __init__(self,parent):
        super().__init__(parent, title="Releves")
