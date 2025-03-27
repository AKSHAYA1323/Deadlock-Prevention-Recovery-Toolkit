import tkinter as tk
from tkinter import Toplevel, messagebox
import ttkbootstrap as tb
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.deadlock_detection import detect_deadlock  
from src.deadlock_prevention import is_safe  
from src.deadlock_recovery import recover_deadlock  

class DeadlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Prevention & Recovery Toolkit")
        self.root.geometry("1200x800")  
        self.style = tb.Style("darkly")  

        # 📌 **Opening Page with Information**
        self.intro_frame = tb.Frame(root, padding=50)
        self.intro_frame.pack(fill="both", expand=True, pady=(30, 10))

        tb.Label(self.intro_frame, text="🔗 Deadlock Prevention & Recovery Toolkit", font=("Arial", 20, "bold")).pack(pady=10)
        tb.Label(self.intro_frame, text="This toolkit helps in detecting, preventing, and recovering from deadlocks in a system.", font=("Courier New", 12)).pack(pady=5)
        tb.Label(self.intro_frame, text="Features:\n - Deadlock Detection\n - Deadlock Prevention using Banker's Algorithm\n - Deadlock Recovery", font=("Courier New", 12), justify="left").pack(pady=5)
        
        tb.Label(self.intro_frame, text="🔽 Enter the details below to analyze deadlocks 🔽", font=("Courier New", 14, "bold")).pack(pady=10)

        # 📌 **Input Section**
        self.input_frame = tb.Frame(root, padding=30)
        self.input_frame.pack(fill="x", anchor="w", padx=20,pady=(0, 10))  # Aligns input frame to the left

        entry_width = 30
        tb.Label(self.input_frame, text="Number of Processes:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.num_processes_entry = tb.Entry(self.input_frame,width=entry_width)
        self.num_processes_entry.grid(row=0, column=1,padx=5, pady=5)

        tb.Label(self.input_frame, text="Number of Resources:").grid(row=1, column=0,sticky="w", padx=5, pady=5)
        self.num_resources_entry = tb.Entry(self.input_frame,width=entry_width)
        self.num_resources_entry.grid(row=1, column=1,padx=5, pady=5)

        tb.Label(self.input_frame, text="Allocation Matrix (comma-separated rows):").grid(row=2, column=0,sticky="w", padx=5, pady=5)
        self.allocation_entry = tb.Entry(self.input_frame, width=entry_width)
        self.allocation_entry.grid(row=2, column=1,padx=5, pady=5)

        tb.Label(self.input_frame, text="Max Demand Matrix (comma-separated rows):").grid(row=3, column=0,sticky="w", padx=5, pady=5)
        self.max_demand_entry = tb.Entry(self.input_frame, width=entry_width)
        self.max_demand_entry.grid(row=3, column=1,padx=5, pady=5)

        tb.Label(self.input_frame, text="Available Resources:").grid(row=4, column=0,sticky="w", padx=5, pady=5)
        self.available_entry = tb.Entry(self.input_frame,width=entry_width)
        self.available_entry.grid(row=4, column=1,padx=5, pady=5)

        # 📌 **Buttons**
        self.button_frame = tb.Frame(root, padding=10)
        self.button_frame.pack()

        tb.Button(self.button_frame, text="Run Detection", command=self.run_detection, bootstyle="warning").grid(row=0, column=1, padx=5)
        tb.Button(self.button_frame, text="Run Prevention", command=self.run_prevention, bootstyle="success").grid(row=0, column=2, padx=5)
        tb.Button(self.button_frame, text="Run Recovery", command=self.run_recovery, bootstyle="danger").grid(row=0, column=3, padx=5)

    def get_input_data(self):
        try:
            num_processes = int(self.num_processes_entry.get())
            num_resources = int(self.num_resources_entry.get())
            allocation = [list(map(int, row.split(','))) for row in self.allocation_entry.get().split()]
            max_demand = [list(map(int, row.split(','))) for row in self.max_demand_entry.get().split()]
            available = list(map(int, self.available_entry.get().split(',')))
            processes = [f"P{i+1}" for i in range(num_processes)]
            resources = [f"R{i+1}" for i in range(num_resources)]
            return processes, resources, allocation, max_demand, available
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input! Please enter correct values.")
            return None, None, None, None, None

    def run_detection(self):
        processes, resources, allocation, max_demand, available = self.get_input_data()
        if not processes:
            return
        
        deadlocked_processes = detect_deadlock(processes, allocation, max_demand, available)
        if deadlocked_processes:
            messagebox.showwarning("Deadlock Detected", f"⚠️ Deadlocked Processes: {deadlocked_processes}")
        else:
            messagebox.showinfo("Result", "✅ No Deadlock Detected.")

        self.show_graph_window(processes, resources, allocation, deadlocked_processes)

    def run_prevention(self):
        processes, resources, allocation, max_demand, available = self.get_input_data()
        if not processes:
            return
        safe, safe_sequence = is_safe(processes, allocation, max_demand, available)
        if safe:
            messagebox.showinfo("Result", f"✅ Safe Sequence Found: {safe_sequence}")
        else:
            messagebox.showwarning("Deadlock Risk", "❌ No Safe Sequence Found!")

        self.show_graph_window(processes, resources, allocation)

    def run_recovery(self):
        processes, resources, allocation, max_demand, available = self.get_input_data()
        if not processes:
            return
        deadlocked_processes = detect_deadlock(processes, allocation, max_demand, available)
        if deadlocked_processes:
            available, message = recover_deadlock(deadlocked_processes, allocation, available)
            messagebox.showinfo("Recovery", message)
        else:
            messagebox.showinfo("Result", "✅ No Deadlock to Recover.")

        self.show_graph_window(processes, resources, allocation, deadlocked_processes)

    def show_graph_window(self, processes, resources, allocation, deadlocked_processes=[]):
        graph_window = Toplevel(self.root)
        graph_window.title("Deadlock Graph Visualization")
        graph_window.geometry("1000x700")

        G = nx.DiGraph()

        # Add process and resource nodes
        for process in processes:
            G.add_node(process, color="skyblue")

        for resource in resources:
            G.add_node(resource, color="lightgreen")

        # Add edges based on allocation
        for i, process in enumerate(processes):
            for j, resource in enumerate(resources):
                if allocation[i][j] > 0:
                    G.add_edge(resource, process, label=f"Allocated {allocation[i][j]}")
                else:
                    G.add_edge(process, resource, label=f"Requested 1")

        # Colors
        colors = ["red" if node in deadlocked_processes else "skyblue" if node in processes else "lightgreen" for node in G.nodes]

        fig, ax = plt.subplots(figsize=(10, 8))
        pos = nx.spring_layout(G, k=0.8)  
        nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2000, edge_color="black", font_size=12, ax=ax)

        labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tb.Window(themename="darkly")  
    app = DeadlockGUI(root)
    root.mainloop()
