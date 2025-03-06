import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image  # do przetwarzania obrazów
import os


class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.file_path = None
        self.file_type = None  # "audio" lub "image"
        self.create_widgets()

    def create_widgets(self):
        # Nagłówek
        header_label = ctk.CTkLabel(
            self, text="Wczytaj plik oraz wybierz metodę kompresji", font=("Arial", 20)
        )
        header_label.pack(pady=20)

        # Przyciski do wczytywania plików
        audio_btn = ctk.CTkButton(
            self, text="Wczytaj plik audio", command=self.load_audio_file
        )
        audio_btn.pack(pady=10)

        image_btn = ctk.CTkButton(
            self, text="Wczytaj plik obrazu", command=self.load_image_file
        )
        image_btn.pack(pady=10)

        # Kontener na podgląd wczytanego pliku
        self.preview_frame = ctk.CTkFrame(self)
        self.preview_frame.pack(pady=10, fill="both", expand=True)

        # Panel opcji kompresji (na początku ukryty)
        self.options_frame = ctk.CTkFrame(self)
        # Opcja wyboru metody kompresji
        method_label = ctk.CTkLabel(
            self.options_frame, text="Wybierz metodę kompresji:"
        )
        method_label.grid(row=0, column=0, padx=10, pady=5)

        self.method_optionmenu = ctk.CTkOptionMenu(
            self.options_frame, values=["Metoda 1", "Metoda 2", "Metoda 3"]
        )
        self.method_optionmenu.grid(row=0, column=1, padx=10, pady=5)

        # Pole do podania parametru
        param_label = ctk.CTkLabel(self.options_frame, text="Parametr kompresji:")
        param_label.grid(row=1, column=0, padx=10, pady=5)

        self.param_entry = ctk.CTkEntry(self.options_frame)
        self.param_entry.grid(row=1, column=1, padx=10, pady=5)

        # Przycisk startowy
        start_btn = ctk.CTkButton(
            self.options_frame,
            text="Rozpocznij kompresję",
            command=self.start_compression,
        )
        start_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def load_audio_file(self):
        file_path = filedialog.askopenfilename(
            title="Wybierz plik audio",
            filetypes=[("Pliki audio", "*.wav *.mp3"), ("Wszystkie pliki", "*.*")],
        )
        if file_path:
            self.file_path = file_path
            self.file_type = "audio"
            messagebox.showinfo("Plik audio", f"Wczytano plik audio:\n{file_path}")
            self.display_file_preview()
            self.show_options_frame()

    def load_image_file(self):
        file_path = filedialog.askopenfilename(
            title="Wybierz plik obrazu",
            filetypes=[
                ("Pliki obrazów", "*.jpg *.jpeg *.png"),
                ("Wszystkie pliki", "*.*"),
            ],
        )
        if file_path:
            self.file_path = file_path
            self.file_type = "image"
            messagebox.showinfo("Plik obrazu", f"Wczytano plik obrazu:\n{file_path}")
            self.display_file_preview()
            self.show_options_frame()

    def display_file_preview(self):
        # Czyścimy poprzedni podgląd
        for widget in self.preview_frame.winfo_children():
            widget.destroy()

        if self.file_type == "image":
            try:
                # Załaduj obraz przy użyciu Pillow
                img = Image.open(self.file_path)
                # Zmniejsz obraz, aby pasował do podglądu (maksymalny rozmiar 400x400)
                img.thumbnail((400, 400))
                # Utwórz CTkImage, podając tylko light_image oraz rozmiar
                ctk_img = ctk.CTkImage(light_image=img, size=(img.width, img.height))
                # Wyświetl obraz w etykiecie
                image_label = ctk.CTkLabel(self.preview_frame, image=ctk_img, text="")
                image_label.image = ctk_img  # zachowaj referencję, aby obraz nie został usunięty przez garbage collector
                image_label.pack(pady=10)
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się załadować obrazu:\n{e}")
        elif self.file_type == "audio":
            # Wyświetl podstawowy podgląd pliku audio (np. nazwa pliku)
            filename = os.path.basename(self.file_path)
            audio_label = ctk.CTkLabel(
                self.preview_frame, text=f"Plik audio: {filename}", font=("Arial", 16)
            )
            audio_label.pack(pady=10)

    def show_options_frame(self):
        # Wyświetlamy panel opcji kompresji, jeśli jeszcze nie jest widoczny
        if not self.options_frame.winfo_ismapped():
            self.options_frame.pack(pady=20)

    def start_compression(self):
        # Pobieramy wybrane ustawienia
        method = self.method_optionmenu.get()
        param = self.param_entry.get()

        # W tym miejscu dodaj logikę wywołania odpowiedniego algorytmu kompresji na podstawie self.file_type
        print(f"Rozpoczynam kompresję pliku {self.file_path}")
        print(f"Wybrana metoda: {method}")
        print(f"Podany parametr: {param}")
        messagebox.showinfo(
            "Kompresja",
            f"Kompresja rozpoczęta z metodą '{method}' i parametrem '{param}'.",
        )
