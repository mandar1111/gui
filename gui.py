import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Python rocks!", foreground="white", background="black", width=15, height=3)
greeting.pack()

signin_button = tk.Button(text= "sign in", width=25, height=5,bg="blue",fg="yellow")
signin_button.pack()

name_label= tk.Label(text="Enter your Name:")
name_entry = tk.Entry(fg="yellow", bg="blue", width=50)
name_label.pack()
name_entry.pack()
window. mainloop()

