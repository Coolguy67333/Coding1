import tkinter as tk
from tkinter import ttk, messagebox

class ResturantOrderManagment:
    def __init(self, root):
        self.root = root
        self.root.title("Resturant Managemnt App")

        self.menu_items = {
            "FRIES MEAL":2,
            "LUNCH MEAL":2,
            "BURGER MEAL":3,
            "PIZZA MEAL":4,
            "DRINKS":1        }

        self.exchange_rate = 82
        self.setup_background(root)

        frame = ttk.frame(root)
        frame.place(relx=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Resturant Order Management"
            font=("Times New Roman", 20, "bold")
        ).grid(row=0, columspan = 3, padx=10, pady=10)

        self.menu_labels = {}

        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1)

            label = ttk.Label(
                frame,
                text=f"{item} (${price})"
                font=("Times New Roman", 12)
            )
            label 
                