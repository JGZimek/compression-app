import customtkinter as ctk


class StatisticsView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Widok Statystyk", font=("Arial", 20))
        label.pack(pady=20)
        # Dodaj dodatkowe elementy interfejsu statystyk według potrzeb
