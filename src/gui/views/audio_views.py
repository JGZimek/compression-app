import customtkinter as ctk
from tkinter import filedialog, messagebox
import os


class AudioCompressionView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.file_path = None
        self.original_audio = None
        self.compressed_audio = None
        self.create_widgets()

    def create_widgets(self):
        header_label = ctk.CTkLabel(self, text="Kompresja Audio", font=("Arial", 20))
        header_label.pack(pady=20)

        audio_btn = ctk.CTkButton(
            self, text="Wczytaj plik audio", command=self.load_audio_file
        )
        audio_btn.pack(pady=10)

        # Kontener na dwa panele: oryginał (lewym) oraz wynik po kompresji (prawym)
        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.pack(fill="both", expand=True, pady=10)
        self.display_frame.grid_rowconfigure(0, weight=1)
        self.display_frame.grid_columnconfigure(0, weight=1)
        self.display_frame.grid_columnconfigure(1, weight=1)

        self.original_frame = ctk.CTkFrame(self.display_frame)
        self.original_frame.grid(row=0, column=0, sticky="nsew", padx=5)
        self.compressed_frame = ctk.CTkFrame(self.display_frame)
        self.compressed_frame.grid(row=0, column=1, sticky="nsew", padx=5)

        # Ustalamy, aby panele nie zmieniały swoich rozmiarów względem dzieci
        self.original_frame.grid_propagate(False)
        self.compressed_frame.grid_propagate(False)
        self.display_frame.bind("<Configure>", self.resize_panels)

        # Tytuły paneli
        orig_title = ctk.CTkLabel(self.original_frame, text="Oryginał")
        orig_title.place(relx=0.5, rely=0.1, anchor="n")
        comp_title = ctk.CTkLabel(self.compressed_frame, text="Po kompresji")
        comp_title.place(relx=0.5, rely=0.1, anchor="n")

        # Panel opcji kompresji poniżej panelu wyświetlania
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=10)
        method_label = ctk.CTkLabel(
            self.options_frame, text="Wybierz metodę kompresji:"
        )
        method_label.grid(row=0, column=0, padx=10, pady=5)
        self.method_optionmenu = ctk.CTkOptionMenu(
            self.options_frame, values=["Metoda A1", "Metoda A2", "Metoda A3"]
        )
        self.method_optionmenu.grid(row=0, column=1, padx=10, pady=5)
        param_label = ctk.CTkLabel(self.options_frame, text="Parametr kompresji:")
        param_label.grid(row=1, column=0, padx=10, pady=5)
        self.param_entry = ctk.CTkEntry(self.options_frame)
        self.param_entry.grid(row=1, column=1, padx=10, pady=5)
        compress_btn = ctk.CTkButton(
            self.options_frame, text="Kompresuj", command=self.start_compression
        )
        compress_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def resize_panels(self, event):
        panel_width = (event.width - 10) / 2
        panel_height = event.height
        self.original_frame.configure(width=panel_width, height=panel_height)
        self.compressed_frame.configure(width=panel_width, height=panel_height)

    def load_audio_file(self):
        file_path = filedialog.askopenfilename(
            title="Wybierz plik audio",
            filetypes=[("Pliki audio", "*.wav *.mp3"), ("Wszystkie pliki", "*.*")],
        )
        if file_path:
            self.file_path = file_path
            messagebox.showinfo("Plik audio", f"Wczytano plik audio:\n{file_path}")
            self.display_original_audio()
            # Wyczyść panel po kompresji
            for widget in self.compressed_frame.winfo_children():
                if not (
                    isinstance(widget, ctk.CTkLabel)
                    and widget.cget("text") == "Po kompresji"
                ):
                    widget.destroy()

    def display_original_audio(self):
        for widget in self.original_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "Oryginał":
                continue
            widget.destroy()
        orig_text = f"Oryginał: {os.path.basename(self.file_path)}"
        label = ctk.CTkLabel(self.original_frame, text=orig_text)
        label.place(relx=0.5, rely=0.5, anchor="center")

    def start_compression(self):
        if self.file_path:
            self.compressed_audio = self.file_path  # placeholder – symulacja kompresji
            self.display_compressed_audio()
            messagebox.showinfo("Kompresja", "Kompresja audio zakończona (symulacja).")

    def display_compressed_audio(self):
        for widget in self.compressed_frame.winfo_children():
            if (
                isinstance(widget, ctk.CTkLabel)
                and widget.cget("text") == "Po kompresji"
            ):
                continue
            widget.destroy()
        comp_text = f"Po kompresji: {os.path.basename(self.file_path)}"
        label = ctk.CTkLabel(self.compressed_frame, text=comp_text)
        label.place(relx=0.5, rely=0.5, anchor="center")
