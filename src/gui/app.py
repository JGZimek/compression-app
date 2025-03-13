import customtkinter as ctk
from gui.sidebar import Sidebar
from gui.views.home_views import HomeView
from gui.views.audio_views import AudioCompressionView
from gui.views.image_views import ImageCompressionView
from gui.views.statistics_views import StatisticsView
from gui.views.settings_views import SettingsView


class App:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.title("Aplikacja Kompresji Danych")
        self.root.geometry("1000x600")

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.sidebar = Sidebar(self.main_frame, self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.pages = {}
        self.current_page = None
        self.init_pages()

        # Domyślny widok to HomeView
        self.show_page("HomeView")

    def init_pages(self):
        self.pages["HomeView"] = HomeView(self.content_frame)
        self.pages["AudioCompressionView"] = AudioCompressionView(self.content_frame)
        self.pages["ImageCompressionView"] = ImageCompressionView(self.content_frame)
        self.pages["StatisticsView"] = StatisticsView(self.content_frame)
        self.pages["SettingsView"] = SettingsView(self.content_frame)

    def show_page(self, page_name):
        if self.current_page is not None:
            self.pages[self.current_page].grid_forget()
        self.pages[page_name].grid(row=0, column=0, sticky="nsew")
        self.current_page = page_name

    def run(self):
        self.root.mainloop()
