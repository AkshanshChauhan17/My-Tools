import tkinter as tk

win = tk.Tk()

win.title("Document Scanner")
win.geometry("600x400")

label = tk.Label(win, text="Document Scanner")
label.pack(pady=10, padx=10)

button = tk.Button(win, text="Button", command=lambda: label.config(text="Button Clicked"))
button.pack()

win.mainloop()