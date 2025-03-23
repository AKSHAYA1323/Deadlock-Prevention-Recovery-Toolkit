import tkinter as tk
from main import main

def run_toolkit():
    output_text.delete(1.0, tk.END)
    result = main()
    output_text.insert(tk.END, result)

root = tk.Tk()
root.title("Deadlock Prevention & Recovery Toolkit")

run_button = tk.Button(root, text="Run Deadlock Toolkit", command=run_toolkit)
run_button.pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
