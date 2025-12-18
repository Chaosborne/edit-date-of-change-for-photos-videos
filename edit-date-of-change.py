#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime

# ========= DnD =========
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    TKDND_AVAILABLE = True
except ImportError:
    TKDND_AVAILABLE = False


# ========= ОСНОВНОЙ КЛАСС =========
class FileDateChanger(TkinterDnD.Tk if TKDND_AVAILABLE else tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Изменение даты файла")
        self.geometry("520x420")

        self.current_file = None

        self._build_ui()

    # ---------- UI ----------
    def _build_ui(self):
        main = ttk.Frame(self, padding=20)
        main.pack(fill=tk.BOTH, expand=True)

        # ---- Файл ----
        ttk.Label(main, text="Файл:").pack(anchor=tk.W)

        self.file_label = ttk.Label(
            main,
            text="Перетащите файл сюда или выберите вручную",
            relief="solid",
            padding=10
        )
        self.file_label.pack(fill=tk.X, pady=10)

        if TKDND_AVAILABLE:
            self.file_label.drop_target_register(DND_FILES)
            self.file_label.dnd_bind("<<Drop>>", self._on_drop)

        ttk.Button(
            main,
            text="Выбрать файл",
            command=self._select_file
        ).pack(pady=(0, 20))

        # ---- Дата ----
        self._create_date_widgets(main)

        # ---- Кнопка ----
        ttk.Button(
            main,
            text="Изменить дату файла",
            command=self.change_file_date
        ).pack(pady=20)

    # ---------- DATE WIDGETS ----------
    def _create_date_widgets(self, parent):
        now = datetime.now()

        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X)

        def spin(label, frm, to, value, col):
            ttk.Label(frame, text=label).grid(row=0, column=col, sticky=tk.W)
            var = tk.StringVar(value=str(value))
            ttk.Spinbox(frame, from_=frm, to=to, width=5, textvariable=var)\
                .grid(row=1, column=col, padx=5)
            return var

        self.year = spin("Год", 1900, 2100, now.year, 0)
        self.month = spin("Месяц", 1, 12, now.month, 1)
        self.day = spin("День", 1, 31, now.day, 2)
        self.hour = spin("Час", 0, 23, now.hour, 3)
        self.minute = spin("Минута", 0, 59, now.minute, 4)
        self.second = spin("Секунда", 0, 59, now.second, 5)

    # ---------- FILE SELECT ----------
    def _select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self._set_file(path)

    def _on_drop(self, event):
        path = event.data.strip("{}")
        if os.path.isfile(path):
            self._set_file(path)

    def _set_file(self, path):
        self.current_file = path
        self.file_label.config(text=path)

    # ---------- CORE LOGIC ----------
    def change_file_date(self):
        if not self.current_file:
            messagebox.showerror("Ошибка", "Файл не выбран")
            return

        try:
            dt = datetime(
                int(self.year.get()),
                int(self.month.get()),
                int(self.day.get()),
                int(self.hour.get()),
                int(self.minute.get()),
                int(self.second.get()),
            )

            ts = dt.timestamp()
            os.utime(self.current_file, (ts, ts))

            messagebox.showinfo("Готово", "Дата изменения файла обновлена")

        except ValueError:
            messagebox.showerror("Ошибка", "Некорректная дата")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


# ========= START =========
if __name__ == "__main__":
    app = FileDateChanger()
    app.mainloop()
