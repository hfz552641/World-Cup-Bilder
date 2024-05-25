from random import randint

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


Countries = Euro + Afro + SA + NA + Asia + Oceania
Host = Countries[randint(0, len(Countries) - 1)]
print(Host)
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
print(P1)
print(P2)
print(P3)
print(P4)

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
print(G1)
print(G2)
print(G3)
print(G4)
print(G5)
print(G6)
print(G7)
print(G8)

print("Round 1 :")
print(G1[0]+" vs "+G1[1])
print(G1[2]+" vs "+G1[3])
print(G2[0]+" vs "+G2[1])
print(G2[2]+" vs "+G2[3])
print(G3[0]+" vs "+G3[1])
print(G3[2]+" vs "+G3[3])
print(G4[0]+" vs "+G4[1])
print(G4[2]+" vs "+G4[3])
print(G5[0]+" vs "+G5[1])
print(G5[2]+" vs "+G5[3])
print(G6[0]+" vs "+G6[1])
print(G6[2]+" vs "+G6[3])
print(G7[0]+" vs "+G7[1])
print(G7[2]+" vs "+G7[3])
print(G8[0]+" vs "+G8[1])
print(G8[2]+" vs "+G8[3])

print("Round 2 :")
print(G1[0]+" vs "+G1[2])
print(G1[1]+" vs "+G1[3])
print(G2[0]+" vs "+G2[2])
print(G2[1]+" vs "+G2[3])
print(G3[0]+" vs "+G3[2])
print(G3[1]+" vs "+G3[3])
print(G4[0]+" vs "+G4[2])
print(G4[1]+" vs "+G4[3])
print(G5[0]+" vs "+G5[2])
print(G5[1]+" vs "+G5[3])
print(G6[0]+" vs "+G6[2])
print(G6[1]+" vs "+G6[3])
print(G7[0]+" vs "+G7[2])
print(G7[1]+" vs "+G7[3])
print(G8[0]+" vs "+G8[2])
print(G8[1]+" vs "+G8[3])

print("Round 3 :")
print(G1[0]+" vs "+G1[3])
print(G1[1]+" vs "+G1[2])
print(G2[0]+" vs "+G2[2])
print(G2[1]+" vs "+G2[3])
print(G3[0]+" vs "+G3[2])
print(G3[1]+" vs "+G3[3])
print(G4[0]+" vs "+G4[2])
print(G4[1]+" vs "+G4[3])
print(G5[0]+" vs "+G5[2])
print(G5[1]+" vs "+G5[3])
print(G6[0]+" vs "+G6[2])
print(G6[1]+" vs "+G6[3])
print(G7[0]+" vs "+G7[2])
print(G7[1]+" vs "+G7[3])
print(G8[0]+" vs "+G8[2])
print(G8[1]+" vs "+G8[3])
