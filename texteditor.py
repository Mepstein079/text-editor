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


# Will count the user's words to display them
def word_counter():
    text = editor.get(1.0, END)
    words = text.split()
    word_count_label.config(text=f"Word Count: {len(words)}")


# Calculates the option's location
def calculate_options_location():
    x = text_window.winfo_rootx() + show_options.winfo_x()
    y = text_window.winfo_rooty() + +show_options.winfo_y() + \
        show_options.winfo_height()
    return x, y


# Will be called to show the Toplevel window where the user can pick new options
def show_option_window():
    # Creates the window
    option_window = tk.Toplevel(text_window)

    # Sets the position, it not being resizable, and not show window manager
    option_window.geometry("+40+55")
    option_window.resizable(False, False)
    option_window.overrideredirect(True)

    option_window.update()

    x, y = calculate_options_location()
    option_window.geometry(f"+{x}+{y}")

    text_window.bind("<Configure>", lambda event: option_window.geometry(
        f"+{calculate_options_location()[0]}+{calculate_options_location()[1]}"))

    # The button where the user can save their text
    save_button = Button(
        option_window, text="Save", font=("normal", 10), command=save
    )
    save_button.pack()

    # The button to for the user to load their text file
    load_button = Button(
        option_window, text="Load", font=("normal", 10), command=load
    )
    load_button.pack()


# creating the text window
text_window = Tk()
text_window.geometry("600x600")
text_window.title("Matt's Text Editor")


# Creates a button in the text_window to show the option_window
show_options = tk.Button(text_window, text="Options",
                         command=show_option_window, font=("normal", 10))
show_options.pack(anchor="nw")

# Creates the scroll bar on the right side along with the area where the text will be
scroll = Scrollbar(text_window)
scroll.pack(side=RIGHT, fill=Y)
editor = Text(text_window, width=400, height=450, yscrollcommand=scroll.set, bg="black", font=("Helvetica", 12), fg="white")
editor.pack(fill=BOTH)
scroll.config(command=editor.yview)


# Area for the user's word count to show
word_count_label = Label(
    text_window, text="Word Count: 0", font=("normal", 10), bg="black", fg="white")
word_count_label.place(relx=0, rely=1, anchor="sw")

# Calls the word_counter function at each key release
editor.bind("<KeyRelease>", lambda event: text_window.after(150, word_counter))

text_window.mainloop()
