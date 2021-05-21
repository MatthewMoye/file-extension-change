import tkinter as tk
from tkinter import filedialog
import os


def rename(directory, old_extension, new_extension):
    old_extension = old_extension[:-1]
    new_extension = new_extension[:-1]
    if not os.path.isdir(str(directory[:-1])):
        errorMsg.set("Directory does not exist")
        return
    elif old_extension == "" or new_extension == "":
        errorMsg.set("Please populate the extension fields")
        return
    if old_extension[0] != ".":
        old_extension = "." + old_extension
    if new_extension[0] != ".":
        new_extension = "." + new_extension
    errorMsg.set('')
    len_ext = len(old_extension)
    os.chdir(directory[:-1])
    for filename in os.listdir():
        if filename[-len_ext:] == old_extension:
            os.rename(filename, filename.replace(old_extension, new_extension))


# Inserts selected directory into the directory text box
def directory(e):
    e.delete(1.0, tk.END)
    e.insert(tk.END, filedialog.askdirectory())


# Setup window
main = tk.Tk()
main.title("File Extension Change")
main.geometry("600x230")
main.resizable(0, 0)


# Original and End Directory Text
origDir = tk.Text(main, width=60, height=1)


# Pic size
old_extension = tk.Text(main, width=20, height=1)
new_extension = tk.Text(main, width=20, height=1)


# Labels
orDir = tk.Label(main, text="Source Directory")
old_label = tk.Label(main, text="Original Extension:")
new_label = tk.Label(main, text="New Extension:")
global errorMsg
errorMsg = tk.StringVar()
error = tk.Label(main, textvariable=errorMsg, fg="red")


# Buttons
browse1 = tk.Button(
    main, text="Browse", bg="#a6a3a0", command=lambda: directory(origDir)
)
stop = tk.Button(
    main, text="Quit", bg="#a6a3a0", width=10, command=lambda: main.destroy()
)
start = tk.Button(
    main,
    text="Start",
    bg="#a6a3a0",
    width=10,
    command=lambda: rename(
        str(origDir.get(1.0, tk.END)),
        str(old_extension.get(1.0, tk.END)),
        str(new_extension.get(1.0, tk.END)),
    ),
)


# Placements in window
orDir.pack(pady=5)
origDir.pack()
browse1.pack(pady=10)
old_label.place(x=105, y=105)
old_extension.pack(pady=10)
new_label.place(x=122, y=137)
new_extension.pack()
error.place(x=398,y=160)
start.place(x=500, y=180)
stop.place(x=400, y=180)

main.mainloop()
