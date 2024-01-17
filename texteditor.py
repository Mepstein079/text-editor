from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename


# Creates the save function to be used later
def save():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[
                                 ("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output:
        text = editor.get(1.0, tk.END)
        output.write(text)
    text_window.title(f"Entitled - {filepath}")


# creating the text window
text_window = Tk()
text_window.geometry('600x600')
text_window.title("Matt's Text Editor")

# Will create the label for the heading
heading = Label(text_window, text="Text Editor",
                font=('bold', 20), bg='light grey')
heading.pack()

# Creates the scroll bar on the right side along with the area where the text will be
scroll = Scrollbar(text_window)
scroll.pack(side=RIGHT, fill=Y)
editor = Text(text_window, width=400, height=450, yscrollcommand=scroll.set)
editor.pack(fill=BOTH)
scroll.config(command=editor.yview)

# The button where the user can save their text
save_button = Button(text_window, text='Save', font=(
    'normal', 10), command=save, bg='light blue')
save_button.place(x=270, y=520)


text_window.mainloop()
