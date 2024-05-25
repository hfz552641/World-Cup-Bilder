import tkinter as tk
from tkinter import scrolledtext

Euro = ["austria", "belgium", "bulgaria", "croatia", "czech rep", "denmark", "england", "finland", "france", "germany", "greece", "iceland", "ireland", "italy", "hungary",
        "netherlands", "norwege", "poland", "portugal", "romania", "russia", "scotland", "serbia", "slovakia", "slovenia", "spain", "sweeden", "switherland", "turkey", "ukrania", "wales"]
Afro = ["algeria", "egypt", "cameroon", "ghana", "senegal", "morocco", "nigeria", "south africa", "tunisia"]
NA = ["costa rica", "canada", "mexico", "jamaica", "usa"]
SA = ["argentina", "brazil", "chile", "colombia", "ecuadro", "panama", "peru", "uruguay"]
Asia = ["australia", "china", "iran", "irak", "japan", "new zeeland", "north korea", "ksa", "south korea", "qatar"]

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


def CalcEuro(EuroQ, G):
    n = 0
    for i in range(len(G)):
        if G[i] in Euro:
            n += 1
    return n


def CalcAfro(AfroQ, G):
    n = 0
    for i in range(len(G)):
        if G[i] in Afro:
            n += 1
    return n


def CalcAsia(AsiaQ, G):
    n = 0
    for i in range(len(G)):
        if G[i] in Asia:
            n += 1
    return n


def CalcNA(NAQ, G):
    n = 0
    for i in range(len(G)):
        if G[i] in NA:
            n += 1
    return n


def CalcSA(SAQ, G):
    n = 0
    for i in range(len(G)):
        if G[i] in SA:
            n += 1
    return n


def search(A, Europe, Afro, Asia, SA, NA):
    if A in Europe:
        return 1
    elif A in Afro:
        return 2
    elif A in Asia:
        return 3
    elif A in NA:
        return 4
    elif A in SA:
        return 5


G1, G2, G3, G4, G5, G6, G7, G8 = [], [], [], [], [], [], [], []
T = P1 + P2 + P3 + P4
for i in range(32):
    A = T[i]
    j = 1
    while j != 9:
        Test
        if len(G) != 0:
            print("")


P1add = tk.Button(root, text="Add", command=fillP1)
P2add = tk.Button(root, text="Add", command=fillP2)
P3add = tk.Button(root, text="Add", command=fillP3)
P4add = tk.Button(root, text="Add", command=fillP4)

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


root.mainloop()
