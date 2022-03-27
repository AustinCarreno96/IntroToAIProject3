from tkinter import *
from tkinter import ttk
import tkinter as tk
# import main


class PyGUI:
    def __init__(self, input_dict):
        # Make and name TK GUI
        self.dict = input_dict
        self.root = Tk()
        self.root.title("Project 3 AI")

        # Left Frame
        self.frm_left = tk.LabelFrame(self.root, text="", labelanchor=N, padx=100, pady=50)
        self.frm_left.grid(column=0, row=0)

        # Attribute Label
        self.lbl_attr = Label(self.frm_left, text="Binary Attributes")
        self.lbl_attr.pack()

        # Make tree view table for attributes
        self.tree_attr = ttk.Treeview(self.frm_left, height=10)
        self.tree_attr['columns'] = ("Attr #", "Attribute", "Option 1", "Option 2")
        self.tree_attr.column("#0", width=0)
        self.tree_attr.column("Attr #", width=100, minwidth=50, anchor=CENTER)
        self.tree_attr.column("Attribute", width=100, minwidth=50, anchor=CENTER)
        self.tree_attr.column("Option 1", width=100, minwidth=50, anchor=CENTER)
        self.tree_attr.column("Option 2", width=100, minwidth=50, anchor=CENTER)

        # Attribute tree headers
        self.tree_attr.heading("Attr #", text="Attr #", anchor=CENTER)
        self.tree_attr.heading("Attribute", text="Attribute", anchor=CENTER)
        self.tree_attr.heading("Option 1", text="Option 1", anchor=CENTER)
        self.tree_attr.heading("Option 2", text="Option 2", anchor=CENTER)

        # Show tree
        self.tree_attr.pack()


        # Constraints Label
        self.lbl_con = Label(self.frm_left, text="Hard Constraints")
        self.lbl_con.pack()

        # Make Constraints tree
        self.tree_con = ttk.Treeview(self.frm_left, height=10)
        self.tree_con['columns'] = ("Const #", "Constraint")
        self.tree_con.column("#0", width=0)
        self.tree_con.column("Const #", width=100, minwidth=20, anchor=CENTER)
        self.tree_con.column("Constraint", width=300, minwidth=50, anchor=CENTER)

        # Constraints tree headers
        self.tree_con.heading("Const #", text="Const #", anchor=CENTER)
        self.tree_con.heading("Constraint", text="Constraint", anchor=CENTER)

        # Show tree
        self.tree_con.pack()


        # Right Frame
        self.frm_right = LabelFrame(self.root, text="", padx=100, pady=25)
        self.frm_right.grid(column=1, row=0)

        # Penalty Logic Label
        self.lbl_pen = Label(self.frm_right, text="Penalty Logic")
        self.lbl_pen.pack()

        # Make tree view table for Penalty Logic
        self.tree_pen = ttk.Treeview(self.frm_right, height=6)
        self.tree_pen['columns'] = ("Pref #", "Preference", "Penalty")
        self.tree_pen.column("#0", width=0)
        self.tree_pen.column("Pref #", width=100, anchor=CENTER)
        self.tree_pen.column("Preference", width=250, anchor=CENTER)
        self.tree_pen.column("Penalty", width=100, anchor=CENTER)

        # Penalty Logic tree headers
        self.tree_pen.heading("Pref #", text="Pref #", anchor=CENTER)
        self.tree_pen.heading("Preference", text="Preference", anchor=CENTER)
        self.tree_pen.heading("Penalty", text="Penalty", anchor=CENTER)

        # Show tree
        self.tree_pen.pack()


        # Possibilistic Logic Label
        self.lbl_possib = Label(self.frm_right, text="Possibilistic Logic")
        self.lbl_possib.pack()

        # Make tree view table for possibilistic logics
        self.tree_possib = ttk.Treeview(self.frm_right, height=6)
        self.tree_possib['columns'] = ("Pref #", "Preference", "Tolerance")
        self.tree_possib.column("#0", width=0)
        self.tree_possib.column("Pref #", width=100, anchor=CENTER)
        self.tree_possib.column("Preference", width=250, anchor=CENTER)
        self.tree_possib.column("Tolerance", width=100, anchor=CENTER)

        # Possibilistic tree headers
        self.tree_possib.heading("Pref #", text="Pref #", anchor=CENTER)
        self.tree_possib.heading("Preference", text="Preference", anchor=CENTER)
        self.tree_possib.heading("Tolerance", text="Tolerance", anchor=CENTER)

        # Show tree
        self.tree_possib.pack()


        # Qualitative Form Logic Label
        self.lbl_qual = Label(self.frm_right, text="Qualitative Form Logic")
        self.lbl_qual.pack()

        # Make tree view table for attributes
        self.tree_qual = ttk.Treeview(self.frm_right, height=6)
        self.tree_qual['columns'] = ("Pref #", "Preference")
        self.tree_qual.column("#0", width=0)
        self.tree_qual.column("Pref #", width=100, anchor=CENTER)
        self.tree_qual.column("Preference", width=350, anchor=CENTER)

        # Attribute tree headers
        self.tree_qual.heading("Pref #", text="Pref #", anchor=CENTER)
        self.tree_qual.heading("Preference", text="Preference", anchor=CENTER)

        # Show tree
        self.tree_qual.pack()


        # Read and Display to TreeView widgets
        self.display_attributes()
        self.display_constraints()
        self.display_penalty()
        self.display_possibilistic()
        # self.display_qualitative()

        # Main loop for GUI
        self.root.mainloop()


    def add_attribute(self, attribute):
        print("This will add attributes")

    def delete_attribute(self, attribute):
        print("This will delete attributes")

    # Displays Binary Attributes values
    def display_attributes(self):
        i = 0
        while i < len(self.dict['attributes']):
            attr_num = i + 1
            attr_name = self.dict['attributes'][i][0]
            attr_op1 = self.dict['attributes'][i][1]
            attr_op2 = self.dict['attributes'][i][2]
            self.tree_attr.insert(parent='', index='end', iid=i, values=(attr_num, attr_name, attr_op1, attr_op2))
            i += 1

    # Displays Hard Constraints variables
    def display_constraints(self):
        i = 0
        while i < len(self.dict['hard_constraints']):
            con_num = i + 1
            con_name = self.dict['hard_constraints'][i]
            if con_name == '':
                break
            self.tree_con.insert(parent='', index='end', iid=i, values=(con_num, con_name))
            i += 1

    # Displays Penalty Logic variables
    def display_penalty(self):
        i = 0
        while i < len(self.dict['penalty_logic']['penalty']):
            pen_num = i + 1
            pen_pref = self.dict['penalty_logic']['logic_stmts'][i]
            pen_penalty = self.dict['penalty_logic']['penalty'][i]
            self.tree_pen.insert(parent='', index='end', iid=i, values=(pen_num, pen_pref, pen_penalty))
            i += 1

    # Displays Possibilistic Logic variables
    def display_possibilistic(self):
        i = 0
        while i < len(self.dict['possibilistic_logic']['tolerance']):
            possib_num = i + 1
            possib_pref = self.dict['possibilistic_logic']['logic_stmts'][i]
            possib_tol = self.dict['possibilistic_logic']['tolerance'][i]
            self.tree_possib.insert(parent='', index='end', iid=i, values=(possib_num, possib_pref, possib_tol))
            i += 1

    # Displays Qualitative Form Logic variables
    def display_qualitative(self):
        i = 0
        print("")



