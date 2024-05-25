from random import randint
from tkinter import scrolledtext
import tkinter as tk
Euro = ["Albania", "Austria", "Belgium", "Bosnia and Herzovico", "Bulgaria", "Croatia", "Czech Rep.", "Denmark", "England", "Finland", "France", "North Macedonia", "Germany", "Greece", "Hungary", "Iceland", "Ireland",
        "Italy", "Latvia", "Netherlands", "Northen Ireland", "Norway", "Poland", "Portugal", "Romania", "Russia", "Scotland", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweeden", "Switherland", "Turkey", "Ukraine", "Wales"]
Afro = ["Algeria", "Angola", "Benin", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Comoros", "Congo Rep.", "DRC", "Egypt", "Equatorial Guinea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea Bisseau",
        "Ivory Coast", "Kenya", "Madagashcar", "Malawi", "Mali", "Mauritania", "Morocco", "Namibia", "Niger", "Nigeria", "Senegal", "Sierra Leone", "South Africa", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
SA = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Paraguay", "Peru", "Uruguay", "Venezuela"]
NA = ["Belize", "Bermuda", "Canada", "Costa Rica", "Cuba", "Curaco", "El Salvador", "French Guyana", "Grenada", "Guadelope", "Guatemela",
      "Guyana", "Haiti", "Honduras", "Jamaica", "Martinique", "Mexico", "Nicaragua", "Panama", "Suriname", "Trinidad and Tobago", "USA"]
Asia = ["Australia", "Bahrain", "China", "India", "Indonesia", "Iran", "Iraq", "Japan", "Jordan", "Kuwait", "Kygyzstan", "Lebanon", "Malaysia", "North Korea",
        "Oman", "Palestine", "Philippines", "Qatar", "KSA", "South Korea", "Syria", "Thailand", "Turkemenistan", "UAE", "Uzbakestan", "Vietnam", "Yemen"]
Oceania = ["New Zeeland"]

Continents = Euro + Afro + SA + NA + Asia + Oceania


root = tk.Tk()
root.title("World Cup")
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
    if S != "" and S in Continents:
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
    if S != "" and S in Continents:
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
    if S != "" and S in Continents:
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
    if S != "" and S in Continents:
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


def generate():
    P = P1 + P2 + P3 + P4
    G1, G2, G3, G4, G5, G6, G7, G8 = [], [], [], [], [], [], [], []
    for i in range(32):
        Test = False
        while not(Test):
            X = randint(1, 8)
            match X:
                case 1:
                    Test = (len(G1) != 4)
                    if Test:
                        G1.append(P[i])
                case 2:
                    Test = (len(G2) != 4)
                    if Test:
                        G2.append(P[i])
                case 3:
                    Test = (len(G3) != 4)
                    if Test:
                        G3.append(P[i])
                case 4:
                    Test = (len(G4) != 4)
                    if Test:
                        G4.append(P[i])
                case 5:
                    Test = (len(G5) != 4)
                    if Test:
                        G5.append(P[i])
                case 6:
                    Test = (len(G6) != 4)
                    if Test:
                        G6.append(P[i])
                case 7:
                    Test = (len(G7) != 4)
                    if Test:
                        G7.append(P[i])
                case 8:
                    Test = (len(G8) != 4)
                    if Test:
                        G8.append(P[i])
    print(G1)
    print(G2)
    print(G3)
    print(G4)
    print(G5)
    print(G6)
    print(G7)
    print(G8)


def show():
    cont = tk.Toplevel()
    cont.title("Countries list")

    conttitle = tk.Label(cont, text="Countries")
    conttitle.grid(row=1, column=1, columnspan=6)

    eurotitle = tk.Label(cont, text="Europe")
    eurotitle.grid(row=2, column=1)
    afrotitle = tk.Label(cont, text="Africa")
    afrotitle.grid(row=2, column=2)
    asiatitle = tk.Label(cont, text="Asia")
    asiatitle.grid(row=2, column=3)
    satitle = tk.Label(cont, text="South America")
    satitle.grid(row=2, column=4)
    natitle = tk.Label(cont, text="North America")
    natitle.grid(row=2, column=5)
    oceantitle = tk.Label(cont, text="Oceania")
    oceantitle.grid(row=2, column=6)

    Eurolist = scrolledtext.ScrolledText(cont, width=20, height=38)
    Euroelements = Euro[0]
    for i in range(1, len(Euro)):
        Euroelements += "\n" + Euro[i]
    Eurolist.insert(tk.END, Euroelements)

    Afrolist = scrolledtext.ScrolledText(cont, width=20, height=38)
    Afroelements = Afro[0]
    for i in range(1, len(Afro)):
        Afroelements += "\n" + Afro[i]
    Afrolist.insert(tk.END, Afroelements)

    Asialist = scrolledtext.ScrolledText(cont, width=20, height=38)
    Asiaelements = Asia[0]
    for i in range(1, len(Asia)):
        Asiaelements += "\n" + Asia[i]
    Asialist.insert(tk.END, Asiaelements)

    NAlist = scrolledtext.ScrolledText(cont, width=20, height=38)
    NAelements = NA[0]
    for i in range(1, len(NA)):
        NAelements += "\n" + NA[i]
    NAlist.insert(tk.END, NAelements)

    SAlist = scrolledtext.ScrolledText(cont, width=20, height=38)
    SAelements = SA[0]
    for i in range(1, len(SA)):
        SAelements += "\n" + SA[i]
    SAlist.insert(tk.END, SAelements)

    Oceanialist = scrolledtext.ScrolledText(cont, width=20, height=38)
    Oceaniaelements = Oceania[0]
    for i in range(1, len(Oceania)):
        Oceaniaelements += "\n" + Oceania[i]
    Oceanialist.insert(tk.END, Oceaniaelements)

    Eurolist.grid(row=3, column=1)
    Afrolist.grid(row=3, column=2)
    Asialist.grid(row=3, column=3)
    NAlist.grid(row=3, column=4)
    SAlist.grid(row=3, column=5)
    Oceanialist.grid(row=3, column=6)

    hint = tk.Label(cont, text="Only countries with this synthax will be accepted")
    hint.grid(row=4, column=1, columnspan=6)


genbutton = tk.Button(root, text="Generate", command=generate)
showbutton = tk.Button(root, text="Show countries", command=show)

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

genbutton.grid(row=6, column=1, columnspan=2, pady=5)
showbutton.grid(row=6, column=3, columnspan=2, pady=5)

root.mainloop()
