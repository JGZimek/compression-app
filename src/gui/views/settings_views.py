import customtkinter as ctk


class SettingsView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Widok Ustawień", font=("Arial", 20))
        label.pack(pady=20)
        # Dodaj elementy umożliwiające konfigurację aplikacji
