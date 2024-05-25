from random import randint

Euro = ["austria", "belgium", "bulgaria", "croatia", "czech rep", "denmark", "england", "finland", "france", "germany", "greece", "iceland", "ireland", "italy", "hungary",
        "netherlands", "norwege", "poland", "portugal", "romania", "russia", "scotland", "serbia", "slovakia", "slovenia", "spain", "sweeden", "switherland", "turkey", "ukrania", "wales"]
Afro = ["algeria", "egypt", "cameroon", "ghana", "senegal", "morocco", "nigeria", "south africa", "tunisia"]
NA = ["costa rica", "canada", "mexico", "jamaica", "usa"]
SA = ["argentina", "brazil", "chile", "colombia", "ecuadro", "panama", "peru", "uruguay"]
Asia = ["australia", "china", "iran", "irak", "japan", "new zeeland", "north korea", "ksa", "south korea", "qatar"]

print("World Cup : Winner Soccer Evolution")

T = []
EuroQ = []
for a in range(13):
    X = randint(0, len(Euro) - 1)
    while Euro[X] in EuroQ:
        X = randint(0, len(Euro) - 1)
    EuroQ.append(Euro[X])
T = T + EuroQ
AfroQ = []
for b in range(5):
    Y = randint(0, len(Afro) - 1)
    while Afro[Y] in AfroQ:
        Y = randint(0, len(Afro) - 1)
    AfroQ.append(Afro[Y])
T = T + AfroQ
AsiaQ = []
for c in range(5):
    A = randint(0, len(Asia) - 1)
    while Asia[A] in AsiaQ:
        A = randint(0, len(Asia) - 1)
    AsiaQ.append(Asia[A])
T = T + AsiaQ
NAQ = []
SAQ = []
for d in range(9):
    choice = randint(0, 1)
    match choice:
        case 0:
            B = randint(0, len(NA) - 1)
            while NA[B] in NAQ:
                B = randint(0, len(NA) - 1)
            NAQ.append(NA[B])
        case 1:
            C = randint(0, len(SA) - 1)
            while SA[C] in SAQ:
                C = randint(0, len(SA) - 1)
            SAQ.append(SA[C])
T = T + NAQ + SAQ
P1, P2, P3, P4 = [], [], [], []
for i in range(8):
    s = randint(0, 31)
    while T[s] in P1 or T[s] in P2 or T[s] in P3 or T[s] in P4:
        s = randint(0, 31)
    P1.append(T[s])
for i in range(8):
    s = randint(0, 31)
    while T[s] in P1 or T[s] in P2 or T[s] in P3 or T[s] in P4:
        s = randint(0, 31)
    P2.append(T[s])
for i in range(8):
    s = randint(0, 31)
    while T[s] in P1 or T[s] in P2 or T[s] in P3 or T[s] in P4:
        s = randint(0, 31)
    P3.append(T[s])
for i in range(8):
    s = randint(0, 31)
    while T[s] in P1 or T[s] in P2 or T[s] in P3 or T[s] in P4:
        s = randint(0, 31)
    P4.append(T[s])
i = 0
G1, G2, G3, G4, G5, G6, G7, G8 = [], [], [], [], [], [], [], []


def show(i, G1, G2, G3, G4, G5, G6, G7, G8):
    print("Bild number : " + str(i))
    print("G1 : ", end="")
    print(G1)
    print("G2 : ", end="")
    print(G2)
    print("G3 : ", end="")
    print(G3)
    print("G4 : ", end="")
    print(G4)
    print("G5 : ", end="")
    print(G5)
    print("G6 : ", end="")
    print(G6)
    print("G7 : ", end="")
    print(G7)
    print("G8 : ", end="")
    print(G8)


def search(x, a, EuroQ, AfroQ, AsiaQ, NAQ, SAQ, P1, P2, P3, P4):
    match a:
        case 1:
            if P1[x] in EuroQ:
                return 1
            elif P1[x] in AfroQ:
                return 2
            elif P1[x] in AsiaQ:
                return 3
            elif P1[x] in NAQ:
                return 4
            elif P1[x] in SAQ:
                return 5
        case 2:
            if P2[x] in EuroQ:
                return 1
            elif P2[x] in AfroQ:
                return 2
            elif P2[x] in AsiaQ:
                return 3
            elif P2[x] in NAQ:
                return 4
            elif P2[x] in SAQ:
                return 5
        case 3:
            if P3[x] in EuroQ:
                return 1
            elif P3[x] in AfroQ:
                return 2
            elif P3[x] in AsiaQ:
                return 3
            elif P3[x] in NAQ:
                return 4
            elif P3[x] in SAQ:
                return 5
        case 4:
            if P4[x] in EuroQ:
                return 1
            elif P4[x] in AfroQ:
                return 2
            elif P4[x] in AsiaQ:
                return 3
            elif P4[x] in NAQ:
                return 4
            elif P4[x] in SAQ:
                return 5


def CalcEuro(EuroQ, G):
    n = 0
    for i in range(4):
        if G[i] in EuroQ:
            n += 1
    return n


def CalcAfro(AfroQ, G):
    n = 0
    for i in range(4):
        if G[i] in AfroQ:
            n += 1
    return n


def CalcAsia(AsiaQ, G):
    n = 0
    for i in range(4):
        if G[i] in AsiaQ:
            n += 1
    return n


def CalcNA(NAQ, G):
    n = 0
    for i in range(4):
        if G[i] in NAQ:
            n += 1
    return n


def CalcSA(SAQ, G):
    n = 0
    for i in range(4):
        if G[i] in SAQ:
            n += 1
    return n


def verifend(G1, G2, G3, G4, G5, G6, G7, G8):
    Test = ((len(G1) == 4) or (len(G2) == 4) or (len(G3) == 4) or (len(G4) == 4)
            or (len(G5) == 4) or (len(G6) == 4) or (len(G7) == 4) or (len(G8) == 4))
    return Test


while verifend:
    i += 1
    show(i, G1, G2, G3, G4, G5, G6, G7, G8)
    a = randint(1, 4)
    match a:
        case 1:
            x = randint(0, 7)
            while P1[x] in G1 or P1[x] in G2 or P1[x] in G3 or P1[x] in G4 or P1[x] in G5 or P1[x] in G6 or P1[x] in G7 or P1[x] in G8:
                x = randint(0, 7)
            loc = search(x, a, EuroQ, AfroQ, AsiaQ, NAQ, SAQ, P1, P2, P3, P4)
            match loc:
                case 1:
                    n = CalcEuro(EuroQ, G1)
                    if n < 2 and len(G1) != 4:
                        G1.append(P1[x])
                    else:
                        n = CalcEuro(EuroQ, G2)
                        if n < 2 and len(G2) != 4:
                            G2.append(P1[x])
                        else:
                            n = CalcEuro(EuroQ, G3)
                            if n < 2 and len(G3) != 4:
                                G3.append(P1[x])
                            else:
                                n = CalcEuro(EuroQ, G4)
                                if n < 2 and len(G4) != 4:
                                    G4.append(P1[x])
                                else:
                                    n = CalcEuro(EuroQ, G5)
                                    if n < 2 and len(G5) != 4:
                                        G5.append(P1[x])
                                    else:
                                        n = CalcEuro(EuroQ, G6)
                                        if n < 2 and len(G6) != 4:
                                            G6.append(P1[x])
                                        else:
                                            n = CalcEuro(EuroQ, G7)
                                            if n < 2 and len(G7) != 4:
                                                G7.append(P1[x])
                                            else:
                                                n = CalcEuro(EuroQ, G8)
                                                if n < 2 and len(G8) != 4:
                                                    G8.append(P1[x])
                case 2:
                    n = CalcAfro(AfroQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P1[x])
                    else:
                        n = CalcAfro(AfroQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P1[x])
                        else:
                            n = CalcAfro(AfroQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P1[x])
                            else:
                                n = CalcAfro(AfroQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P1[x])
                                else:
                                    n = CalcAfro(AfroQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P1[x])
                                    else:
                                        n = CalcAfro(AfroQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P1[x])
                                        else:
                                            n = CalcAfro(AfroQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P1[x])
                                            else:
                                                n = CalcAfro(AfroQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P1[x])
                case 3:
                    n = CalcAsia(AsiaQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P1[x])
                    else:
                        n = CalcAsia(AsiaQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P1[x])
                        else:
                            n = CalcAsia(AsiaQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P1[x])
                            else:
                                n = CalcAsia(AsiaQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P1[x])
                                else:
                                    n = CalcAsia(AsiaQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P1[x])
                                    else:
                                        n = CalcAsia(AsiaQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P1[x])
                                        else:
                                            n = CalcAsia(AsiaQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P1[x])
                                            else:
                                                n = CalcAsia(AsiaQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P1[x])
                case 4:
                    n = CalcNA(NAQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P1[x])
                    else:
                        n = CalcNA(NAQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P1[x])
                        else:
                            n = CalcNA(NAQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P1[x])
                            else:
                                n = CalcNA(NAQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P1[x])
                                else:
                                    n = CalcNA(NAQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P1[x])
                                    else:
                                        n = CalcNA(NAQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P1[x])
                                        else:
                                            n = CalcNA(NAQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P1[x])
                                            else:
                                                n = CalcNA(NAQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P1[x])
                case 5:
                    n = CalcSA(SAQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P1[x])
                    else:
                        n = CalcSA(SAQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P1[x])
                        else:
                            n = CalcSA(SAQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P1[x])
                            else:
                                n = CalcSA(SAQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P1[x])
                                else:
                                    n = CalcSA(SAQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P1[x])
                                    else:
                                        n = CalcSA(SAQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P1[x])
                                        else:
                                            n = CalcSA(SAQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P1[x])
                                            else:
                                                n = CalcSA(SAQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P1[x])
        case 2:
            x = randint(0, 7)
            while P1[x] in G1 or P1[x] in G2 or P1[x] in G3 or P1[x] in G4 or P1[x] in G5 or P1[x] in G6 or P1[x] in G7 or P1[x] in G8:
                x = randint(0, 7)
            loc = search(x, a, EuroQ, AfroQ, AsiaQ, NAQ, SAQ, P1, P2, P3, P4)
            match loc:
                case 1:
                    n = CalcEuro(EuroQ, G1)
                    if n < 2 and len(G1) != 4:
                        G1.append(P2[x])
                    else:
                        n = CalcEuro(EuroQ, G2)
                        if n < 2 and len(G2) != 4:
                            G2.append(P2[x])
                        else:
                            n = CalcEuro(EuroQ, G3)
                            if n < 2 and len(G3) != 4:
                                G3.append(P2[x])
                            else:
                                n = CalcEuro(EuroQ, G4)
                                if n < 2 and len(G4) != 4:
                                    G4.append(P2[x])
                                else:
                                    n = CalcEuro(EuroQ, G5)
                                    if n < 2 and len(G5) != 4:
                                        G5.append(P2[x])
                                    else:
                                        n = CalcEuro(EuroQ, G6)
                                        if n < 2 and len(G6) != 4:
                                            G6.append(P2[x])
                                        else:
                                            n = CalcEuro(EuroQ, G7)
                                            if n < 2 and len(G7) != 4:
                                                G7.append(P2[x])
                                            else:
                                                n = CalcEuro(EuroQ, G8)
                                                if n < 2 and len(G8) != 4:
                                                    G8.append(P2[x])
                case 2:
                    n = CalcAfro(AfroQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P2[x])
                    else:
                        n = CalcAfro(AfroQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P2[x])
                        else:
                            n = CalcAfro(AfroQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P2[x])
                            else:
                                n = CalcAfro(AfroQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P2[x])
                                else:
                                    n = CalcAfro(AfroQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P2[x])
                                    else:
                                        n = CalcAfro(AfroQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P2[x])
                                        else:
                                            n = CalcAfro(AfroQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P2[x])
                                            else:
                                                n = CalcAfro(AfroQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P2[x])
                case 3:
                    n = CalcAsia(AsiaQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P2[x])
                    else:
                        n = CalcAsia(AsiaQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P2[x])
                        else:
                            n = CalcAsia(AsiaQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P2[x])
                            else:
                                n = CalcAsia(AsiaQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P2[x])
                                else:
                                    n = CalcAsia(AsiaQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P2[x])
                                    else:
                                        n = CalcAsia(AsiaQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P2[x])
                                        else:
                                            n = CalcAsia(AsiaQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P2[x])
                                            else:
                                                n = CalcAsia(AsiaQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P2[x])
                case 4:
                    n = CalcNA(NAQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P2[x])
                    else:
                        n = CalcNA(NAQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P2[x])
                        else:
                            n = CalcNA(NAQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P2[x])
                            else:
                                n = CalcNA(NAQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P2[x])
                                else:
                                    n = CalcNA(NAQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P2[x])
                                    else:
                                        n = CalcNA(NAQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P2[x])
                                        else:
                                            n = CalcNA(NAQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P2[x])
                                            else:
                                                n = CalcNA(NAQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P2[x])
                case 5:
                    n = CalcSA(SAQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P2[x])
                    else:
                        n = CalcSA(SAQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P2[x])
                        else:
                            n = CalcSA(SAQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P2[x])
                            else:
                                n = CalcSA(SAQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P2[x])
                                else:
                                    n = CalcSA(SAQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P2[x])
                                    else:
                                        n = CalcSA(SAQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P2[x])
                                        else:
                                            n = CalcSA(SAQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P2[x])
                                            else:
                                                n = CalcSA(SAQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P2[x])
        case 3:
            x = randint(0, 7)
            while P1[x] in G1 or P1[x] in G2 or P1[x] in G3 or P1[x] in G4 or P1[x] in G5 or P1[x] in G6 or P1[x] in G7 or P1[x] in G8:
                x = randint(0, 7)
            loc = search(x, a, EuroQ, AfroQ, AsiaQ, NAQ, SAQ, P1, P2, P3, P4)
            match loc:
                case 1:
                    n = CalcEuro(EuroQ, G1)
                    if n < 2 and len(G1) != 4:
                        G1.append(P3[x])
                    else:
                        n = CalcEuro(EuroQ, G2)
                        if n < 2 and len(G2) != 4:
                            G2.append(P3[x])
                        else:
                            n = CalcEuro(EuroQ, G3)
                            if n < 2 and len(G3) != 4:
                                G3.append(P3[x])
                            else:
                                n = CalcEuro(EuroQ, G4)
                                if n < 2 and len(G4) != 4:
                                    G4.append(P3[x])
                                else:
                                    n = CalcEuro(EuroQ, G5)
                                    if n < 2 and len(G5) != 4:
                                        G5.append(P3[x])
                                    else:
                                        n = CalcEuro(EuroQ, G6)
                                        if n < 2 and len(G6) != 4:
                                            G6.append(P3[x])
                                        else:
                                            n = CalcEuro(EuroQ, G7)
                                            if n < 2 and len(G7) != 4:
                                                G7.append(P3[x])
                                            else:
                                                n = CalcEuro(EuroQ, G8)
                                                if n < 2 and len(G8) != 4:
                                                    G8.append(P3[x])
                case 2:
                    n = CalcAfro(AfroQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P3[x])
                    else:
                        n = CalcAfro(AfroQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P3[x])
                        else:
                            n = CalcAfro(AfroQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P3[x])
                            else:
                                n = CalcAfro(AfroQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P3[x])
                                else:
                                    n = CalcAfro(AfroQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P3[x])
                                    else:
                                        n = CalcAfro(AfroQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P3[x])
                                        else:
                                            n = CalcAfro(AfroQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P3[x])
                                            else:
                                                n = CalcAfro(AfroQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P3[x])
                case 3:
                    n = CalcAsia(AsiaQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P3[x])
                    else:
                        n = CalcAsia(AsiaQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P3[x])
                        else:
                            n = CalcAsia(AsiaQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P3[x])
                            else:
                                n = CalcAsia(AsiaQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P3[x])
                                else:
                                    n = CalcAsia(AsiaQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P3[x])
                                    else:
                                        n = CalcAsia(AsiaQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P3[x])
                                        else:
                                            n = CalcAsia(AsiaQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P3[x])
                                            else:
                                                n = CalcAsia(AsiaQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P3[x])
                case 4:
                    n = CalcNA(NAQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P3[x])
                    else:
                        n = CalcNA(NAQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P3[x])
                        else:
                            n = CalcNA(NAQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P3[x])
                            else:
                                n = CalcNA(NAQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P3[x])
                                else:
                                    n = CalcNA(NAQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P3[x])
                                    else:
                                        n = CalcNA(NAQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P3[x])
                                        else:
                                            n = CalcNA(NAQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P3[x])
                                            else:
                                                n = CalcNA(NAQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P3[x])
                case 5:
                    n = CalcSA(SAQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P3[x])
                    else:
                        n = CalcSA(SAQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P3[x])
                        else:
                            n = CalcSA(SAQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P3[x])
                            else:
                                n = CalcSA(SAQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P3[x])
                                else:
                                    n = CalcSA(SAQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P3[x])
                                    else:
                                        n = CalcSA(SAQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P3[x])
                                        else:
                                            n = CalcSA(SAQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P3[x])
                                            else:
                                                n = CalcSA(SAQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P3[x])
        case 2:
            x = randint(0, 7)
            while P1[x] in G1 or P1[x] in G2 or P1[x] in G3 or P1[x] in G4 or P1[x] in G5 or P1[x] in G6 or P1[x] in G7 or P1[x] in G8:
                x = randint(0, 7)
            loc = search(x, a, EuroQ, AfroQ, AsiaQ, NAQ, SAQ, P1, P2, P3, P4)
            match loc:
                case 1:
                    n = CalcEuro(EuroQ, G1)
                    if n < 2 and len(G1) != 4:
                        G1.append(P4[x])
                    else:
                        n = CalcEuro(EuroQ, G2)
                        if n < 2 and len(G2) != 4:
                            G2.append(P4[x])
                        else:
                            n = CalcEuro(EuroQ, G3)
                            if n < 2 and len(G3) != 4:
                                G3.append(P4[x])
                            else:
                                n = CalcEuro(EuroQ, G4)
                                if n < 2 and len(G4) != 4:
                                    G4.append(P4[x])
                                else:
                                    n = CalcEuro(EuroQ, G5)
                                    if n < 2 and len(G5) != 4:
                                        G5.append(P4[x])
                                    else:
                                        n = CalcEuro(EuroQ, G6)
                                        if n < 2 and len(G6) != 4:
                                            G6.append(P4[x])
                                        else:
                                            n = CalcEuro(EuroQ, G7)
                                            if n < 2 and len(G7) != 4:
                                                G7.append(P4[x])
                                            else:
                                                n = CalcEuro(EuroQ, G8)
                                                if n < 2 and len(G8) != 4:
                                                    G8.append(P4[x])
                case 2:
                    n = CalcAfro(AfroQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P4[x])
                    else:
                        n = CalcAfro(AfroQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P4[x])
                        else:
                            n = CalcAfro(AfroQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P4[x])
                            else:
                                n = CalcAfro(AfroQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P4[x])
                                else:
                                    n = CalcAfro(AfroQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P4[x])
                                    else:
                                        n = CalcAfro(AfroQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P4[x])
                                        else:
                                            n = CalcAfro(AfroQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P4[x])
                                            else:
                                                n = CalcAfro(AfroQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P4[x])
                case 3:
                    n = CalcAsia(AsiaQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P4[x])
                    else:
                        n = CalcAsia(AsiaQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P4[x])
                        else:
                            n = CalcAsia(AsiaQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P4[x])
                            else:
                                n = CalcAsia(AsiaQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P4[x])
                                else:
                                    n = CalcAsia(AsiaQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P4[x])
                                    else:
                                        n = CalcAsia(AsiaQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P4[x])
                                        else:
                                            n = CalcAsia(AsiaQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P4[x])
                                            else:
                                                n = CalcAsia(AsiaQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P4[x])
                case 4:
                    n = CalcNA(NAQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P4[x])
                    else:
                        n = CalcNA(NAQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P4[x])
                        else:
                            n = CalcNA(NAQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P4[x])
                            else:
                                n = CalcNA(NAQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P4[x])
                                else:
                                    n = CalcNA(NAQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P4[x])
                                    else:
                                        n = CalcNA(NAQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P4[x])
                                        else:
                                            n = CalcNA(NAQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P4[x])
                                            else:
                                                n = CalcNA(NAQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P4[x])
                case 5:
                    n = CalcSA(SAQ, G1)
                    if n < 1 and len(G1) != 4:
                        G1.append(P4[x])
                    else:
                        n = CalcSA(SAQ, G2)
                        if n < 1 and len(G2) != 4:
                            G2.append(P4[x])
                        else:
                            n = CalcSA(SAQ, G3)
                            if n < 1 and len(G3) != 4:
                                G3.append(P4[x])
                            else:
                                n = CalcSA(SAQ, G4)
                                if n < 1 and len(G4) != 4:
                                    G4.append(P4[x])
                                else:
                                    n = CalcSA(SAQ, G5)
                                    if n < 1 and len(G5) != 4:
                                        G5.append(P4[x])
                                    else:
                                        n = CalcSA(SAQ, G6)
                                        if n < 1 and len(G6) != 4:
                                            G6.append(P4[x])
                                        else:
                                            n = CalcSA(SAQ, G7)
                                            if n < 1 and len(G7) != 4:
                                                G7.append(P4[x])
                                            else:
                                                n = CalcSA(SAQ, G8)
                                                if n < 1 and len(G8) != 4:
                                                    G8.append(P4[x])
show(i, G1, G2, G3, G4, G5, G6, G7, G8)
