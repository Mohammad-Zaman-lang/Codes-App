# 38
import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Display
        self.display = tk.Entry(master, width=25, borderwidth=5, state='readonly')
        self.display.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(master)
        button_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 0
        col = 0
        for button_text in buttons:
            button = ttk.Button(button_frame, text=button_text, width=5, command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        clear_button = ttk.Button(button_frame, text="C", width=5, command=self.clear_display)
        clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Equals button spans two columns
        equals_button = ttk.Button(button_frame, text="=", width=5, command=self.calculate)
        equals_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

        self.current_expression = ""

    def button_click(self, text):
        if text == '=':
            self.calculate()
        else:
            self.current_expression += text
            self.display.config(state='normal')
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_expression)
            self.display.config(state='readonly')

    def calculate(self):
        try:
            result = str(eval(self.current_expression))
            self.display.config(state='normal')
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.display.config(state='readonly')
            self.current_expression = result
        except Exception as e:
            self.display.config(state='normal')
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.display.config(state='readonly')
            self.current_expression = ""

    def clear_display(self):
        self.current_expression = ""
        self.display.config(state='normal')
        self.display.delete(0, tk.END)
        self.display.config(state='readonly')

# Create the main window and run the app
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
