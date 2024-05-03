import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Generador de Contraseñas")
        self.master.geometry("400x300")

        self.password_var = tk.StringVar()

        # Widgets
        tk.Label(master, text="Longitud de la contraseña:").pack()
        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.use_uppercase_var = tk.BooleanVar(value=True)
        self.use_lowercase_var = tk.BooleanVar(value=True)
        self.use_digits_var = tk.BooleanVar(value=True)
        self.use_symbols_var = tk.BooleanVar(value=True)

        tk.Checkbutton(master, text="Mayúsculas", variable=self.use_uppercase_var).pack(anchor=tk.W)
        tk.Checkbutton(master, text="Minúsculas", variable=self.use_lowercase_var).pack(anchor=tk.W)
        tk.Checkbutton(master, text="Números", variable=self.use_digits_var).pack(anchor=tk.W)
        tk.Checkbutton(master, text="Símbolos", variable=self.use_symbols_var).pack(anchor=tk.W)

        self.generate_button = tk.Button(master, text="Generar Contraseña", command=self.generate_password)
        self.generate_button.pack()

        self.password_entry = tk.Entry(master, textvariable=self.password_var, state="readonly")
        self.password_entry.pack()

        self.copy_button = tk.Button(master, text="Copiar Contraseña", command=self.copy_password)
        self.copy_button.pack()

        self.passwords_label = tk.Label(master, text="Contraseñas generadas:")
        self.passwords_label.pack()

        self.password_listbox = tk.Listbox(master, selectmode=tk.SINGLE)
        self.password_listbox.pack()

        self.delete_button = tk.Button(master, text="Borrar Contraseña", command=self.delete_password)
        self.delete_button.pack()

        self.passwords = []

    def generate_password(self):
        length = int(self.length_entry.get())
        use_uppercase = self.use_uppercase_var.get()
        use_lowercase = self.use_lowercase_var.get()
        use_digits = self.use_digits_var.get()
        use_symbols = self.use_symbols_var.get()

        characters = ''
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Debe seleccionar al menos un conjunto de caracteres.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)
        self.passwords.append(password)
        self.password_listbox.insert(tk.END, password)

    def copy_password(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.password_var.get())
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")

    def delete_password(self):
        selection = self.password_listbox.curselection()
        if selection:
            index = selection[0]
            deleted_password = self.password_listbox.get(index)
            self.password_listbox.delete(index)
            self.passwords.remove(deleted_password)
        else:
            messagebox.showerror("Error", "Seleccione una contraseña para borrar.")
def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "_main_":
    main()