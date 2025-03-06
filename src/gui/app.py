import customtkinter as ctk
from gui.views import MainView


class App:
    def __init__(self):
        # Ustawienia customtkinter: tryb wyglądu oraz motyw kolorystyczny
        ctk.set_appearance_mode("dark")  # dostępne: "light", "dark", "system"
        ctk.set_default_color_theme(
            "blue"
        )  # dostępne motywy: "blue", "dark-blue", "green"

        # Tworzymy główne okno aplikacji
        self.root = ctk.CTk()
        self.root.title("Aplikacja Kompresji Danych")
        self.root.geometry("800x600")  # ustal rozmiar okna

        # Inicjalizacja widoku głównego
        self.main_view = MainView(master=self.root)

    def run(self):
        self.root.mainloop()
