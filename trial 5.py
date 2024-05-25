from random import randint
import tkinter as tk
from tkinter import scrolledtext

Euro = ["austria", "belgium", "bulgaria", "croatia", "czech rep", "denmark", "england", "finland", "france", "germany", "greece", "iceland", "ireland", "italy", "hungary",
        "netherlands", "norwege", "poland", "portugal", "romania", "russia", "scotland", "serbia", "slovakia", "slovenia", "spain", "sweeden", "switherland", "turkey", "ukrania", "wales"]
Afro = ["algeria", "egypt", "cameroon", "ghana", "senegal", "morocco", "nigeria", "south africa", "tunisia"]
NA = ["costa rica", "canada", "mexico", "jamaica", "usa"]
SA = ["argentina", "brazil", "chile", "colombia", "ecuadro", "panama", "peru", "uruguay"]
Asia = ["australia", "china", "iran", "irak", "japan", "north korea", "ksa", "south korea", "qatar"]
Oceania = ["New Zeeland"]


def find(Country):
    if Country in Euro:
        return 1
    elif Country in Afro:
        return 2
    elif Country in SA:
        return 3
    elif Country in NA:
        return 4
    elif Country in Asia:
        return 5
    elif Country in Oceania:
        return 6


def check(T):
    EuroNum, AfroNum, AsiaNum, SANum, NANum, OceaniaNum = 0, 0, 0, 0, 0, 0
    for i in range(4):
        A = find(T[i])
        match A:
            case 1:
                EuroNum += 1
            case 2:
                AfroNum += 1
            case 3:
                SANum += 1
            case 4:
                NANum += 1
            case 5:
                AsiaNum += 1
            case 6:
                OceaniaNum += 1
    return EuroNum <= 2 and AfroNum <= 1 and AsiaNum <= 1 and NANum <= 1 and SANum <= 1


def main():
    try:
        Countries = Euro + Afro + SA + NA + Asia + Oceania
        Host = Countries[randint(0, len(Countries) - 1)]
        A = find(Host)

        QEuro = []
        while len(QEuro) < 13:
            x = randint(0, len(Euro) - 1)
            while Euro[x] in QEuro or Euro[x] == Host:
                x = randint(0, len(Euro) - 1)
            (QEuro).append(Euro[x])

        QAfro = []
        while len(QAfro) < 5:
            x = randint(0, len(Afro) - 1)
            while Afro[x] in QAfro or Afro[x] == Host:
                x = randint(0, len(Afro) - 1)
            (QAfro).append(Afro[x])

        if A == 6:
            MaxNA = 4
            MaxOce = 0
        else:
            Choice1 = randint(0, 1)
            match Choice1:
                case 0:
                    MaxNA = 3
                    MaxOce = 1
                case 1:
                    MaxNA = 4
                    MaxOce = 0

        Choice2 = randint(0, 1)
        match Choice2:
            case 0:
                MaxSA = 5
                MaxAsia = 4
            case 1:
                MaxSA = 4
                MaxAsia = 5

        QOceania = []
        if MaxOce == 1:
            QOceania.append(Oceania[0])

        QSA = []
        while len(QSA) < MaxSA:
            x = randint(0, len(SA) - 1)
            while SA[x] in QSA or SA[x] == Host:
                x = randint(0, len(SA) - 1)
            (QSA).append(SA[x])

        QNA = []
        while len(QNA) < MaxNA:
            x = randint(0, len(NA) - 1)
            while NA[x] in QNA or NA[x] == Host:
                x = randint(0, len(NA) - 1)
            (QNA).append(NA[x])

        QAsia = []
        while len(QAsia) < MaxAsia:
            x = randint(0, len(Asia) - 1)
            while Asia[x] in QAsia or Asia[x] == Host:
                x = randint(0, len(Asia) - 1)
            (QAsia).append(Asia[x])

        QCountries = []
        QCountries.append(Host)
        QCountries += QEuro
        QCountries += QAfro
        QCountries += QNA
        QCountries += QSA
        QCountries += QAsia

        End = False
        P = []
        P.append(Host)
        while len(P) < 32:
            a = randint(1, 31)
            while QCountries[a] in P:
                a = randint(1, 31)
            P.append(QCountries[a])

        P1 = P[0:8]
        P2 = P[8:16]
        P3 = P[16:24]
        P4 = P[24:32]

        Test = False
        while not(Test):
            G = []
            G.append(Host)
            A2 = randint(0, 7)
            G.append(P2[A2])
            A3 = randint(0, 7)
            G.append(P3[A3])
            A4 = randint(0, 7)
            G.append(P4[A4])
            while len(G) < 32:
                A1 = randint(0, 7)
                while P1[A1] in G:
                    A1 = randint(0, 7)
                G.append(P1[A1])
                A2 = randint(0, 7)
                while P2[A2] in G:
                    A2 = randint(0, 7)
                G.append(P2[A2])
                A3 = randint(0, 7)
                while P3[A3] in G:
                    A3 = randint(0, 7)
                G.append(P3[A3])
                A4 = randint(0, 7)
                while P4[A4] in G:
                    A4 = randint(0, 7)
                G.append(P4[A4])

            G1 = G[0:4]
            G2 = G[4:8]
            G3 = G[8:12]
            G4 = G[12:16]
            G5 = G[16:20]
            G6 = G[20:24]
            G7 = G[24:28]
            G8 = G[28:32]
            Test = (check(G1) and check(G2) and check(G3) and check(G4) and check(
                G4) and check(G5) and check(G6) and check(G7) and check(G8))

        AffG1 = G1[0] + "\n"
        for i in range(1, 4):
            AffG1 += G1[i] + "\n"
        AffG2 = G2[0] + "\n"
        for i in range(1, 4):
            AffG2 += G2[i] + "\n"
        AffG3 = G3[0] + "\n"
        for i in range(1, 4):
            AffG3 += G3[i] + "\n"
        AffG4 = G4[0] + "\n"
        for i in range(1, 4):
            AffG4 += G4[i] + "\n"
        AffG5 = G5[0] + "\n"
        for i in range(1, 4):
            AffG5 += G5[i] + "\n"
        AffG6 = G6[0] + "\n"
        for i in range(1, 4):
            AffG6 += G6[i] + "\n"
        AffG7 = G7[0] + "\n"
        for i in range(1, 4):
            AffG7 += G7[i] + "\n"
        AffG8 = G8[0] + "\n"
        for i in range(1, 4):
            AffG8 += G8[i] + "\n"
        G1show.insert(tk.END, AffG1)
        G2show.insert(tk.END, AffG2)
        G3show.insert(tk.END, AffG3)
        G4show.insert(tk.END, AffG4)
        G5show.insert(tk.END, AffG5)
        G6show.insert(tk.END, AffG6)
        G7show.insert(tk.END, AffG7)
        G8show.insert(tk.END, AffG8)
        generate.grid_forget()
        delete.grid(row=6, column=1, columnspan=2, pady=5)

    except Exception as e:
        main()


def execute():
    if __name__ == "__main__":
        main()


def clear():
    G1show.delete(1.0, tk.END)
    G2show.delete(1.0, tk.END)
    G3show.delete(1.0, tk.END)
    G4show.delete(1.0, tk.END)
    G5show.delete(1.0, tk.END)
    G6show.delete(1.0, tk.END)
    G7show.delete(1.0, tk.END)
    G8show.delete(1.0, tk.END)
    delete.grid_forget()
    generate.grid(row=6, column=1, columnspan=2, pady=5)


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


root = tk.Tk()
root.title("World Cup : Winner Soccer Evolution")
root.geometry("770x270")
title = tk.Label(root, text="World Cup Bild")
G1title = tk.Label(root, text="G1")
G2title = tk.Label(root, text="G2")
G3title = tk.Label(root, text="G3")
G4title = tk.Label(root, text="G4")
G5title = tk.Label(root, text="G5")
G6title = tk.Label(root, text="G6")
G7title = tk.Label(root, text="G7")
G8title = tk.Label(root, text="G8")
G1show = scrolledtext.ScrolledText(root, width=20, height=5)
G2show = scrolledtext.ScrolledText(root, width=20, height=5)
G3show = scrolledtext.ScrolledText(root, width=20, height=5)
G4show = scrolledtext.ScrolledText(root, width=20, height=5)
G5show = scrolledtext.ScrolledText(root, width=20, height=5)
G6show = scrolledtext.ScrolledText(root, width=20, height=5)
G7show = scrolledtext.ScrolledText(root, width=20, height=5)
G8show = scrolledtext.ScrolledText(root, width=20, height=5)
generate = tk.Button(root, text="Generate", command=execute)
delete = tk.Button(root, text="Clear", command=clear)
showbutton = tk.Button(root, text="Show countries", command=show)


title.grid(row=1, column=1, columnspan=4)
G1title.grid(row=2, column=1)
G2title.grid(row=2, column=2)
G3title.grid(row=2, column=3)
G4title.grid(row=2, column=4)
G1show.grid(row=3, column=1, padx=5)
G2show.grid(row=3, column=2, padx=5)
G3show.grid(row=3, column=3, padx=5)
G4show.grid(row=3, column=4, padx=5)
G5title.grid(row=4, column=1)
G6title.grid(row=4, column=2)
G7title.grid(row=4, column=3)
G8title.grid(row=4, column=4)
G5show.grid(row=5, column=1, padx=5)
G6show.grid(row=5, column=2, padx=5)
G7show.grid(row=5, column=3, padx=5)
G8show.grid(row=5, column=4, padx=5)
generate.grid(row=6, column=1, columnspan=2, pady=5)
showbutton.grid(row=6, column=3, columnspan=2, pady=5)


root.mainloop()
