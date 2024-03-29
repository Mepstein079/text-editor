from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename


# Creates the save function to be used later
def save():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output:
        text = editor.get(1.0, tk.END)
        output.write(text)
    text_window.title(f"Entitled - {filepath}")


# User chooses a text file to load, which will delete whatever is currently on the text editor
# Will replace the current contents with the new text file's contents
def load():
    filepath = askopenfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return

    with open(filepath, "r") as file:
        lines = file.read()
        editor.delete(1.0, END)
        editor.insert(INSERT, lines)
    text_window.title(f"Entitled - {filepath}")

    # Calls the word counter function so the word counter stays up to date with the new file
    word_counter()


# Will count the user's words to display them
def word_counter():
    text = editor.get(1.0, END)
    words = text.split()
    word_count_label.config(text=f"Word Count: {len(words)}")

# Will calculate the option's location so the menu can drop below it
def calculate_options_location():
    x = text_window.winfo_rootx() + show_options.winfo_x()
    y = text_window.winfo_rooty() + +show_options.winfo_y() + \
        show_options.winfo_height()
    return x, y


# Will be called to show the option window along with its values
def popup_option_menu(event):

    # Creates the option menu
    option_menu = Menu(text_window, tearoff=0)

    # Creates the commands within the menu
    option_menu.add_command(label="Save", command=save)
    option_menu.add_command(label="Load", command=load)

    # Gets the x and y values
    x, y = calculate_options_location()

    try:
        option_menu.tk_popup(x + 5, y + 5)
    finally:
        option_menu.grab_release()


def on_key_release(event):
    if event.keysym in ("space", "BackSpace", "Delete"):
        word_counter()

# creating the text window
text_window = Tk()
text_window.geometry("600x600")
text_window.title("Matt's Text Editor")


# Creates a button in the text_window to show the option_window
show_options = tk.Button(text_window, text="Options", font=("normal", 10))
show_options.pack(anchor="nw")
show_options.bind("<Button-1>", popup_option_menu)


# Creates the scroll bar on the right side along with the area where the text will be
scroll = Scrollbar(text_window)
scroll.pack(side=RIGHT, fill=Y)
editor = Text(text_window, width=400, height=450, yscrollcommand=scroll.set,
              bg="black", font=("Helvetica", 12), fg="white")
editor.pack(fill=BOTH)
scroll.config(command=editor.yview)


# Area for the user's word count to show
word_count_label = Label(
    text_window, text="Word Count: 0", font=("normal", 10), bg="black", fg="white")
word_count_label.place(relx=0, rely=1, anchor="sw")

# Calls the word_counter function at each key release
editor.bind("<KeyRelease>", on_key_release)

text_window.mainloop()
