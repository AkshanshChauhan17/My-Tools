import tkinter as tk

win = tk.Tk()

win.title("Document Scanner")
win.geometry("600x400")

label = tk.Label(win, text="Document Scanner")
label.pack(padx=0, pady=0)

button = tk.Button(win, text="Button", cursor="cross", command=lambda: label.config(text="Button Clicked"))
button.pack(ipadx=10, ipady=10, padx=10, pady=10)

win.mainloop()