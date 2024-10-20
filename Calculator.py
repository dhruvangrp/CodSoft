import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("400x300")

        # Create GUI elements
        self.num1_label = tk.Label(self.master, text="Number 1:")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(self.master, width=15)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_label = tk.Label(self.master, text="Number 2:")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(self.master, width=15)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.operation_label = tk.Label(self.master, text="Operation:")
        self.operation_label.grid(row=2, column=0, padx=5, pady=5)
        self.operation_var = tk.StringVar(self.master)
        self.operation_var.set("+")  # default value
        self.operation_menu = tk.OptionMenu(self.master, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.grid(row=2, column=1, padx=5, pady=5)

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(self.master, text="Result: ")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero")
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
  root = tk.Tk()
  calculator = Calculator(root)
  root.mainloop()
