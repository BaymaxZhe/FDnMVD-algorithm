# advdependency_gui.py

import tkinter as tk
from tkinter import messagebox
from advdependency import FunctionalDependency, MultivaluedDependency, compute_fd_closure, compute_mvd_closure, decide_fd_implication, decide_mvd_implication, generate_random_fd, generate_random_mvd

class DependencyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dependency Basis and Implication Problem")

        self.label = tk.Label(master, text="Functional and Multivalued Dependency Analyzer")
        self.label.pack()

        self.fd_button = tk.Button(master, text="Generate Random FDs", command=self.generate_fds)
        self.fd_button.pack()

        self.mvd_button = tk.Button(master, text="Generate Random MVDs", command=self.generate_mvds)
        self.mvd_button.pack()

        self.compute_fd_closure_button = tk.Button(master, text="Compute FD Closure", command=self.compute_fd_closure)
        self.compute_fd_closure_button.pack()

        self.compute_mvd_closure_button = tk.Button(master, text="Compute MVD Closure", command=self.compute_mvd_closure)
        self.compute_mvd_closure_button.pack()

        self.decide_fd_implication_button = tk.Button(master, text="Decide FD Implication", command=self.decide_fd_implication)
        self.decide_fd_implication_button.pack()

        self.decide_mvd_implication_button = tk.Button(master, text="Decide MVD Implication", command=self.decide_mvd_implication)
        self.decide_mvd_implication_button.pack()

        self.result_text = tk.Text(master, height=15, width=50)
        self.result_text.pack()

        self.fd_set = []
        self.mvd_set = []

    def generate_fds(self):
        num_attributes = 5
        num_fds = 5
        self.fd_set = generate_random_fd(num_attributes, num_fds)
        self.result_text.insert(tk.END, "Generated FDs:\n")
        for fd in self.fd_set:
            self.result_text.insert(tk.END, f"{fd.left_hand_side} -> {fd.right_hand_side}\n")
        self.result_text.insert(tk.END, "\n")

    def generate_mvds(self):
        num_attributes = 5
        num_mvds = 5
        self.mvd_set = generate_random_mvd(num_attributes, num_mvds)
        self.result_text.insert(tk.END, "Generated MVDs:\n")
        for mvd in self.mvd_set:
            self.result_text.insert(tk.END, f"{mvd.left_hand_side} ->> {mvd.right_hand_side}\n")
        self.result_text.insert(tk.END, "\n")

    def compute_fd_closure(self):
        if not self.fd_set:
            messagebox.showerror("Error", "No FDs generated")
            return
        closure = compute_fd_closure(self.fd_set, ['A'])
        self.result_text.insert(tk.END, f"FD Closure of ['A']: {closure}\n\n")

    def compute_mvd_closure(self):
        if not self.mvd_set:
            messagebox.showerror("Error", "No MVDs generated")
            return
        closure = compute_mvd_closure(self.mvd_set, ['A'])
        self.result_text.insert(tk.END, f"MVD Closure of ['A']: {closure}\n\n")

    def decide_fd_implication(self):
        if not self.fd_set:
            messagebox.showerror("Error", "No FDs generated")
            return
        fd = FunctionalDependency(['A'], ['C'])
        result = decide_fd_implication(self.fd_set, fd)
        self.result_text.insert(tk.END, f"FD Implication ['A'] -> ['C']: {result}\n\n")

    def decide_mvd_implication(self):
        if not self.mvd_set:
            messagebox.showerror("Error", "No MVDs generated")
            return
        mvd = MultivaluedDependency(['A'], ['C'])
        result = decide_mvd_implication(self.mvd_set, mvd)
        self.result_text.insert(tk.END, f"MVD Implication ['A'] ->> ['C']: {result}\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    gui = DependencyGUI(root)
    root.mainloop()
