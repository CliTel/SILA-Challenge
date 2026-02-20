import tkinter as tk
from calculator.ui import ScientificCalculatorUI

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculatorUI(root)
    root.mainloop()