import tkinter as tk
import math
from math import sqrt 
window = tk.Tk()
window.title("Calculator GUI")
window.geometry("300x540")
window.resizable(False, False)
entry = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right",
    )
entry.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
def click(number):
    entry.insert(tk.END, number)
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        history.append(f"{expression} = {result}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def clear():
    entry.delete(0, tk.END)
def delete_one():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])
def square_root():
    try:
        number = float(entry.get())
        result = sqrt(number)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def show_history():
    history_window = tk.Toplevel(window)
    history_window.title("History")

    text = tk.Text(history_window, font=("Arial", 14))
    text.pack()

    for item in history:
        text.insert(tk.END, item + "\n")
    
button1 = tk.Button(
    window,
    text="1",
    font=("Arial", 20),
    command=lambda: click("1")
    )
button1.grid(row=1, column=0, sticky="nsew")
button1.bind("<Enter>", lambda e: button1.config(bg="lightblue"))
button1.bind("<Leave>", lambda e: button1.config(bg="SystemButtonFace"))


button2 = tk.Button(
    window,
    text="2",
    font=("Arial", 20),
    command=lambda: click("2")
    )
button2.grid(row=1, column=1, sticky="nsew")
button2.bind("<Enter>", lambda e: button2.config(bg="lightblue"))
button2.bind("<Leave>", lambda e: button2.config(bg="SystemButtonFace"))

button3 = tk.Button(
    window,
    text="3",
    font=("Arial", 20),
    command=lambda: click("3")
    )
button3.grid(row=1, column=2, sticky="nsew")
button3.bind("<Enter>", lambda e: button3.config(bg="lightblue"))
button3.bind("<Leave>", lambda e: button3.config(bg="SystemButtonFace"))

button4 = tk.Button(
    window,
    text="4",
    font=("Arial", 20),
    command=lambda: click("4")
    )
button4.grid(row=2, column=0, sticky="nsew")
button4.bind("<Enter>", lambda e: button4.config(bg="lightblue"))
button4.bind("<Leave>", lambda e: button4.config(bg="SystemButtonFace"))

button5 = tk.Button(
    window,
    text="5",
    font=("Arial", 20),
    command=lambda: click("5")
    )
button5.grid(row=2, column=1, sticky="nsew")
button5.bind("<Enter>", lambda e: button5.config(bg="lightblue"))
button5.bind("<Leave>", lambda e: button5.config(bg="SystemButtonFace"))

button6 = tk.Button(
    window,
    text="6",
    font=("Arial", 20),
    command=lambda: click("6")
    )
button6.grid(row=2, column=2, sticky="nsew")
button6.bind("<Enter>", lambda e: button6.config(bg="lightblue"))
button6.bind("<Leave>", lambda e: button6.config(bg="SystemButtonFace"))

button7 = tk.Button(
    window,
    text="7",
    font=("Arial", 20),
    command=lambda: click("7")
    )
button7.grid(row=3, column=0, sticky="nsew")
button7.bind("<Enter>", lambda e: button7.config(bg="lightblue"))
button7.bind("<Leave>", lambda e: button7.config(bg="SystemButtonFace"))

button8 = tk.Button(
    window,
    text="8",
    font=("Arial", 20),
    command=lambda: click("8")
    )
button8.grid(row=3, column=1, sticky="nsew")
button8.bind("<Enter>", lambda e: button8.config(bg="lightblue"))
button8.bind("<Leave>", lambda e: button8.config(bg="SystemButtonFace"))

button9 = tk.Button(
    window,
    text="9",
    font=("Arial", 20),
    command=lambda: click("9")
    )
button9.grid(row=3, column=2, sticky="nsew")
button9.bind("<Enter>", lambda e: button9.config(bg="lightblue"))
button9.bind("<Leave>", lambda e: button9.config(bg="SystemButtonFace"))

button0 = tk.Button(
    window,
    text="0",
    font=("Arial", 20),
    command=lambda: click("0")
    )
button0.grid(row=4, column=0, sticky="nsew")
button0.bind("<Enter>", lambda e: button0.config(bg="lightblue"))
button0.bind("<Leave>", lambda e: button0.config(bg="SystemButtonFace"))


button_plus = tk.Button(
    window,
    text="+",
    font=("Arial", 20),
    command=lambda: click("+")
)
button_plus.grid(row=4, column=1, sticky="nsew")

button_equal = tk.Button(
    window,
    text="=",
    font=("Arial", 20),
    command=calculate
)
button_equal.grid(row=4, column=2, sticky="nsew")
button_clear = tk.Button(
    window,
    text="c",
    font=("Arial", 20),
    command=clear
)
button_clear.grid(row=6, column=1, sticky="nsew")
button_minus = tk.Button(
    window, 
    text="-",
    font=("Arial", 20),
    command=lambda: click("-")
)
button_minus.grid(row=5, column=0, sticky="nsew")
button_multiply = tk.Button(
    window,
    text="*",
    font=("Arial", 20),
    command=lambda: click("*")
)
button_multiply.grid(row=5, column=1, sticky="nsew")
button_divide = tk.Button(
    window,
    text="/",
    font=("Arial", 20),
    command=lambda: click("/")
)
button_divide.grid(row=5, column=2, sticky="nsew")
button_percent = tk.Button(
    window,
    text="%",
    font=("Arial", 20),
    command=lambda: click("%")
    
)
button_percent.grid(row=7, column=0, sticky="nsew")
button_sqrt = tk.Button(
    window,
    text="√",
    font=("Arial", 20),
    command=square_root
)

button_sqrt.grid(row=7, column=1, sticky="nsew")
button_history = tk.Button(
    window,
    text="History",
    font=("Arial", 20),
    command=show_history
)

button_history.grid(row=7, column=2, sticky="nsew")
button_delete = tk.Button(
    window,
    text="⌫",
    font=("Arial", 20),
    command=delete_one
)
button_delete.grid(row=6, column=2, sticky="nsew")
button_dot = tk.Button(
    window,
    text=".",
    font=("Arial", 20),
    command =lambda: click(".")
)
button_dot.grid(row=6, column=0, sticky="nsew")
def key_press(event):
    key = event.char 
    if key in "0123456789+-*/":
        click(key)
        return "break"
    elif event.keysym == "Return":
        calculate()
        return "break"
    elif event.keysym == "BackSpace":
        delete_one()
        return "break"
entry.bind("<Key>", key_press)   
operations = [
    button_plus,
    button_minus,
    button_multiply,
    button_divide,
    button_percent,
    button_sqrt,
    button_history,
    button_equal,
    button_clear,
    button_delete,
    button_dot
] 
for btn in operations:
    btn.bind("<Enter>", lambda e, b=btn: b.config(bg="lightblue"))
    btn.bind("<Leave>", lambda e, b=btn: b.config(bg="SystemButtonFace"))
def square_root():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error") 
history = []  
window.grid_rowconfigure(0, weight=0)
for i in range(1, 8):
    window.grid_rowconfigure(i, weight=1, uniform="rows")

for i in range(3):
    window.grid_columnconfigure(i, weight=1, uniform="cols") 
window.mainloop()