import tkinter as tk
from tkinter import filedialog, ttk
import os
import time
import lang_eng

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
if not file_path:
    print("Файл не выбран")
    exit()
print(file_path)

progress_window = tk.Toplevel()
progress_window.title(lang_eng.get("en", "repoopen.title"))
progress_window.geometry("300x100")

progress_label = tk.Label(progress_window, text="Начало открытия файла...")
progress_label.pack()

progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()



steps = ["Проверка версии", "Чтение типа", "Проверка доступа", "Запрос данных", "Обновление библиотеки"]
total_steps = len(steps)
step_size = 100 / total_steps



for step in steps:
    progress_label.config(text=step)
    progress_window.update()
    time.sleep(1)
    progress_bar['value'] += step_size
    progress_window.update()

progress_window.destroy()
print("Файл успешно открыт")