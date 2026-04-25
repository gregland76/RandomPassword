import random
import tkinter as tk
import webbrowser
from pathlib import Path


UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
SPECIAL_CHARS = "!@#$%^&*()_+[]{}|;:,.<>?"


def get_random_chars(char_set: str, length: int) -> str:
    return "".join(random.choice(char_set) for _ in range(length))


def generate_password() -> str:
    password = ""
    password += get_random_chars(UPPERCASE, 2)
    password += get_random_chars(DIGITS, 3)
    password += get_random_chars(SPECIAL_CHARS, 2)
    password += get_random_chars(LOWERCASE, 13)

    chars = list(password)
    random.shuffle(chars)
    return "".join(chars)


def generate_passwords(count: int = 10) -> list[str]:
    return [generate_password() for _ in range(count)]


class PasswordGeneratorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.base_dir = Path(__file__).resolve().parent
        self.root.title("Generateur de mots de passe")
        self.root.configure(bg="#e9f0f5")

        self._build_ui()
        self.generate_and_render()

    def _build_ui(self) -> None:
        self.main_card = tk.Frame(
            self.root,
            bg="#ffffff",
            bd=1,
            relief="solid",
            padx=16,
            pady=12,
        )
        self.main_card.pack(padx=10, pady=10, fill="both", expand=True)

        title = tk.Label(
            self.main_card,
            text="GENERATEUR DE MOTS DE PASSE",
            font=("Helvetica", 24, "bold"),
            bg="#ffffff",
            fg="#0f2b46",
        )
        title.pack(pady=(4, 8))

        subtitle = tk.Label(
            self.main_card,
            text="Cliquez pour generer 10 mots de passe robustes",
            font=("Helvetica", 11),
            bg="#ffffff",
            fg="#5a6d7e",
        )
        subtitle.pack(pady=(0, 12))

        generate_btn = tk.Button(
            self.main_card,
            text="Generer des mots de passe",
            command=self.generate_and_render,
            bg="#cfe7ef",
            fg="#0f2b46",
            activebackground="#b9dbe6",
            activeforeground="#0f2b46",
            relief="flat",
            padx=16,
            pady=6,
            font=("Helvetica", 12, "bold"),
            cursor="hand2",
        )
        generate_btn.pack(anchor="center")

        links_row = tk.Frame(self.main_card, bg="#ffffff")
        links_row.pack(pady=(8, 8))

        docs_menu_btn = tk.Menubutton(
            links_row,
            text="Documentation et historique",
            bg="#ecf3f7",
            fg="#0f2b46",
            activebackground="#dceaf2",
            activeforeground="#0f2b46",
            relief="flat",
            padx=12,
            pady=5,
            font=("Helvetica", 10, "bold"),
            cursor="hand2",
            direction="below",
        )
        docs_menu = tk.Menu(docs_menu_btn, tearoff=False)
        docs_menu.add_command(
            label="Documentation",
            command=lambda: self.open_html_doc("documentation.html"),
        )
        docs_menu.add_command(
            label="Historique",
            command=lambda: self.open_html_doc("changelog.html"),
        )
        docs_menu_btn.configure(menu=docs_menu)
        docs_menu_btn.pack(anchor="center")

        self.passwords_container = tk.Frame(self.main_card, bg="#ffffff")
        self.passwords_container.pack(pady=10, fill="both", expand=True)

        footer = tk.Label(
            self.main_card,
            text="© 2025 Generateur de mots de passe. Tous droits reserves.\nCree par Gregory HARGOUS",
            font=("Helvetica", 9),
            bg="#ffffff",
            fg="#7b8793",
            justify="center",
        )
        footer.pack(pady=(6, 0))

    def generate_and_render(self) -> None:
        for widget in self.passwords_container.winfo_children():
            widget.destroy()

        for password in generate_passwords(10):
            row = tk.Frame(self.passwords_container, bg="#ffffff")
            row.pack(anchor="center", pady=4)

            password_label = tk.Label(
                row,
                text=password,
                font=("Courier New", 18, "bold"),
                fg="#0f5132",
                bg="#f3faf6",
                bd=1,
                relief="solid",
                padx=12,
                pady=3,
            )
            password_label.pack(side="left", padx=(0, 10))

            copy_btn = tk.Button(
                row,
                text="Copier",
                bg="#cfe7ef",
                fg="#0f2b46",
                activebackground="#b9dbe6",
                activeforeground="#0f2b46",
                relief="flat",
                padx=12,
                pady=6,
                font=("Helvetica", 11, "bold"),
                cursor="hand2",
                command=lambda p=password, lbl=password_label: self.copy_password(p, lbl),
            )
            copy_btn.pack(side="left")

    def copy_password(self, password: str, label: tk.Label) -> None:
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        label.config(fg="red")
        self.root.after(1000, lambda: label.config(fg="darkgreen"))

    def open_html_doc(self, file_name: str) -> None:
        doc_path = self.base_dir / "docs" / file_name
        if doc_path.exists():
            webbrowser.open(doc_path.resolve().as_uri())


def run() -> None:
    root = tk.Tk()
    window_width = 700
    window_height = 680
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    pos_x = (screen_width - window_width) // 2
    pos_y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")
    root.resizable(False, False)
    PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    run()
