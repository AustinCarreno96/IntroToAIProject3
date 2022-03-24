from tkinter import *
from tkinter import ttk
import tkinter as tk


class PyGUI:
    def __init__(self):
        # Make and name TK GUI
        self.root = Tk()
        self.root.title("Project 3 AI")
        self.root.geometry("900x800")


        # Attributes Frame
        self.frm_attributes = tk.Frame(self.root)
        self.frm_attributes.grid(column=0, row=0)
        self.lbl_attributes = tk.Label(self.frm_attributes, text="Binary Attributes", anchor=N)
        self.lbl_attributes.pack()

        # Make tree view table for attributes
        self.tree_attributes = ttk.Treeview(self.frm_attributes, height=10)
        self.tree_attributes['columns'] = ("Attr #", "Attribute", "Option 1", "Option 2")
        self.tree_attributes.column("#0", width=0)
        self.tree_attributes.column("Attr #", width=80, anchor=CENTER)
        self.tree_attributes.column("Attribute", width=80, anchor=W)
        self.tree_attributes.column("Option 1", width=80, anchor=W)
        self.tree_attributes.column("Option 2", width=80, anchor=W)

        # Attribute tree headers
        self.tree_attributes.heading("Attr #", text="Attr #", anchor=CENTER)
        self.tree_attributes.heading("Attribute", text="Attribute", anchor=W)
        self.tree_attributes.heading("Option 1", text="Option 1", anchor=W)
        self.tree_attributes.heading("Option 2", text="Option 2", anchor=W)

        # Show tree
        self.tree_attributes.pack()


        # Constraints Frame
        self.frm_constraints = tk.Frame(self.root)
        self.frm_constraints.grid(column=0, row=1)
        self.lbl_constraints = tk.Label(self.frm_constraints, text="Hard Constraints")
        self.lbl_constraints.pack()

        # Make Constraints tree
        self.tree_constraints = ttk.Treeview(self.frm_constraints, height=10)
        self.tree_constraints['columns'] = ("Const #", "Constraint")
        self.tree_constraints.column("#0", width=0)
        self.tree_constraints.column("Const #", width=80, minwidth=20, anchor=CENTER)
        self.tree_constraints.column("Constraint", width=240, minwidth=20, anchor=W)

        # Constraints tree headers
        self.tree_constraints.heading("Const #", text="Const #", anchor=CENTER)
        self.tree_constraints.heading("Constraint", text="Constraint", anchor=W)

        # Show tree
        self.tree_constraints.pack()


        # Penalty Logic Frame
        self.frm_penalty = tk.Frame(self.root, padx=0, pady=10)
        self.frm_penalty.grid(column=1, row=0)
        self.lbl_penalty = tk.Label(self.frm_penalty, text="Penalty Logic")
        self.lbl_penalty.pack()

        # Make tree view table for Penalty Logic
        self.tree_penalty = ttk.Treeview(self.frm_penalty, height=10)
        self.tree_penalty['columns'] = ("Pref #", "Preference", "Penalty")
        self.tree_penalty.column("#0", width=0)
        self.tree_penalty.column("Pref #", width=80, anchor=CENTER)
        self.tree_penalty.column("Preference", width=160, anchor=W)
        self.tree_penalty.column("Penalty", width=80, anchor=CENTER)

        # Attribute tree headers
        self.tree_penalty.heading("Pref #", text="Pref #", anchor=CENTER)
        self.tree_penalty.heading("Preference", text="Preference", anchor=W)
        self.tree_penalty.heading("Penalty", text="Penalty", anchor=CENTER)

        # Show tree
        self.tree_penalty.pack()


        # Possibilistic Logic Frame
        self.frm_possib = tk.Frame(self.root, padx=200, pady=10)
        self.frm_possib.grid(column=1, row=1)
        self.lbl_possib = tk.Label(self.frm_possib, text="Possibilistic Logic")
        self.lbl_possib.pack()

        # Make tree view table for attributes
        self.tree_possib = ttk.Treeview(self.frm_possib, height=10)
        self.tree_possib['columns'] = ("Pref #", "Preference", "Tolerance")
        self.tree_possib.column("#0", width=0)
        self.tree_possib.column("Pref #", width=80, anchor=CENTER)
        self.tree_possib.column("Preference", width=160, anchor=W)
        self.tree_possib.column("Tolerance", width=80, anchor=CENTER)


        # Attribute tree headers
        self.tree_possib.heading("Pref #", text="Pref #", anchor=CENTER)
        self.tree_possib.heading("Preference", text="Preference", anchor=W)
        self.tree_possib.heading("Tolerance", text="Tolerance", anchor=CENTER)

        # Show tree
        self.tree_possib.pack()


        # Qualitative Logic Frame
        self.frm_qual = tk.Frame(self.root, padx=200, pady=10)
        self.frm_qual.grid(column=1, row=2)
        self.lbl_qual = tk.Label(self.frm_qual, text="Qualitative Logic")
        self.lbl_qual.pack()

        # Make tree view table for attributes
        self.tree_qual = ttk.Treeview(self.frm_qual, height=10)
        self.tree_qual['columns'] = ("Pref #", "Preference")
        self.tree_qual.column("#0", width=0)
        self.tree_qual.column("Pref #", width=80, anchor=CENTER)
        self.tree_qual.column("Preference", width=240, anchor=W)

        # Attribute tree headers
        self.tree_qual.heading("Pref #", text="Pref #", anchor=CENTER)
        self.tree_qual.heading("Preference", text="Preference", anchor=W)

        # Show tree
        self.tree_qual.pack()

        # Main loop for GUI
        self.root.mainloop()


    def add_attribute(self, attribute):
        print("This will add attributes")

    def delete_attribute(self, attribute):
        print("This will delete attributes")
