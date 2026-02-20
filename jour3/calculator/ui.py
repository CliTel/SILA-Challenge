import tkinter as tk
from tkinter import messagebox
from calculator.logic import safe_calculate
from calculator.theme import apply_dark_theme, apply_light_theme


class ScientificCalculatorUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice Scientifique")
        self.root.geometry("600x700")

        self.expression = ""
        self.dark_mode = False

        self.create_widgets()

    def create_widgets(self):

        self.display = tk.Entry(self.root, font=("Arial", 22), justify="right")
        self.display.pack(fill="both", padx=10, pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        buttons = [
            "7", "8", "9", "/", "sin",
            "4", "5", "6", "*", "cos",
            "1", "2", "3", "-", "tan",
            "0", ".", "pi", "+", "log",
            "(", ")", "e", "C", "=",
            "sqrt", "^", "Theme"
        ]

        row = 0
        col = 0

        for btn in buttons:
            tk.Button(
                btn_frame,
                text=btn,
                width=8,
                height=2,
                command=lambda x=btn: self.on_click(x)
            ).grid(row=row, column=col)

            col += 1
            if col > 4:
                col = 0
                row += 1

        self.history = tk.Text(self.root, height=8)
        self.history.pack(fill="both", expand=True)

    def on_click(self, value):

        if value == "=":
            self.calculate()

        elif value == "C":
            self.expression = ""
            self.display.delete(0, tk.END)

        elif value == "Theme":
            self.toggle_theme()

        elif value == "^":
            self.expression += "**"
            self.display.insert(tk.END, "^")

        elif value in ["sin", "cos", "tan", "log", "sqrt"]:
            self.expression += f"{value}("
            self.display.insert(tk.END, value + "(")

        elif value == "pi":
            self.expression += "pi"
            self.display.insert(tk.END, "π")

        elif value == "e":
            self.expression += "e"
            self.display.insert(tk.END, "e")

        else:
            self.expression += value
            self.display.insert(tk.END, value)

    def calculate(self):
        try:
            result = safe_calculate(self.expression)

            self.history.insert(tk.END, self.display.get() + " = " + str(result) + "\n")

            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))

            self.expression = str(result)

        except ZeroDivisionError:
            messagebox.showerror("Erreur", "Division par zéro")

        except Exception:
            messagebox.showerror("Erreur", "Expression invalide")

    def toggle_theme(self):
        if not self.dark_mode:
            apply_dark_theme(self)
            self.dark_mode = True
        else:
            apply_light_theme(self)
            self.dark_mode = False