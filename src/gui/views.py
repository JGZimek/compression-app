import customtkinter as ctk


class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Przykładowa etykieta powitalna
        label = ctk.CTkLabel(
            self, text="Witaj w Aplikacji Kompresji Danych", font=("Arial", 20)
        )
        label.pack(pady=20)

        # Przykładowy przycisk do uruchomienia procesu kompresji
        button = ctk.CTkButton(
            self, text="Uruchom kompresję", command=self.start_compression
        )
        button.pack(pady=10)

    def start_compression(self):
        # Na tym etapie można zintegrować wywołanie funkcji kompresji
        print("Kompresja rozpoczęta")
