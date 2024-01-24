from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename


# Creates the save function to be used later
def save():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[
                                 ("Text Files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "w") as output:
        text = editor.get(1.0, tk.END)
        output.write(text)
    text_window.title(f"Entitled - {filepath}")


# User chooses a text file to load, which will delete whatever is currently on the text editor
# Will replace the current contents with the new text file's contents
def load():
    filepath = askopenfilename(defaultextension="txt", filetypes=[
                               ("Text Files", "*.txt")], )
    if not filepath:
        return

    with open(filepath, "r") as file:
        lines = file.read()
        editor.delete(1.0, END)
        editor.insert(INSERT, lines)
    text_window.title(f"Entitled - {filepath}")


# Will count the user's words to display them
def word_counter():
    text = editor.get(1.0, END)
    words = text.split()
    word_count_label.config(text=f"Word Count: {len(words)}")


# creating the text window
text_window = Tk()
text_window.geometry("600x600")
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
save_button = Button(text_window, text="Save", font=(
    "normal", 10), command=save, bg="light blue")
save_bottom_width = save_button.winfo_reqwidth()
save_button.place(relx=0.45, rely=.9, anchor="s", x=save_bottom_width/2)


# The button to for the user to load their text file
load_button = Button(text_window, text="Load", font=(
    "normal", 10), command=load, bg="red")
load_bottom_width = load_button.winfo_reqwidth()
load_button.place(relx=0.53, rely=0.9, anchor="s", x=load_bottom_width/2)


# Area for the user's word count to show
word_count_label = Label(
    text_window, text="Word Count: 0", font=("normal", 10))
word_count_label.place(relx=0, rely=1, anchor="sw")

# Calls the word_counter function at each key release
editor.bind("<KeyRelease>", lambda event: text_window.after(150, word_counter))

text_window.mainloop()
