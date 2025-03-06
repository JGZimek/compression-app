import customtkinter as ctk
from tkinter import filedialog, messagebox


class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Etykieta powitalna
        label = ctk.CTkLabel(
            self, text="Wczytaj plik sygnału audio lub obraz", font=("Arial", 20)
        )
        label.pack(pady=20)

        # Przycisk do wczytania pliku audio
        audio_btn = ctk.CTkButton(
            self, text="Wczytaj plik audio", command=self.load_audio_file
        )
        audio_btn.pack(pady=10)

        # Przycisk do wczytania pliku obrazu
        image_btn = ctk.CTkButton(
            self, text="Wczytaj plik obrazu", command=self.load_image_file
        )
        image_btn.pack(pady=10)

    def load_audio_file(self):
        # Użycie filedialog do wyboru pliku audio (np. wav, mp3)
        file_path = filedialog.askopenfilename(
            title="Wybierz plik audio",
            filetypes=[("Pliki audio", "*.wav *.mp3"), ("Wszystkie pliki", "*.*")],
        )
        if file_path:
            # Tutaj możesz wczytać plik np. używając biblioteki wave lub pydub
            print(f"Wybrano plik audio: {file_path}")
            messagebox.showinfo("Plik audio", f"Wczytano plik audio:\n{file_path}")

    def load_image_file(self):
        # Użycie filedialog do wyboru pliku obrazu (np. jpg, png)
        file_path = filedialog.askopenfilename(
            title="Wybierz plik obrazu",
            filetypes=[
                ("Pliki obrazów", "*.jpg *.jpeg *.png"),
                ("Wszystkie pliki", "*.*"),
            ],
        )
        if file_path:
            # Tutaj możesz wczytać obraz np. przy użyciu biblioteki Pillow
            print(f"Wybrano plik obrazu: {file_path}")
            messagebox.showinfo("Plik obrazu", f"Wczytano plik obrazu:\n{file_path}")
