import customtkinter as ctk


class SidebarButton(ctk.CTkButton):
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(parent, text=text, command=command, **kwargs)
        self.configure(
            fg_color="#2b2b2b",  # Ciemne tło
            hover_color="#3a3a3a",  # Kolor przy najechaniu
            text_color="white",
            font=("Arial", 14),
            corner_radius=5,
        )
