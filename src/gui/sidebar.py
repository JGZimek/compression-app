import customtkinter as ctk
from gui.widgets import SidebarButton


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, width=220, corner_radius=0)
        self.app = app  # Referencja do głównej klasy aplikacji
        self.configure(fg_color="#1f1f1f")
        self.create_widgets()

    def create_widgets(self):
        # Nagłówek sidebaru
        header = ctk.CTkLabel(self, text="Menu", font=("Arial", 20), text_color="white")
        header.pack(pady=20, padx=10)

        # Przycisk do widoku kompresji audio
        btn_audio = SidebarButton(
            self,
            text="Audio Kompresja",
            command=lambda: self.app.show_page("AudioCompressionView"),
        )
        btn_audio.pack(pady=10, padx=10, fill="x")

        # Przycisk do widoku kompresji obrazów
        btn_image = SidebarButton(
            self,
            text="Obraz Kompresja",
            command=lambda: self.app.show_page("ImageCompressionView"),
        )
        btn_image.pack(pady=10, padx=10, fill="x")

        # Przycisk do widoku statystyk
        btn_stats = SidebarButton(
            self,
            text="Statystyki",
            command=lambda: self.app.show_page("StatisticsView"),
        )
        btn_stats.pack(pady=10, padx=10, fill="x")

        # Przycisk do widoku ustawień
        btn_settings = SidebarButton(
            self, text="Ustawienia", command=lambda: self.app.show_page("SettingsView")
        )
        btn_settings.pack(pady=10, padx=10, fill="x")

        # Dodatkowe opcje – przykładowe elementy
        options_label = ctk.CTkLabel(
            self, text="Opcje:", text_color="white", font=("Arial", 16)
        )
        options_label.pack(pady=(20, 5), padx=10)

        self.options_menu = ctk.CTkOptionMenu(
            self, values=["Opcja 1", "Opcja 2", "Opcja 3"]
        )
        self.options_menu.pack(pady=10, padx=10, fill="x")

        self.toggle_feature = ctk.CTkSwitch(self, text="Funkcja A", text_color="white")
        self.toggle_feature.pack(pady=10, padx=10)

        self.toggle_feature2 = ctk.CTkSwitch(self, text="Funkcja B", text_color="white")
        self.toggle_feature2.pack(pady=10, padx=10)
