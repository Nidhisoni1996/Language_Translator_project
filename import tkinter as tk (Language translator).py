import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize translator
translator = Translator()

# Create main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x500")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Language Translator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Input Text
input_label = tk.Label(root, text="Enter Text:")
input_label.pack()
input_text = tk.Text(root, height=6, width=60)
input_text.pack(pady=5)

# Language selection
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="From:").grid(row=0, column=0, padx=10)
tk.Label(frame, text="To:").grid(row=0, column=1, padx=10)

languages = list(LANGUAGES.values())

src_lang = ttk.Combobox(frame, values=languages, width=20)
src_lang.set("english")
src_lang.grid(row=1, column=0, padx=10)

dest_lang = ttk.Combobox(frame, values=languages, width=20)
dest_lang.set("hindi")
dest_lang.grid(row=1, column=1, padx=10)

# Output Text
output_label = tk.Label(root, text="Translated Text:")
output_label.pack()

output_text = tk.Text(root, height=6, width=60, bg="#f0f0f0")
output_text.pack(pady=5)

# Translate function
def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text")
            return

        src = src_lang.get()
        dest = dest_lang.get()

        # Convert language name to code
        src_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(src)]
        dest_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest)]

        translated = translator.translate(text, src=src_code, dest=dest_code)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Translate Button
translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="blue", fg="white")
translate_btn.pack(pady=15)

# Run app
root.mainloop()