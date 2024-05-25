import tkinter as tk
from tkinter import scrolledtext
import random

root = tk.Tk()
root.geometry("770x270")

bigtitle = tk.Label(text="Pots")

P1title = tk.Label(root, text="Pot 1")
P2title = tk.Label(root, text="Pot 2")
P3title = tk.Label(root, text="Pot 3")
P4title = tk.Label(root, text="Pot 4")

P1 = []
P2 = []
P3 = []
P4 = []

P1input = scrolledtext.ScrolledText(root, width=20, height=9)
P2input = scrolledtext.ScrolledText(root, width=20, height=9)
P3input = scrolledtext.ScrolledText(root, width=20, height=9)
P4input = scrolledtext.ScrolledText(root, width=20, height=9)

P1entry = tk.Entry(root)
P2entry = tk.Entry(root)
P3entry = tk.Entry(root)
P4entry = tk.Entry(root)


def fillP1():
    S = P1entry.get()
    if S != "":
        P1entry.delete(0, tk.END)
        if len(P1) == 0:
            P1input.insert(tk.END, S)
            P1.append(S)
        else:
            P1.append(S)
            S = "\n" + S
            P1input.insert(tk.END, S)
        if len(P1) == 8:
            P1add.grid_forget()
            P1entry.grid_forget()


def fillP2():
    S = P2entry.get()
    if S != "":
        P2entry.delete(0, tk.END)
        if len(P2) == 0:
            P2input.insert(tk.END, S)
            P2.append(S)
        else:
            P2.append(S)
            S = "\n" + S
            P2input.insert(tk.END, S)
        if len(P2) == 8:
            P2add.grid_forget()
            P2entry.grid_forget()


def fillP3():
    S = P3entry.get()
    if S != "":
        P3entry.delete(0, tk.END)
        if len(P3) == 0:
            P3input.insert(tk.END, S)
            P3.append(S)
        else:
            P3.append(S)
            S = "\n" + S
            P3input.insert(tk.END, S)
        if len(P3) == 8:
            P3add.grid_forget()
            P3entry.grid_forget()


def fillP4():
    S = P4entry.get()
    if S != "":
        P4entry.delete(0, tk.END)
        if len(P4) == 0:
            P4input.insert(tk.END, S)
            P4.append(S)
        else:
            P4.append(S)
            S = "\n" + S
            P4input.insert(tk.END, S)
        if len(P4) == 8:
            P4add.grid_forget()
            P4entry.grid_forget()


P1add = tk.Button(root, text="Add", command=fillP1)
P2add = tk.Button(root, text="Add", command=fillP2)
P3add = tk.Button(root, text="Add", command=fillP3)
P4add = tk.Button(root, text="Add", command=fillP4)


def generate():
    G1, G2, G3, G4, G5, G6, G7, G8 = [], [], [], [], [], [], [], []

    def get_random_available_choice(pot):
        available_choices = [i for i in pot if i != "(x)"]
        if not available_choices:
            return None
        return random.choice(available_choices)

    pots = [P1, P2, P3, P4]
    groups = [G1, G2, G3, G4, G5, G6, G7, G8]

    for group in groups:
        for _ in range(4):
            choices = [get_random_available_choice(pot) for pot in pots]
            if None in choices:
                print("Selection not possible. Please add more choices to the pots.")
                return
            choice = random.choice(choices)
            for pot in pots:
                if choice in pot:
                    pot[pot.index(choice)] = "(x)"
            group.append(choice)

    print(G1)
    print(G2)
    print(G3)
    print(G4)
    print(G5)
    print(G6)
    print(G7)
    print(G8)


genbutton = tk.Button(root, text="Generate", command=generate)

bigtitle.grid(row=1, column=1, columnspan=4)

P1title.grid(row=2, column=1)
P2title.grid(row=2, column=2)
P3title.grid(row=2, column=3)
P4title.grid(row=2, column=4)

P1input.grid(row=3, column=1, padx=5)
P2input.grid(row=3, column=2, padx=5)
P3input.grid(row=3, column=3, padx=5)
P4input.grid(row=3, column=4, padx=5)

P1add.grid(row=4, column=1)
P2add.grid(row=4, column=2)
P3add.grid(row=4, column=3)
P4add.grid(row=4, column=4)

P1entry.grid(row=5, column=1)
P2entry.grid(row=5, column=2)
P3entry.grid(row=5, column=3)
P4entry.grid(row=5, column=4)

genbutton.grid(row=6, column=1, columnspan=4, pady=5)
root.mainloop()
