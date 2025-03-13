import customtkinter as ctk


class HomeView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        header = ctk.CTkLabel(
            self, text="Witamy w Aplikacji Kompresji Danych", font=("Arial", 24)
        )
        header.pack(pady=20)
        # Możesz dodać tu dodatkowe informacje, np. krótką instrukcję lub logo
