import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, font

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, font=("Arial", 12))
        self.text_area.pack(fill="both", expand=True)

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open...", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.format_menu.add_command(label="Font...", command=self.change_font)
        self.format_menu.add_command(label="Color...", command=self.change_color)
        self.format_menu.add_command(label="Background...", command=self.change_background)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)

        self.root.config(menu=self.menu_bar)

        self.font_dialog = font.Font(family="Arial", size=12)
        self.text_area.config(font=self.font_dialog)

        self.color_dialog = colorchooser.askcolor(title="Choose text color")[1]
        self.text_area.config(fg=self.color_dialog)

        self.background_dialog = colorchooser.askcolor(title="Choose background color")[1]
        self.text_area.config(bg=self.background_dialog)

    def new_file(self):
        self.text_area.delete(1.0, "end")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, "end")
                self.text_area.insert("end", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end-1c"))

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end-1c"))

    def cut(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
        self.text_area.delete("sel.first", "sel.last")

    def copy(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste(self):
        self.text_area.insert("insert", self.text_area.clipboard_get())

    def change_font(self):
        font_name = font.askfont()[0]
        self.font_dialog.config(family=font_name)
        self.text_area.config(font=self.font_dialog)

    def change_color(self):
        color = colorchooser.askcolor(title="Choose text color")[1]
        self.text_area.config(fg=color)

    def change_background(self):
        color = colorchooser.askcolor(title="Choose background color")[1]
        self.text_area.config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()