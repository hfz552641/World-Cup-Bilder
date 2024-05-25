from random import randint, shuffle
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

EuroLib = ['Albania', 'Austria', 'Belgium', 'Bosnia & Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'England', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Montenegro', 'Netherlands', 'North Macedonia', 'Northern Ireland', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'Wales']

AfroLib = ['Algeria', 'Angola', 'Benin', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Comoros', 'Congo Rep.', 'DRC', 'Egypt', 'Equatorial Guinea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Morocco', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

SALib = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

NALib = ['Bahamas', 'Barbados', 'Belize', 'Bermuda', 'Canada', 'Costa Rica', 'Cuba', 'Curaçao', 'Dominica', 'Dominican Republic', 'El Salvador', 'French Guiana', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guyana', 'Haiti', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Nicaragua', 'Panama', 'Saint Lucia', 'Snt Vincent & Gren.', 'Suriname', 'Trinidad and Tobago', 'USA']

AsiaLib = ['Australia', 'Bahrain', 'Brunei', 'Cambodia', 'China', 'India', 'Indonesia', 'Iran', 'Iraq', 'Japan', 'Jordan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar (Burma)', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkmenistan', 'UAE', 'Uzbekistan', 'Vietnam', 'Yemen']

OceaniaLib = ['Fiji', 'New Zealand', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Vanuatu']

Euro,Afro,SA,NA,Asia,Oceania=[],[],[],[],[],[]

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

def fillscrolledlist(L,sclltxt):
    Aff=""
    Aff+=L[0]
    for i in range (1,len(L)):
        Aff+="\n"+L[i]
    sclltxt.insert(tk.END,Aff)


def main12g():
    try:
        Countries = Euro + Afro + SA + NA + Asia + Oceania
        Host = Countries[randint(0, len(Countries) - 1)]
        A = find(Host)

        QEuro = []
        while len(QEuro) < 16:
            x = randint(0, len(Euro) - 1)
            while Euro[x] in QEuro or Euro[x] == Host:
                x = randint(0, len(Euro) - 1)
            (QEuro).append(Euro[x])

        MaxAfro,iMaxAfro=9,9
        MaxAsia,iMaxAsia=8,8
        MaxNA,iMaxNA=6,6
        MaxSA,iMaxSA=6,6
        MaxOce,iMaxOce=1,1


        Choice1=randint(1,5)
        match Choice1:
            case 1:
                MaxAfro+=1
            case 2:
                MaxAsia+=1
            case 3:
                MaxNA+=1
            case 4:
                MaxSA+=1
            case 5:
                MaxOce+=1

        Choice2=randint(1,5)
        Test=False
        while not(Test):
            Test=True
            match Choice2:
                case 1:
                    if MaxAfro==iMaxAfro:
                        MaxAfro+=1
                    else :
                        Test=False
                case 2:
                    if MaxAsia==iMaxAsia:
                        MaxAsia+=1
                    else :
                        Test=False
                case 3:
                    if MaxNA==iMaxNA:
                        MaxNA+=1
                    else :
                        Test=False
                case 4:
                    if MaxSA==iMaxSA:
                        MaxSA+=1
                    else :
                        Test=False
                case 5:
                    if MaxOce==iMaxOce:
                        MaxOce+=1
                    else :
                        Test=False

        QAfro = []
        while len(QAfro) < MaxAfro:
            x = randint(0, len(Afro) - 1)
            while Afro[x] in QAfro or Afro[x] == Host:
                x = randint(0, len(Afro) - 1)
            (QAfro).append(Afro[x])

        QOceania = []
        while len(QOceania) < MaxOce:
            x = randint(0, len(Oceania) - 1)
            while Oceania[x] in QOceania or Oceania[x] == Host:
                x = randint(0, len(Oceania) - 1)
            (QOceania).append(Oceania[x])


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

        print("Host :"+Host)
        print("European Countries :",end=" ")
        print(QEuro)
        print("African Countries :",end=" ")
        print(QAfro)
        print("North American Countries :",end=" ")
        print(QNA)
        print("South American Countries :",end=" ")
        print(QSA)
        print("Asian Countries :",end=" ")
        print(QAsia)
        print("Oceanian Countries :",end=" ")
        print(QOceania)

        QCountries = []
        QCountries += QEuro
        QCountries += QAfro
        QCountries += QNA
        QCountries += QSA
        QCountries += QAsia
        QCountries+=QOceania

        P=[]
        P.append(Host)
        shuffle(QCountries)
        P+=QCountries

        P1 = P[0:12]
        P2 = P[12:24]
        P3 = P[24:36]
        P4 = P[36:48]

        Test=False
        while not(Test):
            G = []
            G.append(Host)
            A2 = randint(0, 11)
            G.append(P2[A2])
            A3 = randint(0, 11)
            G.append(P3[A3])
            A4 = randint(0, 11)
            G.append(P4[A4])
            while len(G) < 48:
                A1 = randint(0, 11)
                while P1[A1] in G:
                    A1 = randint(0, 11)
                G.append(P1[A1])
                A2 = randint(0, 11)
                while P2[A2] in G:
                    A2 = randint(0, 11)
                G.append(P2[A2])
                A3 = randint(0, 11)
                while P3[A3] in G:
                    A3 = randint(0,11)
                G.append(P3[A3])
                A4 = randint(0, 11)
                while P4[A4] in G:
                    A4 = randint(0, 11)
                G.append(P4[A4])

            global G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12

            G1 = G[0:4]
            G2 = G[4:8]
            G3 = G[8:12]
            G4 = G[12:16]
            G5 = G[16:20]
            G6 = G[20:24]
            G7 = G[24:28]
            G8 = G[28:32]
            G9=G[32:36]
            G10=G[36:40]
            G11=G[40:44]
            G12=G[44:48]

            Test = (check(G1) and check(G2) and check(G3) and check(G4) and check(G4) and check(G5) and check(G6) and check(G7) and check(G8)) and check(G9) and check(G10) and check(G11) and check(G12)

            if Test :
                print(G1)
                print(G2)
                print(G3)
                print(G4)
                print(G5)
                print(G6)
                print(G7)
                print(G8)
                print(G9)
                print(G10)
                print(G11)
                print(G12)
                
                fillscrolledlist(G1,g1list)
                fillscrolledlist(G2,g2list)
                fillscrolledlist(G3,g3list)
                fillscrolledlist(G4,g4list)
                fillscrolledlist(G5,g5list)
                fillscrolledlist(G6,g6list)
                fillscrolledlist(G7,g7list)
                fillscrolledlist(G8,g8list)
                fillscrolledlist(G9,g9list)
                fillscrolledlist(G10,g10list)
                fillscrolledlist(G11,g11list)
                fillscrolledlist(G12,g12list)
                play46button.pack_forget()
                delete46button.pack(pady=5)
                schedule46.pack(pady=5)

    except Exception as e:
        main12g()


def execute12g():
    if __name__ == "__main__":
        main12g()

def clearbild12g():
    delete46button.pack_forget()
    schedule46.pack_forget()
    play46button.pack(pady=5)
    g1list.delete(1.0,tk.END)
    g2list.delete(1.0,tk.END)
    g3list.delete(1.0,tk.END)
    g4list.delete(1.0,tk.END)
    g5list.delete(1.0,tk.END)
    g6list.delete(1.0,tk.END)
    g7list.delete(1.0,tk.END)
    g8list.delete(1.0,tk.END)
    g9list.delete(1.0,tk.END)
    g10list.delete(1.0,tk.END)
    g11list.delete(1.0,tk.END)
    g12list.delete(1.0,tk.END)

def treat(G, Result, i, j, Score, GS, GC, GT):
    Teamigoals = int(Result[:Result.find("-")])
    Teamjgoals = int(Result[Result.find("-") + 1:])
    if Teamigoals > Teamjgoals:
        Score[i] = Score[i] + 3
    elif Teamjgoals > Teamigoals:
        Score[j] = Score[j] + 3
    elif Teamigoals == Teamjgoals:
        Score[i] = Score[i] + 1
        Score[j] = Score[j] + 1
    GS[i] += Teamigoals
    GS[j] += Teamjgoals
    GC[i] -= Teamjgoals
    GC[j] -= Teamigoals
    GT[i] = GS[i] + GC[i]
    GT[j] = GS[j] + GC[j]

def gotoround2_46():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != "" and match17entry.get() != "" and match18entry.get() != "" and match19entry.get() != "" and match20entry.get() != "" and match21entry.get() != "" and match22entry.get() != "" and match23entry.get() != "" and match24entry.get() != "" :
        Result = match1entry.get()
        treat(G1, Result, 0, 1, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 2, 3, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 1, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 2, 3, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 1, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 2, 3, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 1, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 2, 3, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 1, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 2, 3, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 1, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 2, 3, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 1, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 2, 3, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 1, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 2, 3, Score8, GS8, GC8, GT8)
        Result = match17entry.get()
        treat(G9, Result, 0, 1, Score9, GS9, GC9, GT9)
        Result = match18entry.get()
        treat(G9, Result, 2, 3, Score9, GS9, GC9, GT9)
        Result = match19entry.get()
        treat(G10, Result, 0, 1, Score10, GS10, GC10, GT10)
        Result = match20entry.get()
        treat(G10, Result, 2, 3, Score10, GS10, GC10, GT10)
        Result = match21entry.get()
        treat(G11, Result, 0, 1, Score11, GS11, GC11, GT11)
        Result = match22entry.get()
        treat(G11, Result, 2, 3, Score11, GS11, GC11, GT11)
        Result = match23entry.get()
        treat(G12, Result, 0, 1, Score12, GS12, GC12, GT12)
        Result = match24entry.get()
        treat(G12, Result, 2, 3, Score12, GS12, GC12, GT12)



        match1entry.delete(0, tk.END)
        match2entry.delete(0, tk.END)
        match3entry.delete(0, tk.END)
        match4entry.delete(0, tk.END)
        match5entry.delete(0, tk.END)
        match6entry.delete(0, tk.END)
        match7entry.delete(0, tk.END)
        match8entry.delete(0, tk.END)
        match9entry.delete(0, tk.END)
        match10entry.delete(0, tk.END)
        match11entry.delete(0, tk.END)
        match12entry.delete(0, tk.END)
        match13entry.delete(0, tk.END)
        match14entry.delete(0, tk.END)
        match15entry.delete(0, tk.END)
        match16entry.delete(0, tk.END)
        match17entry.delete(0, tk.END)
        match18entry.delete(0, tk.END)
        match19entry.delete(0, tk.END)
        match20entry.delete(0, tk.END)
        match21entry.delete(0, tk.END)
        match22entry.delete(0, tk.END)
        match23entry.delete(0, tk.END)
        match24entry.delete(0, tk.END)

        match1show.config(text=round2_matches[0])
        match2show.config(text=round2_matches[1])
        match3show.config(text=round2_matches[2])
        match4show.config(text=round2_matches[3])
        match5show.config(text=round2_matches[4])
        match6show.config(text=round2_matches[5])
        match7show.config(text=round2_matches[6])
        match8show.config(text=round2_matches[7])
        match9show.config(text=round2_matches[8])
        match10show.config(text=round2_matches[9])
        match11show.config(text=round2_matches[10])
        match12show.config(text=round2_matches[11])
        match13show.config(text=round2_matches[12])
        match14show.config(text=round2_matches[13])
        match15show.config(text=round2_matches[14])
        match16show.config(text=round2_matches[15])
        match17show.config(text=round2_matches[16])
        match18show.config(text=round2_matches[17])
        match19show.config(text=round2_matches[18])
        match20show.config(text=round2_matches[19])
        match21show.config(text=round2_matches[20])
        match22show.config(text=round2_matches[21])
        match23show.config(text=round2_matches[22])
        match24show.config(text=round2_matches[23])
        roundtitle.config(text="Round 2")
        round2.pack_forget()
        round3.pack(pady=5)

def gotoround3_46():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != "" and match17entry.get() != "" and match18entry.get() != "" and match19entry.get() != "" and match20entry.get() != "" and match21entry.get() != "" and match22entry.get() != "" and match23entry.get() != "" and match24entry.get() != "" :
        Result = match1entry.get()
        treat(G1, Result, 0, 2, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 1, 3, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 2, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 1, 3, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 2, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 1, 3, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 2, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 1, 3, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 2, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 1, 3, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 2, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 1, 3, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 2, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 1, 3, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 2, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 1, 3, Score8, GS8, GC8, GT8)
        Result = match17entry.get()
        treat(G9, Result, 0, 2, Score9, GS9, GC9, GT9)
        Result = match18entry.get()
        treat(G9, Result, 1, 3, Score9, GS9, GC9, GT9)
        Result = match19entry.get()
        treat(G10, Result, 0, 2, Score10, GS10, GC10, GT10)
        Result = match20entry.get()
        treat(G10, Result, 1, 3, Score10, GS10, GC10, GT10)
        Result = match21entry.get()
        treat(G11, Result, 0, 2, Score11, GS11, GC11, GT11)
        Result = match22entry.get()
        treat(G11, Result, 1, 3, Score11, GS11, GC11, GT11)
        Result = match23entry.get()
        treat(G12, Result, 0, 2, Score12, GS12, GC12, GT12)
        Result = match24entry.get()
        treat(G12, Result, 1, 3, Score12, GS12, GC12, GT12)



        match1entry.delete(0, tk.END)
        match2entry.delete(0, tk.END)
        match3entry.delete(0, tk.END)
        match4entry.delete(0, tk.END)
        match5entry.delete(0, tk.END)
        match6entry.delete(0, tk.END)
        match7entry.delete(0, tk.END)
        match8entry.delete(0, tk.END)
        match9entry.delete(0, tk.END)
        match10entry.delete(0, tk.END)
        match11entry.delete(0, tk.END)
        match12entry.delete(0, tk.END)
        match13entry.delete(0, tk.END)
        match14entry.delete(0, tk.END)
        match15entry.delete(0, tk.END)
        match16entry.delete(0, tk.END)
        match17entry.delete(0, tk.END)
        match18entry.delete(0, tk.END)
        match19entry.delete(0, tk.END)
        match20entry.delete(0, tk.END)
        match21entry.delete(0, tk.END)
        match22entry.delete(0, tk.END)
        match23entry.delete(0, tk.END)
        match24entry.delete(0, tk.END)

        match1show.config(text=round3_matches[0])
        match2show.config(text=round3_matches[1])
        match3show.config(text=round3_matches[2])
        match4show.config(text=round3_matches[3])
        match5show.config(text=round3_matches[4])
        match6show.config(text=round3_matches[5])
        match7show.config(text=round3_matches[6])
        match8show.config(text=round3_matches[7])
        match9show.config(text=round3_matches[8])
        match10show.config(text=round3_matches[9])
        match11show.config(text=round3_matches[10])
        match12show.config(text=round3_matches[11])
        match13show.config(text=round3_matches[12])
        match14show.config(text=round3_matches[13])
        match15show.config(text=round3_matches[14])
        match16show.config(text=round3_matches[15])
        match17show.config(text=round3_matches[16])
        match18show.config(text=round3_matches[17])
        match19show.config(text=round3_matches[18])
        match20show.config(text=round3_matches[19])
        match21show.config(text=round3_matches[20])
        match22show.config(text=round3_matches[21])
        match23show.config(text=round3_matches[22])
        match24show.config(text=round3_matches[23])
        roundtitle.config(text="Round 3")
        round3.pack_forget()
        finals.pack(pady=5)

def sort(G, Score, GS, GC, GT):
    Test = False
    while not(Test):
        Test = True
        for x in range(1, len(G)):
            if Score[x - 1] < Score[x]:
                Score[x - 1], Score[x] = Score[x], Score[x - 1]
                G[x - 1], G[x] = G[x], G[x - 1]
                GS[x - 1], GS[x] = GS[x], GS[x - 1]
                GC[x - 1], GC[x] = GC[x], GC[x - 1]
                GT[x - 1], GT[x] = GT[x], GT[x - 1]
                Test = False
            elif Score[x - 1] == Score[x] and GT[x - 1] < GT[x]:
                Score[x - 1], Score[x] = Score[x], Score[x - 1]
                G[x - 1], G[x] = G[x], G[x - 1]
                GS[x - 1], GS[x] = GS[x], GS[x - 1]
                GC[x - 1], GC[x] = GC[x], GC[x - 1]
                GT[x - 1], GT[x] = GT[x], GT[x - 1]
                Test = False
            elif Score[x-1]==Score[x] and GT[x-1]==GT[x] and GS[x-1]<GS[x]:
                Score[x - 1], Score[x] = Score[x], Score[x - 1]
                G[x - 1], G[x] = G[x], G[x - 1]
                GS[x - 1], GS[x] = GS[x], GS[x - 1]
                GC[x - 1], GC[x] = GC[x], GC[x - 1]
                GT[x - 1], GT[x] = GT[x], GT[x - 1]
                Test = False

def filltable(table, G, Score, GS, GC, GT):
    for i in range(len(G)):
        table.insert('', 'end', text=f'Item {i}', values=(i + 1, G[i], Score[i], GS[i], GC[i], GT[i]))

def gotogroupsoreder():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != "" and match17entry.get() != "" and match18entry.get() != "" and match19entry.get() != "" and match20entry.get() != "" and match21entry.get() != "" and match22entry.get() != "" and match23entry.get() != "" and match24entry.get() != "" :
        global G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,Gthird
        Result = match1entry.get()
        treat(G1, Result, 0, 3, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 1, 2, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 3, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 1, 2, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 3, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 1, 2, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 3, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 1, 2, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 3, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 1, 2, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 3, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 1, 2, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 3, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 1, 2, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 3, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 1, 2, Score8, GS8, GC8, GT8)
        Result = match17entry.get()
        treat(G9, Result, 0, 3, Score9, GS9, GC9, GT9)
        Result = match18entry.get()
        treat(G9, Result, 1, 2, Score9, GS9, GC9, GT9)
        Result = match19entry.get()
        treat(G10, Result, 0, 3, Score10, GS10, GC10, GT10)
        Result = match20entry.get()
        treat(G10, Result, 1, 2, Score10, GS10, GC10, GT10)
        Result = match21entry.get()
        treat(G11, Result, 0, 3, Score11, GS11, GC11, GT11)
        Result = match22entry.get()
        treat(G11, Result, 1, 2, Score11, GS11, GC11, GT11)
        Result = match23entry.get()
        treat(G12, Result, 0, 3, Score12, GS12, GC12, GT12)
        Result = match24entry.get()
        treat(G12, Result, 1, 2, Score12, GS12, GC12, GT12)

        sort(G1, Score1, GS1, GC1, GT1)
        sort(G2, Score2, GS2, GC2, GT2)
        sort(G3, Score3, GS3, GC3, GT3)
        sort(G4, Score4, GS4, GC4, GT4)
        sort(G5, Score5, GS5, GC5, GT5)
        sort(G6, Score6, GS6, GC6, GT6)
        sort(G7, Score7, GS7, GC7, GT7)
        sort(G8, Score8, GS8, GC8, GT8)
        sort(G9, Score9, GS9, GC9, GT9)
        sort(G10, Score10, GS10, GC10, GT10)
        sort(G11, Score11, GS11, GC11, GT11)
        sort(G12, Score12, GS12, GC12, GT12)

        Gthird,Scorethird,GSthird,GCthird,GTthird=[],[],[],[],[]

        Gthird.append(G1[2])
        Scorethird.append(Score1[2])
        GSthird.append(GS1[2])
        GCthird.append(GC1[2])
        GTthird.append(GT1[2])
        Gthird.append(G2[2])
        Scorethird.append(Score2[2])
        GSthird.append(GS2[2])
        GCthird.append(GC2[2])
        GTthird.append(GT2[2])
        Gthird.append(G3[2])
        Scorethird.append(Score3[2])
        GSthird.append(GS3[2])
        GCthird.append(GC3[2])
        GTthird.append(GT3[2])
        Gthird.append(G4[2])
        Scorethird.append(Score4[2])
        GSthird.append(GS4[2])
        GCthird.append(GC4[2])
        GTthird.append(GT4[2])
        Gthird.append(G5[2])
        Scorethird.append(Score5[2])
        GSthird.append(GS5[2])
        GCthird.append(GC5[2])
        GTthird.append(GT5[2])
        Gthird.append(G6[2])
        Scorethird.append(Score6[2])
        GSthird.append(GS6[2])
        GCthird.append(GC6[2])
        GTthird.append(GT6[2])
        Gthird.append(G7[2])
        Scorethird.append(Score7[2])
        GSthird.append(GS7[2])
        GCthird.append(GC7[2])
        GTthird.append(GT7[2])
        Gthird.append(G8[2])
        Scorethird.append(Score8[2])
        GSthird.append(GS8[2])
        GCthird.append(GC8[2])
        GTthird.append(GT8[2])
        Gthird.append(G9[2])
        Scorethird.append(Score9[2])
        GSthird.append(GS9[2])
        GCthird.append(GC9[2])
        GTthird.append(GT9[2])
        Gthird.append(G10[2])
        Scorethird.append(Score10[2])
        GSthird.append(GS10[2])
        GCthird.append(GC10[2])
        GTthird.append(GT10[2])
        Gthird.append(G11[2])
        Scorethird.append(Score11[2])
        GSthird.append(GS11[2])
        GCthird.append(GC11[2])
        GTthird.append(GT11[2])
        Gthird.append(G12[2])
        Scorethird.append(Score12[2])
        GSthird.append(GS12[2])
        GCthird.append(GC12[2])
        GTthird.append(GT12[2])

        sort(Gthird, Scorethird, GSthird, GCthird, GTthird)

        schedule46window.destroy()

        table46=tk.Tk()
        table46.title("Table results")

        tableframes=tk.Frame(table46)
        g1tableframe=tk.Frame(tableframes)

        g1name=tk.Label(g1tableframe,text='G1')
        table1 = ttk.Treeview(g1tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table1.heading('#1', text='Rank')
        table1.heading('#2', text='Country')
        table1.heading('#3', text='Score')
        table1.heading('#4', text='GS')
        table1.heading('#5', text='GC')
        table1.heading('#6', text='GT')
        table1.column('#1', width=30)
        table1.column('#2', width=70)
        table1.column('#3', width=30)
        table1.column('#4', width=30)
        table1.column('#5', width=30)
        table1.column('#6', width=30)
        g1name.pack(pady=5)
        table1.pack()
        filltable(table1, G1, Score1, GS1, GC1, GT1)

        g2tableframe=tk.Frame(tableframes)
        g2name=tk.Label(g2tableframe,text='G2')
        table2 = ttk.Treeview(g2tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table2.heading('#1', text='Rank')
        table2.heading('#2', text='Country')
        table2.heading('#3', text='Score')
        table2.heading('#4', text='GS')
        table2.heading('#5', text='GC')
        table2.heading('#6', text='GT')
        table2.column('#1', width=30)
        table2.column('#2', width=70)
        table2.column('#3', width=30)
        table2.column('#4', width=30)
        table2.column('#5', width=30)
        table2.column('#6', width=30)
        g2name.pack(pady=5)
        table2.pack()
        filltable(table2, G2, Score2, GS2, GC2, GT2)

        g3tableframe=tk.Frame(tableframes)
        g3name=tk.Label(g3tableframe,text='G3')
        table3 = ttk.Treeview(g3tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table3.heading('#1', text='Rank')
        table3.heading('#2', text='Country')
        table3.heading('#3', text='Score')
        table3.heading('#4', text='GS')
        table3.heading('#5', text='GC')
        table3.heading('#6', text='GT')
        table3.column('#1', width=30)
        table3.column('#2', width=70)
        table3.column('#3', width=30)
        table3.column('#4', width=30)
        table3.column('#5', width=30)
        table3.column('#6', width=30)
        g3name.pack(pady=5)
        table3.pack()
        filltable(table3, G3, Score3, GS3, GC3, GT3)

        g4tableframe=tk.Frame(tableframes)
        g4name=tk.Label(g4tableframe,text='G4')
        table4 = ttk.Treeview(g4tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table4.heading('#1', text='Rank')
        table4.heading('#2', text='Country')
        table4.heading('#3', text='Score')
        table4.heading('#4', text='GS')
        table4.heading('#5', text='GC')
        table4.heading('#6', text='GT')
        table4.column('#1', width=30)
        table4.column('#2', width=70)
        table4.column('#3', width=30)
        table4.column('#4', width=30)
        table4.column('#5', width=30)
        table4.column('#6', width=30)
        g4name.pack(pady=5)
        table4.pack()
        filltable(table4, G4, Score4, GS4, GC4, GT4)

        g5tableframe=tk.Frame(tableframes)
        g5name=tk.Label(g5tableframe,text='G5')
        table5 = ttk.Treeview(g5tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table5.heading('#1', text='Rank')
        table5.heading('#2', text='Country')
        table5.heading('#3', text='Score')
        table5.heading('#4', text='GS')
        table5.heading('#5', text='GC')
        table5.heading('#6', text='GT')
        table5.column('#1', width=30)
        table5.column('#2', width=70)
        table5.column('#3', width=30)
        table5.column('#4', width=30)
        table5.column('#5', width=30)
        table5.column('#6', width=30)
        g5name.pack(pady=5)
        table5.pack()
        filltable(table5, G5, Score5, GS5, GC5, GT5)

        g6tableframe=tk.Frame(tableframes)
        g6name=tk.Label(g6tableframe,text='G6')
        table6 = ttk.Treeview(g6tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table6.heading('#1', text='Rank')
        table6.heading('#2', text='Country')
        table6.heading('#3', text='Score')
        table6.heading('#4', text='GS')
        table6.heading('#5', text='GC')
        table6.heading('#6', text='GT')
        table6.column('#1', width=30)
        table6.column('#2', width=70)
        table6.column('#3', width=30)
        table6.column('#4', width=30)
        table6.column('#5', width=30)
        table6.column('#6', width=30)
        g6name.pack(pady=5)
        table6.pack()
        filltable(table6, G6, Score6, GS6, GC6, GT6)

        g7tableframe=tk.Frame(tableframes)
        g7name=tk.Label(g7tableframe,text='G7')
        table7 = ttk.Treeview(g7tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table7.heading('#1', text='Rank')
        table7.heading('#2', text='Country')
        table7.heading('#3', text='Score')
        table7.heading('#4', text='GS')
        table7.heading('#5', text='GC')
        table7.heading('#6', text='GT')
        table7.column('#1', width=30)
        table7.column('#2', width=70)
        table7.column('#3', width=30)
        table7.column('#4', width=30)
        table7.column('#5', width=30)
        table7.column('#6', width=30)
        g7name.pack(pady=5)
        table7.pack()
        filltable(table7, G7, Score7, GS7, GC7, GT7)

        g8tableframe=tk.Frame(tableframes)
        g8name=tk.Label(g8tableframe,text='G8')
        table8 = ttk.Treeview(g8tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table8.heading('#1', text='Rank')
        table8.heading('#2', text='Country')
        table8.heading('#3', text='Score')
        table8.heading('#4', text='GS')
        table8.heading('#5', text='GC')
        table8.heading('#6', text='GT')
        table8.column('#1', width=30)
        table8.column('#2', width=70)
        table8.column('#3', width=30)
        table8.column('#4', width=30)
        table8.column('#5', width=30)
        table8.column('#6', width=30)
        g8name.pack(pady=5)
        table8.pack()
        filltable(table8, G8, Score8, GS8, GC8, GT8)

        g9tableframe=tk.Frame(tableframes)
        g9name=tk.Label(g9tableframe,text='G9')
        table9 = ttk.Treeview(g9tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table9.heading('#1', text='Rank')
        table9.heading('#2', text='Country')
        table9.heading('#3', text='Score')
        table9.heading('#4', text='GS')
        table9.heading('#5', text='GC')
        table9.heading('#6', text='GT')
        table9.column('#1', width=30)
        table9.column('#2', width=70)
        table9.column('#3', width=30)
        table9.column('#4', width=30)
        table9.column('#5', width=30)
        table9.column('#6', width=30)
        g9name.pack(pady=5)
        table9.pack()
        filltable(table9, G9, Score9, GS9, GC9, GT9)

        g10tableframe=tk.Frame(tableframes)
        g10name=tk.Label(g10tableframe,text='G10')
        table10 = ttk.Treeview(g10tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table10.heading('#1', text='Rank')
        table10.heading('#2', text='Country')
        table10.heading('#3', text='Score')
        table10.heading('#4', text='GS')
        table10.heading('#5', text='GC')
        table10.heading('#6', text='GT')
        table10.column('#1', width=30)
        table10.column('#2', width=70)
        table10.column('#3', width=30)
        table10.column('#4', width=30)
        table10.column('#5', width=30)
        table10.column('#6', width=30)
        g10name.pack(pady=5)
        table10.pack()
        filltable(table10, G10, Score10, GS10, GC10, GT10)

        g11tableframe=tk.Frame(tableframes)
        g11name=tk.Label(g11tableframe,text='G11')
        table11 = ttk.Treeview(g11tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table11.heading('#1', text='Rank')
        table11.heading('#2', text='Country')
        table11.heading('#3', text='Score')
        table11.heading('#4', text='GS')
        table11.heading('#5', text='GC')
        table11.heading('#6', text='GT')
        table11.column('#1', width=30)
        table11.column('#2', width=70)
        table11.column('#3', width=30)
        table11.column('#4', width=30)
        table11.column('#5', width=30)
        table11.column('#6', width=30)
        g11name.pack(pady=5)
        table11.pack()
        filltable(table11, G11, Score11, GS11, GC11, GT11)

        g12tableframe=tk.Frame(tableframes)
        g12name=tk.Label(g12tableframe,text='G12')
        table12 = ttk.Treeview(g12tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table12.heading('#1', text='Rank')
        table12.heading('#2', text='Country')
        table12.heading('#3', text='Score')
        table12.heading('#4', text='GS')
        table12.heading('#5', text='GC')
        table12.heading('#6', text='GT')
        table12.column('#1', width=30)
        table12.column('#2', width=70)
        table12.column('#3', width=30)
        table12.column('#4', width=30)
        table12.column('#5', width=30)
        table12.column('#6', width=30)
        g12name.pack(pady=5)
        table12.pack()
        filltable(table12, G12, Score12, GS12, GC12, GT12)

        thirdtableframe=tk.Frame(tableframes)
        thirdname=tk.Label(thirdtableframe,text='Third countries ranking')
        tablethird = ttk.Treeview(thirdtableframe, height=13, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        tablethird.heading('#1', text='Rank')
        tablethird.heading('#2', text='Country')
        tablethird.heading('#3', text='Score')
        tablethird.heading('#4', text='GS')
        tablethird.heading('#5', text='GC')
        tablethird.heading('#6', text='GT')
        tablethird.column('#1', width=30)
        tablethird.column('#2', width=70)
        tablethird.column('#3', width=30)
        tablethird.column('#4', width=30)
        tablethird.column('#5', width=30)
        tablethird.column('#6', width=30)
        thirdname.pack(pady=5)
        tablethird.pack()
        filltable(tablethird, Gthird, Scorethird, GSthird, GCthird, GTthird)

        g1tableframe.grid(row=1,column=1,padx=3,pady=3)
        g2tableframe.grid(row=1,column=2,padx=3,pady=3)
        g3tableframe.grid(row=1,column=3,padx=3,pady=3)
        g4tableframe.grid(row=1,column=4,padx=3,pady=3)
        g5tableframe.grid(row=2,column=1,padx=3,pady=3)
        g6tableframe.grid(row=2,column=2,padx=3,pady=3)
        g7tableframe.grid(row=2,column=3,padx=3,pady=3)
        g8tableframe.grid(row=2,column=4,padx=3,pady=3)
        g9tableframe.grid(row=3,column=1,padx=3,pady=3)
        g10tableframe.grid(row=3,column=2,padx=3,pady=3)
        g11tableframe.grid(row=3,column=3,padx=3,pady=3)
        g12tableframe.grid(row=3,column=4,padx=3,pady=3)
        thirdtableframe.grid(row=1,column=5,rowspan=3,padx=3,pady=3)
        
        global round32button

        round32button=tk.Button(table46,text="Round of 32",command=gotoround32_46)

        tableframes.pack()
        round32button.pack(pady=5)

        table46.mainloop()

def checkseq(L):
    Ok=True
    for i in range(len(L)-2):
        if L[i][0]==L[i+1][0] or L[i][0]==L[i+2][0]:
            Ok=False
    return Ok

def gotoround32_46():
    
    seq1=[]
    seq2=[]

    seq1.append("A1")
    seq2.append("A2")

    seq2.append("B1")
    seq1.append("B2")

    seq1.append("C1")
    seq2.append("C2")

    seq2.append("D1")
    seq1.append("D2")

    seq1.append("E1")
    seq2.append("E2")

    seq2.append("F1")
    seq1.append("F2")

    seq1.append("G1")
    seq2.append("G2")

    seq2.append("H1")
    seq1.append("H2")

    seq1.append("I1")
    seq2.append("I2")

    seq2.append("J1")
    seq1.append("J2")

    seq1.append("K1")
    seq2.append("K2")

    seq2.append("L1")
    seq1.append("L2")

    print(seq1)
    print(seq2)

    Test,Rlist=False,[]
    while not(Test):
        A=randint(1,8)
        Choice="R"+str(A)
        while Choice in Rlist:
            A=randint(1,8)
            Choice="R"+str(A)
        Rlist.append(Choice)
        Test=(len(Rlist)==8)

    seq1=seq1+Rlist[0:4]
    seq2=seq2+Rlist[4:8]

    shuffle(seq1)
    while not(checkseq(seq1)):
        shuffle(seq1)

    shuffle(seq2)
    while not(checkseq(seq2)):
        shuffle(seq2)

    seq=seq1+seq2

    global Qround32

    Qround32=[]
    for i in range(32):
        b=seq[i]
        A=b[0]
        p=b[1]
        match A :
            case "A":
                Qround32.append(G1[int(p)-1])
            case "B":
                Qround32.append(G2[int(p)-1])
            case "C":
                Qround32.append(G3[int(p)-1])
            case "D":
                Qround32.append(G4[int(p)-1])
            case "E":
                Qround32.append(G5[int(p)-1])
            case "F":
                Qround32.append(G6[int(p)-1])
            case "G":
                Qround32.append(G7[int(p)-1])
            case "H":
                Qround32.append(G8[int(p)-1])
            case "I":
                Qround32.append(G9[int(p)-1])
            case "J":
                Qround32.append(G10[int(p)-1])
            case "K":
                Qround32.append(G11[int(p)-1])
            case "L":
                Qround32.append(G12[int(p)-1])
            case "R":
                Qround32.append(Gthird[int(p)-1])

    round32_matches=[
        Qround32[0]+" vs "+Qround32[1],
        Qround32[2]+" vs "+Qround32[3],
        Qround32[4]+" vs "+Qround32[5],
        Qround32[6]+" vs "+Qround32[7],
        Qround32[8]+" vs "+Qround32[9],
        Qround32[10]+" vs "+Qround32[11],
        Qround32[12]+" vs "+Qround32[13],
        Qround32[14]+" vs "+Qround32[15],
        Qround32[16]+" vs "+Qround32[17],
        Qround32[18]+" vs "+Qround32[19],
        Qround32[20]+" vs "+Qround32[21],
        Qround32[22]+" vs "+Qround32[23],
        Qround32[24]+" vs "+Qround32[25],
        Qround32[26]+" vs "+Qround32[27],
        Qround32[28]+" vs "+Qround32[29],
        Qround32[30]+" vs "+Qround32[31]]
    
    round32button.pack_forget()

    global finals46root,finalscheduleroot

    finalscheduleroot=tk.Toplevel()
    finalscheduleroot.title("Finals matches")

    global finalsmatchesframe,finalstitle

    finalstitle=tk.Label(finalscheduleroot,text="Round of 32")
    finalsmatchesframe=tk.Frame(finalscheduleroot)
    
    global finalsmatch1,finalsmatch1entry,finalsmatch2,finalsmatch2entry,finalsmatch3,finalsmatch3entry,finalsmatch4,finalsmatch4entry,finalsmatch5,finalsmatch5entry,finalsmatch6,finalsmatch6entry,finalsmatch7,finalsmatch7entry,finalsmatch8,finalsmatch8entry,finalsmatch9,finalsmatch9entry,finalsmatch10,finalsmatch10entry,finalsmatch11,finalsmatch11entry,finalsmatch12,finalsmatch12entry,finalsmatch13,finalsmatch13entry,finalsmatch14,finalsmatch14entry,finalsmatch15,finalsmatch15entry,finalsmatch16,finalsmatch16entry

    finalsmatch1=tk.Label(finalsmatchesframe,text=round32_matches[0])
    finalsmatch1entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch1.grid(row=1,column=1)
    finalsmatch1entry.grid(row=1,column=2)
    finalsmatch2=tk.Label(finalsmatchesframe,text=round32_matches[1])
    finalsmatch2entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch2.grid(row=2,column=1)
    finalsmatch2entry.grid(row=2,column=2)
    finalsmatch3=tk.Label(finalsmatchesframe,text=round32_matches[2])
    finalsmatch3entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch3.grid(row=3,column=1)
    finalsmatch3entry.grid(row=3,column=2)
    finalsmatch4=tk.Label(finalsmatchesframe,text=round32_matches[3])
    finalsmatch4entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch4.grid(row=4,column=1)
    finalsmatch4entry.grid(row=4,column=2)
    finalsmatch5=tk.Label(finalsmatchesframe,text=round32_matches[4])
    finalsmatch5entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch5.grid(row=5,column=1)
    finalsmatch5entry.grid(row=5,column=2)
    finalsmatch6=tk.Label(finalsmatchesframe,text=round32_matches[5])
    finalsmatch6entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch6.grid(row=6,column=1)
    finalsmatch6entry.grid(row=6,column=2)
    finalsmatch7=tk.Label(finalsmatchesframe,text=round32_matches[6])
    finalsmatch7entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch7.grid(row=7,column=1)
    finalsmatch7entry.grid(row=7,column=2)
    finalsmatch8=tk.Label(finalsmatchesframe,text=round32_matches[7])
    finalsmatch8entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch8.grid(row=8,column=1)
    finalsmatch8entry.grid(row=8,column=2)
    finalsmatch9=tk.Label(finalsmatchesframe,text=round32_matches[8])
    finalsmatch9entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch9.grid(row=9,column=1)
    finalsmatch9entry.grid(row=9,column=2)
    finalsmatch10=tk.Label(finalsmatchesframe,text=round32_matches[9])
    finalsmatch10entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch10.grid(row=10,column=1)
    finalsmatch10entry.grid(row=10,column=2)
    finalsmatch11=tk.Label(finalsmatchesframe,text=round32_matches[10])
    finalsmatch11entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch11.grid(row=11,column=1)
    finalsmatch11entry.grid(row=11,column=2)
    finalsmatch12=tk.Label(finalsmatchesframe,text=round32_matches[11])
    finalsmatch12entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch12.grid(row=12,column=1)
    finalsmatch12entry.grid(row=12,column=2)
    finalsmatch13=tk.Label(finalsmatchesframe,text=round32_matches[12])
    finalsmatch13entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch13.grid(row=13,column=1)
    finalsmatch13entry.grid(row=13,column=2)
    finalsmatch14=tk.Label(finalsmatchesframe,text=round32_matches[13])
    finalsmatch14entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch14.grid(row=14,column=1)
    finalsmatch14entry.grid(row=14,column=2)
    finalsmatch15=tk.Label(finalsmatchesframe,text=round32_matches[14])
    finalsmatch15entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch15.grid(row=15,column=1)
    finalsmatch15entry.grid(row=15,column=2)
    finalsmatch16=tk.Label(finalsmatchesframe,text=round32_matches[15])
    finalsmatch16entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch16.grid(row=16,column=1)
    finalsmatch16entry.grid(row=16,column=2)

    global round16

    round16=tk.Button(finalscheduleroot,text="Round 16",command=gotoround16_46)

    finalstitle.pack(pady=5)
    finalsmatchesframe.pack(pady=5)
    round16.pack(pady=5)

    finals46root=tk.Toplevel()
    finals46root.title("Finals Draw")

    country46_1_32=tk.Label(finals46root,text=Qround32[0])
    country46_2_32=tk.Label(finals46root,text=Qround32[1])
    country46_3_32=tk.Label(finals46root,text=Qround32[2])
    country46_4_32=tk.Label(finals46root,text=Qround32[3])
    country46_5_32=tk.Label(finals46root,text=Qround32[4])
    country46_6_32=tk.Label(finals46root,text=Qround32[5])
    country46_7_32=tk.Label(finals46root,text=Qround32[6])
    country46_8_32=tk.Label(finals46root,text=Qround32[7])
    country46_9_32=tk.Label(finals46root,text=Qround32[8])
    country46_10_32=tk.Label(finals46root,text=Qround32[9])
    country46_11_32=tk.Label(finals46root,text=Qround32[10])
    country46_12_32=tk.Label(finals46root,text=Qround32[11])
    country46_13_32=tk.Label(finals46root,text=Qround32[12])
    country46_14_32=tk.Label(finals46root,text=Qround32[13])
    country46_15_32=tk.Label(finals46root,text=Qround32[14])
    country46_16_32=tk.Label(finals46root,text=Qround32[15])
    country46_17_32=tk.Label(finals46root,text=Qround32[16])
    country46_18_32=tk.Label(finals46root,text=Qround32[17])
    country46_19_32=tk.Label(finals46root,text=Qround32[18])
    country46_20_32=tk.Label(finals46root,text=Qround32[19])
    country46_21_32=tk.Label(finals46root,text=Qround32[20])
    country46_22_32=tk.Label(finals46root,text=Qround32[21])
    country46_23_32=tk.Label(finals46root,text=Qround32[22])
    country46_24_32=tk.Label(finals46root,text=Qround32[23])
    country46_25_32=tk.Label(finals46root,text=Qround32[24])
    country46_26_32=tk.Label(finals46root,text=Qround32[25])
    country46_27_32=tk.Label(finals46root,text=Qround32[26])
    country46_28_32=tk.Label(finals46root,text=Qround32[27])
    country46_29_32=tk.Label(finals46root,text=Qround32[28])
    country46_30_32=tk.Label(finals46root,text=Qround32[29])
    country46_31_32=tk.Label(finals46root,text=Qround32[30])
    country46_32_32=tk.Label(finals46root,text=Qround32[31])

    country46_1_32.grid(row=1,column=1)
    country46_2_32.grid(row=2,column=1)
    country46_3_32.grid(row=3,column=1)
    country46_4_32.grid(row=4,column=1)
    country46_5_32.grid(row=5,column=1)
    country46_6_32.grid(row=6,column=1)
    country46_7_32.grid(row=7,column=1)
    country46_8_32.grid(row=8,column=1)
    country46_9_32.grid(row=9,column=1)
    country46_10_32.grid(row=10,column=1)
    country46_11_32.grid(row=11,column=1)
    country46_12_32.grid(row=12,column=1)
    country46_13_32.grid(row=13,column=1)
    country46_14_32.grid(row=14,column=1)
    country46_15_32.grid(row=15,column=1)
    country46_16_32.grid(row=16,column=1)
    country46_17_32.grid(row=1,column=10)
    country46_18_32.grid(row=2,column=10)
    country46_19_32.grid(row=3,column=10)
    country46_20_32.grid(row=4,column=10)
    country46_21_32.grid(row=5,column=10)
    country46_22_32.grid(row=6,column=10)
    country46_23_32.grid(row=7,column=10)
    country46_24_32.grid(row=8,column=10)
    country46_25_32.grid(row=9,column=10)
    country46_26_32.grid(row=10,column=10)
    country46_27_32.grid(row=11,column=10)
    country46_28_32.grid(row=12,column=10)
    country46_29_32.grid(row=13,column=10)
    country46_30_32.grid(row=14,column=10)
    country46_31_32.grid(row=15,column=10)
    country46_32_32.grid(row=16,column=10)

def treatfinals(Result, Qinit, i, j, Qfinal):
    teamigoals = int(Result[:Result.find("-")])
    teamjgoals = int(Result[Result.find("-") + 1:])
    if teamigoals < teamjgoals:
        Qfinal.append(Qinit[j])
    elif teamigoals > teamjgoals:
        Qfinal.append(Qinit[i])
    elif teamigoals==teamjgoals:
        Choice=randint(0,1)
        if Choice==0:
            Qfinal.append(Qinit[i])
        else :
            Qfinal.append(Qinit[j])

def gotoround16_46():
    if match1entry!='' and match2entry!='' and match3entry!='' and match4entry!='' and match5entry!='' and match6entry!='' and match7entry!='' and match8entry!='' and match9entry!='' and match10entry!='' and match11entry!='' and match12entry!='' and match13entry!='' and match14entry!='' and match15entry!='' and match16entry!='' :
        finalstitle.config(text="Round of 16")
        global Qround16
        
        Qround16=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qround32,0,1,Qround16)
        Result=finalsmatch2entry.get()
        treatfinals(Result,Qround32,2,3,Qround16)
        Result=finalsmatch3entry.get()
        treatfinals(Result,Qround32,4,5,Qround16)
        Result=finalsmatch4entry.get()
        treatfinals(Result,Qround32,6,7,Qround16)
        Result=finalsmatch5entry.get()
        treatfinals(Result,Qround32,8,9,Qround16)
        Result=finalsmatch6entry.get()
        treatfinals(Result,Qround32,10,11,Qround16)
        Result=finalsmatch7entry.get()
        treatfinals(Result,Qround32,12,13,Qround16)
        Result=finalsmatch8entry.get()
        treatfinals(Result,Qround32,14,15,Qround16)
        Result=finalsmatch9entry.get()
        treatfinals(Result,Qround32,16,17,Qround16)
        Result=finalsmatch10entry.get()
        treatfinals(Result,Qround32,18,19,Qround16)
        Result=finalsmatch11entry.get()
        treatfinals(Result,Qround32,20,21,Qround16)
        Result=finalsmatch12entry.get()
        treatfinals(Result,Qround32,22,23,Qround16)
        Result=finalsmatch13entry.get()
        treatfinals(Result,Qround32,24,25,Qround16)
        Result=finalsmatch14entry.get()
        treatfinals(Result,Qround32,26,27,Qround16)
        Result=finalsmatch15entry.get()
        treatfinals(Result,Qround32,28,29,Qround16)
        Result=finalsmatch16entry.get()
        treatfinals(Result,Qround32,30,31,Qround16)

        round16_matches=[
            Qround16[0]+" vs "+Qround16[1],
            Qround16[2]+" vs "+Qround16[3],
            Qround16[4]+" vs "+Qround16[5],
            Qround16[6]+" vs "+Qround16[7],
            Qround16[8]+" vs "+Qround16[9],
            Qround16[10]+" vs "+Qround16[11],
            Qround16[12]+" vs "+Qround16[13],
            Qround16[14]+" vs "+Qround16[15],
        ]

        finalsmatch1entry.delete(0,tk.END)
        finalsmatch2entry.delete(0,tk.END)
        finalsmatch3entry.delete(0,tk.END)
        finalsmatch4entry.delete(0,tk.END)
        finalsmatch5entry.delete(0,tk.END)
        finalsmatch6entry.delete(0,tk.END)
        finalsmatch7entry.delete(0,tk.END)
        finalsmatch8entry.delete(0,tk.END)
        finalsmatch1.config(text=round16_matches[0])
        finalsmatch2.config(text=round16_matches[1])
        finalsmatch3.config(text=round16_matches[2])
        finalsmatch4.config(text=round16_matches[3])
        finalsmatch5.config(text=round16_matches[4])
        finalsmatch6.config(text=round16_matches[5])
        finalsmatch7.config(text=round16_matches[6])
        finalsmatch8.config(text=round16_matches[7])
        
        finalsmatch9.grid_forget()
        finalsmatch9entry.grid_forget()
        finalsmatch10.grid_forget()
        finalsmatch10entry.grid_forget()
        finalsmatch11.grid_forget()
        finalsmatch11entry.grid_forget()
        finalsmatch12.grid_forget()
        finalsmatch12entry.grid_forget()
        finalsmatch13.grid_forget()
        finalsmatch13entry.grid_forget()
        finalsmatch14.grid_forget()
        finalsmatch14entry.grid_forget()
        finalsmatch15.grid_forget()
        finalsmatch15entry.grid_forget()
        finalsmatch16.grid_forget()
        finalsmatch16entry.grid_forget()

        country46_1_16=tk.Label(finals46root,text=Qround16[0])
        country46_2_16=tk.Label(finals46root,text=Qround16[1])
        country46_3_16=tk.Label(finals46root,text=Qround16[2])
        country46_4_16=tk.Label(finals46root,text=Qround16[3])
        country46_5_16=tk.Label(finals46root,text=Qround16[4])
        country46_6_16=tk.Label(finals46root,text=Qround16[5])
        country46_7_16=tk.Label(finals46root,text=Qround16[6])
        country46_8_16=tk.Label(finals46root,text=Qround16[7])
        country46_9_16=tk.Label(finals46root,text=Qround16[8])
        country46_10_16=tk.Label(finals46root,text=Qround16[9])
        country46_11_16=tk.Label(finals46root,text=Qround16[10])
        country46_12_16=tk.Label(finals46root,text=Qround16[11])
        country46_13_16=tk.Label(finals46root,text=Qround16[12])
        country46_14_16=tk.Label(finals46root,text=Qround16[13])
        country46_15_16=tk.Label(finals46root,text=Qround16[14])
        country46_16_16=tk.Label(finals46root,text=Qround16[15])

        country46_1_16.grid(row=1,column=2,rowspan=2)
        country46_2_16.grid(row=3,column=2,rowspan=2)
        country46_3_16.grid(row=5,column=2,rowspan=2)
        country46_4_16.grid(row=7,column=2,rowspan=2)
        country46_5_16.grid(row=9,column=2,rowspan=2)
        country46_6_16.grid(row=11,column=2,rowspan=2)
        country46_7_16.grid(row=13,column=2,rowspan=2)
        country46_8_16.grid(row=15,column=2,rowspan=2)
        country46_9_16.grid(row=1,column=9,rowspan=2)
        country46_10_16.grid(row=3,column=9,rowspan=2)
        country46_11_16.grid(row=5,column=9,rowspan=2)
        country46_12_16.grid(row=7,column=9,rowspan=2)
        country46_13_16.grid(row=9,column=9,rowspan=2)
        country46_14_16.grid(row=11,column=9,rowspan=2)
        country46_15_16.grid(row=13,column=9,rowspan=2)
        country46_16_16.grid(row=15,column=9,rowspan=2)

        global round8

        round16.pack_forget()
        round8=tk.Button(finalscheduleroot,text="1/4 Final",command=gotoround8_46)
        round8.pack(pady=5)

def gotoround8_46():
    if match1entry!='' and match2entry!='' and match3entry!='' and match4entry!='' and match5entry!='' and match6entry!='' and match7entry!='' and match8entry!='' :
        finalstitle.config(text="1/4 Final")
        global Qround8
        
        Qround8=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qround16,0,1,Qround8)
        Result=finalsmatch2entry.get()
        treatfinals(Result,Qround16,2,3,Qround8)
        Result=finalsmatch3entry.get()
        treatfinals(Result,Qround16,4,5,Qround8)
        Result=finalsmatch4entry.get()
        treatfinals(Result,Qround16,6,7,Qround8)
        Result=finalsmatch5entry.get()
        treatfinals(Result,Qround16,8,9,Qround8)
        Result=finalsmatch6entry.get()
        treatfinals(Result,Qround16,10,11,Qround8)
        Result=finalsmatch7entry.get()
        treatfinals(Result,Qround16,12,13,Qround8)
        Result=finalsmatch8entry.get()
        treatfinals(Result,Qround16,14,15,Qround8)

        round8_matches=[
            Qround8[0]+" vs "+Qround8[1],
            Qround8[2]+" vs "+Qround8[3],
            Qround8[4]+" vs "+Qround8[5],
            Qround8[6]+" vs "+Qround8[7]
        ]

        finalsmatch1entry.delete(0,tk.END)
        finalsmatch2entry.delete(0,tk.END)
        finalsmatch3entry.delete(0,tk.END)
        finalsmatch4entry.delete(0,tk.END)
        finalsmatch1.config(text=round8_matches[0])
        finalsmatch2.config(text=round8_matches[1])
        finalsmatch3.config(text=round8_matches[2])
        finalsmatch4.config(text=round8_matches[3])
        
        finalsmatch5.grid_forget()
        finalsmatch5entry.grid_forget()
        finalsmatch6.grid_forget()
        finalsmatch6entry.grid_forget()
        finalsmatch7.grid_forget()
        finalsmatch7entry.grid_forget()
        finalsmatch8.grid_forget()
        finalsmatch8entry.grid_forget()

        country46_1_8=tk.Label(finals46root,text=Qround8[0])
        country46_2_8=tk.Label(finals46root,text=Qround8[1])
        country46_3_8=tk.Label(finals46root,text=Qround8[2])
        country46_4_8=tk.Label(finals46root,text=Qround8[3])
        country46_5_8=tk.Label(finals46root,text=Qround8[4])
        country46_6_8=tk.Label(finals46root,text=Qround8[5])
        country46_7_8=tk.Label(finals46root,text=Qround8[6])
        country46_8_8=tk.Label(finals46root,text=Qround8[7])

        country46_1_8.grid(row=1,column=3,rowspan=4)
        country46_2_8.grid(row=5,column=3,rowspan=4)
        country46_3_8.grid(row=9,column=3,rowspan=4)
        country46_4_8.grid(row=13,column=3,rowspan=4)
        country46_5_8.grid(row=1,column=8,rowspan=4)
        country46_6_8.grid(row=5,column=8,rowspan=4)
        country46_7_8.grid(row=9,column=8,rowspan=4)
        country46_8_8.grid(row=13,column=8,rowspan=4)

        global round4

        round8.pack_forget()
        round4=tk.Button(finalscheduleroot,text="1/2 Final",command=gotoround4_46)
        round4.pack(pady=5)

def gotoround4_46():
    if match1entry!='' and match2entry!='' and match3entry!='' and match4entry!='' :
        finalstitle.config(text="1/2 Final")
        global Qround4
        
        Qround4=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qround8,0,1,Qround4)
        Result=finalsmatch2entry.get()
        treatfinals(Result,Qround8,2,3,Qround4)
        Result=finalsmatch3entry.get()
        treatfinals(Result,Qround8,4,5,Qround4)
        Result=finalsmatch4entry.get()
        treatfinals(Result,Qround8,6,7,Qround4)

        round4_matches=[
            Qround4[0]+" vs "+Qround4[1],
            Qround4[2]+" vs "+Qround4[3]
        ]

        finalsmatch1entry.delete(0,tk.END)
        finalsmatch2entry.delete(0,tk.END)
        finalsmatch1.config(text=round4_matches[0])
        finalsmatch2.config(text=round4_matches[1])
        
        finalsmatch3.grid_forget()
        finalsmatch3entry.grid_forget()
        finalsmatch4.grid_forget()
        finalsmatch4entry.grid_forget()

        country46_1_4=tk.Label(finals46root,text=Qround4[0])
        country46_2_4=tk.Label(finals46root,text=Qround4[1])
        country46_3_4=tk.Label(finals46root,text=Qround4[2])
        country46_4_4=tk.Label(finals46root,text=Qround4[3])

        country46_1_4.grid(row=1,column=4,rowspan=8)
        country46_2_4.grid(row=9,column=4,rowspan=8)
        country46_3_4.grid(row=1,column=7,rowspan=8)
        country46_4_4.grid(row=9,column=7,rowspan=8)

        global roundfinal

        round4.pack_forget()
        roundfinal=tk.Button(finalscheduleroot,text="Final",command=gotofinal_46)
        roundfinal.pack(pady=5)

def gotofinal_46():
    if match1entry!='' and match2entry!='' :
        finalstitle.config(text="Final")
        global Qroundfinal
        
        Qroundfinal=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qround4,0,1,Qroundfinal)
        Result=finalsmatch2entry.get()
        treatfinals(Result,Qround4,2,3,Qroundfinal)

        roundfinal_matches=[
            Qroundfinal[0]+" vs "+Qroundfinal[1]
        ]

        finalsmatch1entry.delete(0,tk.END)
        finalsmatch1.config(text=roundfinal_matches[0])
        
        finalsmatch2.grid_forget()
        finalsmatch2entry.grid_forget()

        country46_1_f=tk.Label(finals46root,text=Qroundfinal[0])
        country46_2_f=tk.Label(finals46root,text=Qroundfinal[1])

        country46_1_f.grid(row=1,column=5,rowspan=16)
        country46_2_f.grid(row=1,column=6,rowspan=16)

        global endwc

        roundfinal.pack_forget()
        endwc=tk.Button(finalscheduleroot,text="Final",command=endworldcup_46)
        endwc.pack(pady=5)

def endworldcup_46():
    if match1entry!='' :
        finalstitle.config(text="End of world cup")
        global Winner
        
        Winner=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qroundfinal,0,1,Winner)

        finalscheduleroot.destroy()

        country46_1_f=tk.Label(finals46root,text=Winner[0])

        country46_1_f.grid(row=7,column=5,columnspan=2)



def showschedule12g():
    global Score1, Score2, Score3, Score4, Score5, Score6, Score7, Score8, Score9, Score10, Score11, Score12, GS1, GS2, GS3, GS4, GS5, GS6, GS7, GS8, GS9, GS10, GS11, GS12, GC1, GC2, GC3, GC4, GC5, GC6, GC7, GC8,GC9, GC10, GC11, GC12, GT1, GT2, GT3, GT4, GT5, GT6, GT7, GT8, GT9, GT10, GT11, GT12

    Score1, Score2, Score3, Score4, Score5, Score6, Score7, Score8,Score9, Score10, Score11, Score12 = [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GS1, GS2, GS3, GS4, GS5, GS6, GS7, GS8, GS9, GS10, GS11, GS12 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GC1, GC2, GC3, GC4, GC5, GC6, GC7, GC8, GC9, GC10, GC11, GC12 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GT1, GT2, GT3, GT4, GT5, GT6, GT7, GT8,GT9, GT10, GT11, GT12 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]


    global round1_matches, round2_matches, round3_matches

    round1_matches = [
        G1[0] + " vs " + G1[1],
        G1[2] + " vs " + G1[3],
        G2[0] + " vs " + G2[1],
        G2[2] + " vs " + G2[3],
        G3[0] + " vs " + G3[1],
        G3[2] + " vs " + G3[3],
        G4[0] + " vs " + G4[1],
        G4[2] + " vs " + G4[3],
        G5[0] + " vs " + G5[1],
        G5[2] + " vs " + G5[3],
        G6[0] + " vs " + G6[1],
        G6[2] + " vs " + G6[3],
        G7[0] + " vs " + G7[1],
        G7[2] + " vs " + G7[3],
        G8[0] + " vs " + G8[1],
        G8[2] + " vs " + G8[3],
        G9[0] + " vs " + G9[1],
        G9[2] + " vs " + G9[3],
        G10[0] + " vs " + G10[1],
        G10[2] + " vs " + G10[3],
        G11[0] + " vs " + G11[1],
        G11[2] + " vs " + G11[3],
        G12[0] + " vs " + G12[1],
        G12[2] + " vs " + G12[3]
    ]

    round2_matches = [
        G1[0] + " vs " + G1[2],
        G1[1] + " vs " + G1[3],
        G2[0] + " vs " + G2[2],
        G2[1] + " vs " + G2[3],
        G3[0] + " vs " + G3[2],
        G3[1] + " vs " + G3[3],
        G4[0] + " vs " + G4[2],
        G4[1] + " vs " + G4[3],
        G5[0] + " vs " + G5[2],
        G5[1] + " vs " + G5[3],
        G6[0] + " vs " + G6[2],
        G6[1] + " vs " + G6[3],
        G7[0] + " vs " + G7[2],
        G7[1] + " vs " + G7[3],
        G8[0] + " vs " + G8[2],
        G8[1] + " vs " + G8[3],
        G9[0] + " vs " + G9[2],
        G9[1] + " vs " + G9[3],
        G10[0] + " vs " + G10[2],
        G10[1] + " vs " + G10[3],
        G11[0] + " vs " + G11[2],
        G11[1] + " vs " + G11[3],
        G12[0] + " vs " + G12[2],
        G12[1] + " vs " + G12[3]
    ]

    round3_matches = [
        G1[0] + " vs " + G1[3],
        G1[1] + " vs " + G1[2],
        G2[0] + " vs " + G2[3],
        G2[1] + " vs " + G2[2],
        G3[0] + " vs " + G3[3],
        G3[1] + " vs " + G3[2],
        G4[0] + " vs " + G4[3],
        G4[1] + " vs " + G4[2],
        G5[0] + " vs " + G5[3],
        G5[1] + " vs " + G5[2],
        G6[0] + " vs " + G6[3],
        G6[1] + " vs " + G6[2],
        G7[0] + " vs " + G7[3],
        G7[1] + " vs " + G7[2],
        G8[0] + " vs " + G8[3],
        G8[1] + " vs " + G8[2],
        G9[0] + " vs " + G9[3],
        G9[1] + " vs " + G9[2],
        G10[0] + " vs " + G10[3],
        G10[1] + " vs " + G10[2],
        G11[0] + " vs " + G11[3],
        G11[1] + " vs " + G11[2],
        G12[0] + " vs " + G12[3],
        G12[1] + " vs " + G12[2]
    ]

    global roundtitle,match1show,match2show,match3show,match4show,match5show,match6show,match7show,match8show,match9show,match10show,match11show,match12show,match13show,match14show,match15show,match16show,match17show,match18show,match19show,match20show,match21show,match22show,match23show,match24show
    global match1entry, match2entry, match3entry, match4entry, match5entry, match6entry, match7entry, match8entry, match9entry, match10entry, match11entry, match12entry, match13entry, match14entry, match15entry, match16entry,match17entry, match18entry, match19entry, match20entry, match21entry, match22entry, match23entry, match24entry

    global schedule46window

    schedule46window=tk.Toplevel()
    schedule46window.title("World Cup Scheduled matches")

    roundtitle=tk.Label(schedule46window,text="Round 1")

    matchesframe=tk.Frame(schedule46window)

    match1show=tk.Label(matchesframe,text=round1_matches[0])
    match1entry=tk.Entry(matchesframe,width=10)
    match1show.grid(row=1,column=1)
    match1entry.grid(row=1,column=2)

    match2show=tk.Label(matchesframe,text=round1_matches[1])
    match2entry=tk.Entry(matchesframe,width=10)
    match2show.grid(row=2,column=1)
    match2entry.grid(row=2,column=2)

    match3show=tk.Label(matchesframe,text=round1_matches[2])
    match3entry=tk.Entry(matchesframe,width=10)
    match3show.grid(row=3,column=1)
    match3entry.grid(row=3,column=2)

    match4show=tk.Label(matchesframe,text=round1_matches[3])
    match4entry=tk.Entry(matchesframe,width=10)
    match4show.grid(row=4,column=1)
    match4entry.grid(row=4,column=2)

    match5show=tk.Label(matchesframe,text=round1_matches[4])
    match5entry=tk.Entry(matchesframe,width=10)
    match5show.grid(row=5,column=1)
    match5entry.grid(row=5,column=2)

    match6show=tk.Label(matchesframe,text=round1_matches[5])
    match6entry=tk.Entry(matchesframe,width=10)
    match6show.grid(row=6,column=1)
    match6entry.grid(row=6,column=2)

    match7show=tk.Label(matchesframe,text=round1_matches[6])
    match7entry=tk.Entry(matchesframe,width=10)
    match7show.grid(row=7,column=1)
    match7entry.grid(row=7,column=2)

    match8show=tk.Label(matchesframe,text=round1_matches[7])
    match8entry=tk.Entry(matchesframe,width=10)
    match8show.grid(row=8,column=1)
    match8entry.grid(row=8,column=2)

    match9show=tk.Label(matchesframe,text=round1_matches[8])
    match9entry=tk.Entry(matchesframe,width=10)
    match9show.grid(row=9,column=1)
    match9entry.grid(row=9,column=2)

    match10show=tk.Label(matchesframe,text=round1_matches[9])
    match10entry=tk.Entry(matchesframe,width=10)
    match10show.grid(row=10,column=1)
    match10entry.grid(row=10,column=2)

    match11show=tk.Label(matchesframe,text=round1_matches[10])
    match11entry=tk.Entry(matchesframe,width=10)
    match11show.grid(row=11,column=1)
    match11entry.grid(row=11,column=2)

    match12show=tk.Label(matchesframe,text=round1_matches[11])
    match12entry=tk.Entry(matchesframe,width=10)
    match12show.grid(row=12,column=1)
    match12entry.grid(row=12,column=2)

    match13show=tk.Label(matchesframe,text=round1_matches[12])
    match13entry=tk.Entry(matchesframe,width=10)
    match13show.grid(row=13,column=1)
    match13entry.grid(row=13,column=2)

    match14show=tk.Label(matchesframe,text=round1_matches[13])
    match14entry=tk.Entry(matchesframe,width=10)
    match14show.grid(row=14,column=1)
    match14entry.grid(row=14,column=2)

    match15show=tk.Label(matchesframe,text=round1_matches[14])
    match15entry=tk.Entry(matchesframe,width=10)
    match15show.grid(row=15,column=1)
    match15entry.grid(row=15,column=2)

    match16show=tk.Label(matchesframe,text=round1_matches[15])
    match16entry=tk.Entry(matchesframe,width=10)
    match16show.grid(row=16,column=1)
    match16entry.grid(row=16,column=2)

    match17show=tk.Label(matchesframe,text=round1_matches[16])
    match17entry=tk.Entry(matchesframe,width=10)
    match17show.grid(row=17,column=1)
    match17entry.grid(row=17,column=2)

    match18show=tk.Label(matchesframe,text=round1_matches[17])
    match18entry=tk.Entry(matchesframe,width=10)
    match18show.grid(row=18,column=1)
    match18entry.grid(row=18,column=2)

    match19show=tk.Label(matchesframe,text=round1_matches[18])
    match19entry=tk.Entry(matchesframe,width=10)
    match19show.grid(row=19,column=1)
    match19entry.grid(row=19,column=2)

    match20show=tk.Label(matchesframe,text=round1_matches[19])
    match20entry=tk.Entry(matchesframe,width=10)
    match20show.grid(row=20,column=1)
    match20entry.grid(row=20,column=2)

    match21show=tk.Label(matchesframe,text=round1_matches[20])
    match21entry=tk.Entry(matchesframe,width=10)
    match21show.grid(row=21,column=1)
    match21entry.grid(row=21,column=2)

    match22show=tk.Label(matchesframe,text=round1_matches[21])
    match22entry=tk.Entry(matchesframe,width=10)
    match22show.grid(row=22,column=1)
    match22entry.grid(row=22,column=2)

    match23show=tk.Label(matchesframe,text=round1_matches[22])
    match23entry=tk.Entry(matchesframe,width=10)
    match23show.grid(row=23,column=1)
    match23entry.grid(row=23,column=2)

    match24show=tk.Label(matchesframe,text=round1_matches[23])
    match24entry=tk.Entry(matchesframe,width=10)
    match24show.grid(row=24,column=1)
    match24entry.grid(row=24,column=2)

    global round2,round3,finals

    round2=tk.Button(schedule46window,text="Round 2",command=gotoround2_46)
    round3=tk.Button(schedule46window,text="Round 3",command=gotoround3_46)
    finals=tk.Button(schedule46window,text="Go to finals",command=gotogroupsoreder)

    roundtitle.pack(pady=5)
    matchesframe.pack(padx=5)
    round2.pack(pady=5)

def goto46mode():
    if len(Euro)>=16 and len(Afro)>=10 and len(NA)>=7 and len(SA)>=7 and len(Asia)>=9 and len(Oceania)>=2:
        root.destroy()
        root46=tk.Tk()
        root46.title("World Cup Bilding : 46 countries mode")

        title=tk.Label(root46,text="Welcome to the world cup 46 counties mode bilding")
        grouplist=tk.Frame(root46)
        buttonsframe=tk.Frame(root46)

        g1frame=tk.Frame(grouplist)
        g2frame=tk.Frame(grouplist)
        g3frame=tk.Frame(grouplist)
        g4frame=tk.Frame(grouplist)
        g5frame=tk.Frame(grouplist)
        g6frame=tk.Frame(grouplist)
        g7frame=tk.Frame(grouplist)
        g8frame=tk.Frame(grouplist)
        g9frame=tk.Frame(grouplist)
        g10frame=tk.Frame(grouplist)
        g11frame=tk.Frame(grouplist)
        g12frame=tk.Frame(grouplist)

        global g1list,g2list,g3list,g4list,g5list,g6list,g7list,g8list,g9list,g10list,g11list,g12list

        g1title=tk.Label(g1frame,text="G1")
        g1list=scrolledtext.ScrolledText(g1frame, width=20, height=5)

        g2title=tk.Label(g2frame,text="G2")
        g2list=scrolledtext.ScrolledText(g2frame, width=20, height=5)

        g3title=tk.Label(g3frame,text="G3")
        g3list=scrolledtext.ScrolledText(g3frame, width=20, height=5)

        g4title=tk.Label(g4frame,text="G4")
        g4list=scrolledtext.ScrolledText(g4frame, width=20, height=5)

        g5title=tk.Label(g5frame,text="G5")
        g5list=scrolledtext.ScrolledText(g5frame, width=20, height=5)

        g6title=tk.Label(g6frame,text="G6")
        g6list=scrolledtext.ScrolledText(g6frame, width=20, height=5)

        g7title=tk.Label(g7frame,text="G7")
        g7list=scrolledtext.ScrolledText(g7frame, width=20, height=5)

        g8title=tk.Label(g8frame,text="G8")
        g8list=scrolledtext.ScrolledText(g8frame, width=20, height=5)

        g9title=tk.Label(g9frame,text="G9")
        g9list=scrolledtext.ScrolledText(g9frame, width=20, height=5)

        g10title=tk.Label(g10frame,text="G10")
        g10list=scrolledtext.ScrolledText(g10frame, width=20, height=5)

        g11title=tk.Label(g11frame,text="G11")
        g11list=scrolledtext.ScrolledText(g11frame, width=20, height=5)

        g12title=tk.Label(g12frame,text="G12")
        g12list=scrolledtext.ScrolledText(g12frame, width=20, height=5)

        g1title.pack(pady=5)
        g1list.pack(pady=5)

        g2title.pack(pady=5)
        g2list.pack(pady=5)

        g3title.pack(pady=5)
        g3list.pack(pady=5)

        g4title.pack(pady=5)
        g4list.pack(pady=5)

        g5title.pack(pady=5)
        g5list.pack(pady=5)

        g6title.pack(pady=5)
        g6list.pack(pady=5)

        g7title.pack(pady=5)
        g7list.pack(pady=5)

        g8title.pack(pady=5)
        g8list.pack(pady=5)

        g9title.pack(pady=5)
        g9list.pack(pady=5)

        g10title.pack(pady=5)
        g10list.pack(pady=5)

        g11title.pack(pady=5)
        g11list.pack(pady=5)

        g12title.pack(pady=5)
        g12list.pack(pady=5)

        g1frame.grid(row=1,column=1,padx=5)
        g2frame.grid(row=1,column=2,padx=5)
        g3frame.grid(row=1,column=3,padx=5)
        g4frame.grid(row=1,column=4,padx=5)
        g5frame.grid(row=2,column=1,padx=5)
        g6frame.grid(row=2,column=2,padx=5)
        g7frame.grid(row=2,column=3,padx=5)
        g8frame.grid(row=2,column=4,padx=5)
        g9frame.grid(row=3,column=1,padx=5)
        g10frame.grid(row=3,column=2,padx=5)
        g11frame.grid(row=3,column=3,padx=5)
        g12frame.grid(row=3,column=4,padx=5)

        global play46button,delete46button,schedule46

        play46button=tk.Button(buttonsframe,text="Execute the Bild",command=execute12g)
        delete46button=tk.Button(buttonsframe,text="Clear the Bild",command=clearbild12g)
        schedule46=tk.Button(buttonsframe,text="Show matches schedules",command=showschedule12g)


        play46button.pack(pady=5)

        title.pack()
        grouplist.pack()
        buttonsframe.pack()

        root46.mainloop()

def main8g():
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

        print("Host :"+Host)
        print("European Countries :",end=" ")
        print(QEuro)
        print("African Countries :",end=" ")
        print(QAfro)
        print("North American Countries :",end=" ")
        print(QNA)
        print("South American Countries :",end=" ")
        print(QSA)
        print("Asian Countries :",end=" ")
        print(QAsia)
        print("Oceanian Countries :",end=" ")
        print(QOceania)

        QCountries = []
        QCountries += QEuro
        QCountries += QAfro
        QCountries += QNA
        QCountries += QSA
        QCountries += QAsia
        QCountries+=QOceania

        P=[]
        P.append(Host)
        shuffle(QCountries)
        P+=QCountries

        P1 = P[0:8]
        P2 = P[8:16]
        P3 = P[16:24]
        P4 = P[24:32]

        Test=False
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
                    A3 = randint(0,7)
                G.append(P3[A3])
                A4 = randint(0, 7)
                while P4[A4] in G:
                    A4 = randint(0, 7)
                G.append(P4[A4])

            global G1,G2,G3,G4,G5,G6,G7,G8

            G1 = G[0:4]
            G2 = G[4:8]
            G3 = G[8:12]
            G4 = G[12:16]
            G5 = G[16:20]
            G6 = G[20:24]
            G7 = G[24:28]
            G8 = G[28:32]

            Test = (check(G1) and check(G2) and check(G3) and check(G4) and check(G4) and check(G5) and check(G6) and check(G7) and check(G8))

            if Test :
                print(G1)
                print(G2)
                print(G3)
                print(G4)
                print(G5)
                print(G6)
                print(G7)
                print(G8)
                
                fillscrolledlist(G1,g1list)
                fillscrolledlist(G2,g2list)
                fillscrolledlist(G3,g3list)
                fillscrolledlist(G4,g4list)
                fillscrolledlist(G5,g5list)
                fillscrolledlist(G6,g6list)
                fillscrolledlist(G7,g7list)
                fillscrolledlist(G8,g8list)
                play32button.pack_forget()
                delete32button.pack(pady=5)
                schedule32.pack(pady=5)

    except Exception as e:
        main8g()


def execute8g():
    if __name__ == "__main__":
        main8g()

def clearbild8g():
    delete32button.pack_forget()
    schedule32.pack_forget()
    play32button.pack(pady=5)
    g1list.delete(1.0,tk.END)
    g2list.delete(1.0,tk.END)
    g3list.delete(1.0,tk.END)
    g4list.delete(1.0,tk.END)
    g5list.delete(1.0,tk.END)
    g6list.delete(1.0,tk.END)
    g7list.delete(1.0,tk.END)
    g8list.delete(1.0,tk.END)

def showschedule8g():
    global Score1, Score2, Score3, Score4, Score5, Score6, Score7, Score8, GS1, GS2, GS3, GS4, GS5, GS6, GS7, GS8, GC1, GC2, GC3, GC4, GC5, GC6, GC7, GC8, GT1, GT2, GT3, GT4, GT5, GT6, GT7, GT8

    Score1, Score2, Score3, Score4, Score5, Score6, Score7, Score8 = [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GS1, GS2, GS3, GS4, GS5, GS6, GS7, GS8 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GC1, GC2, GC3, GC4, GC5, GC6, GC7, GC8 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]
    GT1, GT2, GT3, GT4, GT5, GT6, GT7, GT8 = [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]


    global round1_matches, round2_matches, round3_matches

    round1_matches = [
        G1[0] + " vs " + G1[1],
        G1[2] + " vs " + G1[3],
        G2[0] + " vs " + G2[1],
        G2[2] + " vs " + G2[3],
        G3[0] + " vs " + G3[1],
        G3[2] + " vs " + G3[3],
        G4[0] + " vs " + G4[1],
        G4[2] + " vs " + G4[3],
        G5[0] + " vs " + G5[1],
        G5[2] + " vs " + G5[3],
        G6[0] + " vs " + G6[1],
        G6[2] + " vs " + G6[3],
        G7[0] + " vs " + G7[1],
        G7[2] + " vs " + G7[3],
        G8[0] + " vs " + G8[1],
        G8[2] + " vs " + G8[3]
    ]

    round2_matches = [
        G1[0] + " vs " + G1[2],
        G1[1] + " vs " + G1[3],
        G2[0] + " vs " + G2[2],
        G2[1] + " vs " + G2[3],
        G3[0] + " vs " + G3[2],
        G3[1] + " vs " + G3[3],
        G4[0] + " vs " + G4[2],
        G4[1] + " vs " + G4[3],
        G5[0] + " vs " + G5[2],
        G5[1] + " vs " + G5[3],
        G6[0] + " vs " + G6[2],
        G6[1] + " vs " + G6[3],
        G7[0] + " vs " + G7[2],
        G7[1] + " vs " + G7[3],
        G8[0] + " vs " + G8[2],
        G8[1] + " vs " + G8[3]
    ]

    round3_matches = [
        G1[0] + " vs " + G1[3],
        G1[1] + " vs " + G1[2],
        G2[0] + " vs " + G2[3],
        G2[1] + " vs " + G2[2],
        G3[0] + " vs " + G3[3],
        G3[1] + " vs " + G3[2],
        G4[0] + " vs " + G4[3],
        G4[1] + " vs " + G4[2],
        G5[0] + " vs " + G5[3],
        G5[1] + " vs " + G5[2],
        G6[0] + " vs " + G6[3],
        G6[1] + " vs " + G6[2],
        G7[0] + " vs " + G7[3],
        G7[1] + " vs " + G7[2],
        G8[0] + " vs " + G8[3],
        G8[1] + " vs " + G8[2]
    ]

    global roundtitle,match1show,match2show,match3show,match4show,match5show,match6show,match7show,match8show,match9show,match10show,match11show,match12show,match13show,match14show,match15show,match16show
    global match1entry, match2entry, match3entry, match4entry, match5entry, match6entry, match7entry, match8entry, match9entry, match10entry, match11entry, match12entry, match13entry, match14entry, match15entry, match16entry

    global schedule32window

    schedule32window=tk.Toplevel()
    schedule32window.title("World Cup Scheduled matches")

    roundtitle=tk.Label(schedule32window,text="Round 1")

    matchesframe=tk.Frame(schedule32window)

    match1show=tk.Label(matchesframe,text=round1_matches[0])
    match1entry=tk.Entry(matchesframe,width=10)
    match1show.grid(row=1,column=1)
    match1entry.grid(row=1,column=2)

    match2show=tk.Label(matchesframe,text=round1_matches[1])
    match2entry=tk.Entry(matchesframe,width=10)
    match2show.grid(row=2,column=1)
    match2entry.grid(row=2,column=2)

    match3show=tk.Label(matchesframe,text=round1_matches[2])
    match3entry=tk.Entry(matchesframe,width=10)
    match3show.grid(row=3,column=1)
    match3entry.grid(row=3,column=2)

    match4show=tk.Label(matchesframe,text=round1_matches[3])
    match4entry=tk.Entry(matchesframe,width=10)
    match4show.grid(row=4,column=1)
    match4entry.grid(row=4,column=2)

    match5show=tk.Label(matchesframe,text=round1_matches[4])
    match5entry=tk.Entry(matchesframe,width=10)
    match5show.grid(row=5,column=1)
    match5entry.grid(row=5,column=2)

    match6show=tk.Label(matchesframe,text=round1_matches[5])
    match6entry=tk.Entry(matchesframe,width=10)
    match6show.grid(row=6,column=1)
    match6entry.grid(row=6,column=2)

    match7show=tk.Label(matchesframe,text=round1_matches[6])
    match7entry=tk.Entry(matchesframe,width=10)
    match7show.grid(row=7,column=1)
    match7entry.grid(row=7,column=2)

    match8show=tk.Label(matchesframe,text=round1_matches[7])
    match8entry=tk.Entry(matchesframe,width=10)
    match8show.grid(row=8,column=1)
    match8entry.grid(row=8,column=2)

    match9show=tk.Label(matchesframe,text=round1_matches[8])
    match9entry=tk.Entry(matchesframe,width=10)
    match9show.grid(row=9,column=1)
    match9entry.grid(row=9,column=2)

    match10show=tk.Label(matchesframe,text=round1_matches[9])
    match10entry=tk.Entry(matchesframe,width=10)
    match10show.grid(row=10,column=1)
    match10entry.grid(row=10,column=2)

    match11show=tk.Label(matchesframe,text=round1_matches[10])
    match11entry=tk.Entry(matchesframe,width=10)
    match11show.grid(row=11,column=1)
    match11entry.grid(row=11,column=2)

    match12show=tk.Label(matchesframe,text=round1_matches[11])
    match12entry=tk.Entry(matchesframe,width=10)
    match12show.grid(row=12,column=1)
    match12entry.grid(row=12,column=2)

    match13show=tk.Label(matchesframe,text=round1_matches[12])
    match13entry=tk.Entry(matchesframe,width=10)
    match13show.grid(row=13,column=1)
    match13entry.grid(row=13,column=2)

    match14show=tk.Label(matchesframe,text=round1_matches[13])
    match14entry=tk.Entry(matchesframe,width=10)
    match14show.grid(row=14,column=1)
    match14entry.grid(row=14,column=2)

    match15show=tk.Label(matchesframe,text=round1_matches[14])
    match15entry=tk.Entry(matchesframe,width=10)
    match15show.grid(row=15,column=1)
    match15entry.grid(row=15,column=2)

    match16show=tk.Label(matchesframe,text=round1_matches[15])
    match16entry=tk.Entry(matchesframe,width=10)
    match16show.grid(row=16,column=1)
    match16entry.grid(row=16,column=2)


    global round2,round3,finals

    round2=tk.Button(schedule32window,text="Round 2",command=gotoround2_32)
    round3=tk.Button(schedule32window,text="Round 3",command=gotoround3_32)
    finals=tk.Button(schedule32window,text="Go to finals",command=gotogroupsoreder32)

    roundtitle.pack(pady=5)
    matchesframe.pack(padx=5)
    round2.pack(pady=5)

def gotoround2_32():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != "" :
        Result = match1entry.get()
        treat(G1, Result, 0, 1, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 2, 3, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 1, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 2, 3, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 1, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 2, 3, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 1, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 2, 3, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 1, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 2, 3, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 1, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 2, 3, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 1, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 2, 3, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 1, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 2, 3, Score8, GS8, GC8, GT8)

        match1entry.delete(0, tk.END)
        match2entry.delete(0, tk.END)
        match3entry.delete(0, tk.END)
        match4entry.delete(0, tk.END)
        match5entry.delete(0, tk.END)
        match6entry.delete(0, tk.END)
        match7entry.delete(0, tk.END)
        match8entry.delete(0, tk.END)
        match9entry.delete(0, tk.END)
        match10entry.delete(0, tk.END)
        match11entry.delete(0, tk.END)
        match12entry.delete(0, tk.END)
        match13entry.delete(0, tk.END)
        match14entry.delete(0, tk.END)
        match15entry.delete(0, tk.END)
        match16entry.delete(0, tk.END)

        match1show.config(text=round2_matches[0])
        match2show.config(text=round2_matches[1])
        match3show.config(text=round2_matches[2])
        match4show.config(text=round2_matches[3])
        match5show.config(text=round2_matches[4])
        match6show.config(text=round2_matches[5])
        match7show.config(text=round2_matches[6])
        match8show.config(text=round2_matches[7])
        match9show.config(text=round2_matches[8])
        match10show.config(text=round2_matches[9])
        match11show.config(text=round2_matches[10])
        match12show.config(text=round2_matches[11])
        match13show.config(text=round2_matches[12])
        match14show.config(text=round2_matches[13])
        match15show.config(text=round2_matches[14])
        match16show.config(text=round2_matches[15])
        roundtitle.config(text="Round 2")
        round2.pack_forget()
        round3.pack(pady=5)

def gotoround3_32():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != "" :
        Result = match1entry.get()
        treat(G1, Result, 0, 2, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 1, 3, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 2, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 1, 3, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 2, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 1, 3, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 2, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 1, 3, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 2, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 1, 3, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 2, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 1, 3, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 2, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 1, 3, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 2, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 1, 3, Score8, GS8, GC8, GT8)

        match1entry.delete(0, tk.END)
        match2entry.delete(0, tk.END)
        match3entry.delete(0, tk.END)
        match4entry.delete(0, tk.END)
        match5entry.delete(0, tk.END)
        match6entry.delete(0, tk.END)
        match7entry.delete(0, tk.END)
        match8entry.delete(0, tk.END)
        match9entry.delete(0, tk.END)
        match10entry.delete(0, tk.END)
        match11entry.delete(0, tk.END)
        match12entry.delete(0, tk.END)
        match13entry.delete(0, tk.END)
        match14entry.delete(0, tk.END)
        match15entry.delete(0, tk.END)
        match16entry.delete(0, tk.END)

        match1show.config(text=round3_matches[0])
        match2show.config(text=round3_matches[1])
        match3show.config(text=round3_matches[2])
        match4show.config(text=round3_matches[3])
        match5show.config(text=round3_matches[4])
        match6show.config(text=round3_matches[5])
        match7show.config(text=round3_matches[6])
        match8show.config(text=round3_matches[7])
        match9show.config(text=round3_matches[8])
        match10show.config(text=round3_matches[9])
        match11show.config(text=round3_matches[10])
        match12show.config(text=round3_matches[11])
        match13show.config(text=round3_matches[12])
        match14show.config(text=round3_matches[13])
        match15show.config(text=round3_matches[14])
        match16show.config(text=round3_matches[15])
        roundtitle.config(text="Round 3")
        round3.pack_forget()
        finals.pack(pady=5)

def gotogroupsoreder32():
    if match1entry.get() != "" and match2entry.get() != "" and match3entry.get() != "" and match4entry.get() != "" and match5entry.get() != "" and match6entry.get() != "" and match7entry.get() != "" and match8entry.get() != "" and match9entry.get() != "" and match10entry.get() != "" and match11entry.get() != "" and match12entry.get() != "" and match13entry.get() != "" and match14entry.get() != "" and match15entry.get() != "" and match16entry.get() != ""  :
        global G1,G2,G3,G4,G5,G6,G7,G8
        Result = match1entry.get()
        treat(G1, Result, 0, 3, Score1, GS1, GC1, GT1)
        Result = match2entry.get()
        treat(G1, Result, 1, 2, Score1, GS1, GC1, GT1)
        Result = match3entry.get()
        treat(G2, Result, 0, 3, Score2, GS2, GC2, GT2)
        Result = match4entry.get()
        treat(G2, Result, 1, 2, Score2, GS2, GC2, GT2)
        Result = match5entry.get()
        treat(G3, Result, 0, 3, Score3, GS3, GC3, GT3)
        Result = match6entry.get()
        treat(G3, Result, 1, 2, Score3, GS3, GC3, GT3)
        Result = match7entry.get()
        treat(G4, Result, 0, 3, Score4, GS4, GC4, GT4)
        Result = match8entry.get()
        treat(G4, Result, 1, 2, Score4, GS4, GC4, GT4)
        Result = match9entry.get()
        treat(G5, Result, 0, 3, Score5, GS5, GC5, GT5)
        Result = match10entry.get()
        treat(G5, Result, 1, 2, Score5, GS5, GC5, GT5)
        Result = match11entry.get()
        treat(G6, Result, 0, 3, Score6, GS6, GC6, GT6)
        Result = match12entry.get()
        treat(G6, Result, 1, 2, Score6, GS6, GC6, GT6)
        Result = match13entry.get()
        treat(G7, Result, 0, 3, Score7, GS7, GC7, GT7)
        Result = match14entry.get()
        treat(G7, Result, 1, 2, Score7, GS7, GC7, GT7)
        Result = match15entry.get()
        treat(G8, Result, 0, 3, Score8, GS8, GC8, GT8)
        Result = match16entry.get()
        treat(G8, Result, 1, 2, Score8, GS8, GC8, GT8)

        sort(G1, Score1, GS1, GC1, GT1)
        sort(G2, Score2, GS2, GC2, GT2)
        sort(G3, Score3, GS3, GC3, GT3)
        sort(G4, Score4, GS4, GC4, GT4)
        sort(G5, Score5, GS5, GC5, GT5)
        sort(G6, Score6, GS6, GC6, GT6)
        sort(G7, Score7, GS7, GC7, GT7)
        sort(G8, Score8, GS8, GC8, GT8)


        schedule32window.destroy()

        table32=tk.Tk()
        table32.title("Table results")

        tableframes=tk.Frame(table32)
        g1tableframe=tk.Frame(tableframes)

        g1name=tk.Label(g1tableframe,text='G1')
        table1 = ttk.Treeview(g1tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table1.heading('#1', text='Rank')
        table1.heading('#2', text='Country')
        table1.heading('#3', text='Score')
        table1.heading('#4', text='GS')
        table1.heading('#5', text='GC')
        table1.heading('#6', text='GT')
        table1.column('#1', width=30)
        table1.column('#2', width=70)
        table1.column('#3', width=30)
        table1.column('#4', width=30)
        table1.column('#5', width=30)
        table1.column('#6', width=30)
        g1name.pack(pady=5)
        table1.pack()
        filltable(table1, G1, Score1, GS1, GC1, GT1)

        g2tableframe=tk.Frame(tableframes)
        g2name=tk.Label(g2tableframe,text='G2')
        table2 = ttk.Treeview(g2tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table2.heading('#1', text='Rank')
        table2.heading('#2', text='Country')
        table2.heading('#3', text='Score')
        table2.heading('#4', text='GS')
        table2.heading('#5', text='GC')
        table2.heading('#6', text='GT')
        table2.column('#1', width=30)
        table2.column('#2', width=70)
        table2.column('#3', width=30)
        table2.column('#4', width=30)
        table2.column('#5', width=30)
        table2.column('#6', width=30)
        g2name.pack(pady=5)
        table2.pack()
        filltable(table2, G2, Score2, GS2, GC2, GT2)

        g3tableframe=tk.Frame(tableframes)
        g3name=tk.Label(g3tableframe,text='G3')
        table3 = ttk.Treeview(g3tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table3.heading('#1', text='Rank')
        table3.heading('#2', text='Country')
        table3.heading('#3', text='Score')
        table3.heading('#4', text='GS')
        table3.heading('#5', text='GC')
        table3.heading('#6', text='GT')
        table3.column('#1', width=30)
        table3.column('#2', width=70)
        table3.column('#3', width=30)
        table3.column('#4', width=30)
        table3.column('#5', width=30)
        table3.column('#6', width=30)
        g3name.pack(pady=5)
        table3.pack()
        filltable(table3, G3, Score3, GS3, GC3, GT3)

        g4tableframe=tk.Frame(tableframes)
        g4name=tk.Label(g4tableframe,text='G4')
        table4 = ttk.Treeview(g4tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table4.heading('#1', text='Rank')
        table4.heading('#2', text='Country')
        table4.heading('#3', text='Score')
        table4.heading('#4', text='GS')
        table4.heading('#5', text='GC')
        table4.heading('#6', text='GT')
        table4.column('#1', width=30)
        table4.column('#2', width=70)
        table4.column('#3', width=30)
        table4.column('#4', width=30)
        table4.column('#5', width=30)
        table4.column('#6', width=30)
        g4name.pack(pady=5)
        table4.pack()
        filltable(table4, G4, Score4, GS4, GC4, GT4)

        g5tableframe=tk.Frame(tableframes)
        g5name=tk.Label(g5tableframe,text='G5')
        table5 = ttk.Treeview(g5tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table5.heading('#1', text='Rank')
        table5.heading('#2', text='Country')
        table5.heading('#3', text='Score')
        table5.heading('#4', text='GS')
        table5.heading('#5', text='GC')
        table5.heading('#6', text='GT')
        table5.column('#1', width=30)
        table5.column('#2', width=70)
        table5.column('#3', width=30)
        table5.column('#4', width=30)
        table5.column('#5', width=30)
        table5.column('#6', width=30)
        g5name.pack(pady=5)
        table5.pack()
        filltable(table5, G5, Score5, GS5, GC5, GT5)

        g6tableframe=tk.Frame(tableframes)
        g6name=tk.Label(g6tableframe,text='G6')
        table6 = ttk.Treeview(g6tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table6.heading('#1', text='Rank')
        table6.heading('#2', text='Country')
        table6.heading('#3', text='Score')
        table6.heading('#4', text='GS')
        table6.heading('#5', text='GC')
        table6.heading('#6', text='GT')
        table6.column('#1', width=30)
        table6.column('#2', width=70)
        table6.column('#3', width=30)
        table6.column('#4', width=30)
        table6.column('#5', width=30)
        table6.column('#6', width=30)
        g6name.pack(pady=5)
        table6.pack()
        filltable(table6, G6, Score6, GS6, GC6, GT6)

        g7tableframe=tk.Frame(tableframes)
        g7name=tk.Label(g7tableframe,text='G7')
        table7 = ttk.Treeview(g7tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table7.heading('#1', text='Rank')
        table7.heading('#2', text='Country')
        table7.heading('#3', text='Score')
        table7.heading('#4', text='GS')
        table7.heading('#5', text='GC')
        table7.heading('#6', text='GT')
        table7.column('#1', width=30)
        table7.column('#2', width=70)
        table7.column('#3', width=30)
        table7.column('#4', width=30)
        table7.column('#5', width=30)
        table7.column('#6', width=30)
        g7name.pack(pady=5)
        table7.pack()
        filltable(table7, G7, Score7, GS7, GC7, GT7)

        g8tableframe=tk.Frame(tableframes)
        g8name=tk.Label(g8tableframe,text='G8')
        table8 = ttk.Treeview(g8tableframe, height=5, columns=('Rank', 'Country', 'Score', 'GS', 'GC', 'GT'), show='headings')
        table8.heading('#1', text='Rank')
        table8.heading('#2', text='Country')
        table8.heading('#3', text='Score')
        table8.heading('#4', text='GS')
        table8.heading('#5', text='GC')
        table8.heading('#6', text='GT')
        table8.column('#1', width=30)
        table8.column('#2', width=70)
        table8.column('#3', width=30)
        table8.column('#4', width=30)
        table8.column('#5', width=30)
        table8.column('#6', width=30)
        g8name.pack(pady=5)
        table8.pack()
        filltable(table8, G8, Score8, GS8, GC8, GT8)



        g1tableframe.grid(row=1,column=1,padx=3,pady=3)
        g2tableframe.grid(row=1,column=2,padx=3,pady=3)
        g3tableframe.grid(row=1,column=3,padx=3,pady=3)
        g4tableframe.grid(row=1,column=4,padx=3,pady=3)
        g5tableframe.grid(row=2,column=1,padx=3,pady=3)
        g6tableframe.grid(row=2,column=2,padx=3,pady=3)
        g7tableframe.grid(row=2,column=3,padx=3,pady=3)
        g8tableframe.grid(row=2,column=4,padx=3,pady=3)
        global round16button

        round16button=tk.Button(table32,text="Round of 16",command=gotoround16_8g)

        tableframes.pack()
        round16button.pack(pady=5)

        table32.mainloop()

def gotoround16_8g():

    global Qround16

    Qround16=[G1[0], G2[1], G3[0], G4[1], G5[0], G6[1], G7[0],
                    G8[1], G1[1], G2[0], G3[1], G4[0], G5[1], G6[0], G7[1], G8[0]]
    

    round16_matches=[
        Qround16[0]+" vs "+Qround16[1],
        Qround16[2]+" vs "+Qround16[3],
        Qround16[4]+" vs "+Qround16[5],
        Qround16[6]+" vs "+Qround16[7],
        Qround16[8]+" vs "+Qround16[9],
        Qround16[10]+" vs "+Qround16[11],
        Qround16[12]+" vs "+Qround16[13],
        Qround16[14]+" vs "+Qround16[15]]
    
    round16button.pack_forget()

    global finalsroot,finalscheduleroot

    finalscheduleroot=tk.Toplevel()
    finalscheduleroot.title("Finals matches")

    global finalsmatchesframe,finalstitle

    finalstitle=tk.Label(finalscheduleroot,text="Round of 16")
    finalsmatchesframe=tk.Frame(finalscheduleroot)
    
    global finalsmatch1,finalsmatch1entry,finalsmatch2,finalsmatch2entry,finalsmatch3,finalsmatch3entry,finalsmatch4,finalsmatch4entry,finalsmatch5,finalsmatch5entry,finalsmatch6,finalsmatch6entry,finalsmatch7,finalsmatch7entry,finalsmatch8,finalsmatch8entry,finalsmatch9,finalsmatch9entry,finalsmatch10,finalsmatch10entry,finalsmatch11,finalsmatch11entry,finalsmatch12,finalsmatch12entry,finalsmatch13,finalsmatch13entry,finalsmatch14,finalsmatch14entry,finalsmatch15,finalsmatch15entry,finalsmatch16,finalsmatch16entry

    finalsmatch1=tk.Label(finalsmatchesframe,text=round16_matches[0])
    finalsmatch1entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch1.grid(row=1,column=1)
    finalsmatch1entry.grid(row=1,column=2)
    finalsmatch2=tk.Label(finalsmatchesframe,text=round16_matches[1])
    finalsmatch2entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch2.grid(row=2,column=1)
    finalsmatch2entry.grid(row=2,column=2)
    finalsmatch3=tk.Label(finalsmatchesframe,text=round16_matches[2])
    finalsmatch3entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch3.grid(row=3,column=1)
    finalsmatch3entry.grid(row=3,column=2)
    finalsmatch4=tk.Label(finalsmatchesframe,text=round16_matches[3])
    finalsmatch4entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch4.grid(row=4,column=1)
    finalsmatch4entry.grid(row=4,column=2)
    finalsmatch5=tk.Label(finalsmatchesframe,text=round16_matches[4])
    finalsmatch5entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch5.grid(row=5,column=1)
    finalsmatch5entry.grid(row=5,column=2)
    finalsmatch6=tk.Label(finalsmatchesframe,text=round16_matches[5])
    finalsmatch6entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch6.grid(row=6,column=1)
    finalsmatch6entry.grid(row=6,column=2)
    finalsmatch7=tk.Label(finalsmatchesframe,text=round16_matches[6])
    finalsmatch7entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch7.grid(row=7,column=1)
    finalsmatch7entry.grid(row=7,column=2)
    finalsmatch8=tk.Label(finalsmatchesframe,text=round16_matches[7])
    finalsmatch8entry=tk.Entry(finalsmatchesframe,width=10)
    finalsmatch8.grid(row=8,column=1)
    finalsmatch8entry.grid(row=8,column=2)


    global round8

    round8=tk.Button(finalscheduleroot,text="1/4 Final",command=gotoround8)

    finalstitle.pack(pady=5)
    finalsmatchesframe.pack(pady=5)
    round8.pack(pady=5)

    finalsroot=tk.Toplevel()
    finalsroot.title("Finals Draw")

    country32_1_16=tk.Label(finalsroot,text=Qround16[0])
    country32_2_16=tk.Label(finalsroot,text=Qround16[1])
    country32_3_16=tk.Label(finalsroot,text=Qround16[2])
    country32_4_16=tk.Label(finalsroot,text=Qround16[3])
    country32_5_16=tk.Label(finalsroot,text=Qround16[4])
    country32_6_16=tk.Label(finalsroot,text=Qround16[5])
    country32_7_16=tk.Label(finalsroot,text=Qround16[6])
    country32_8_16=tk.Label(finalsroot,text=Qround16[7])
    country32_9_16=tk.Label(finalsroot,text=Qround16[8])
    country32_10_16=tk.Label(finalsroot,text=Qround16[9])
    country32_11_16=tk.Label(finalsroot,text=Qround16[10])
    country32_12_16=tk.Label(finalsroot,text=Qround16[11])
    country32_13_16=tk.Label(finalsroot,text=Qround16[12])
    country32_14_16=tk.Label(finalsroot,text=Qround16[13])
    country32_15_16=tk.Label(finalsroot,text=Qround16[14])
    country32_16_16=tk.Label(finalsroot,text=Qround16[15])

    country32_1_16.grid(row=1,column=1)
    country32_2_16.grid(row=2,column=1)
    country32_3_16.grid(row=3,column=1)
    country32_4_16.grid(row=4,column=1)
    country32_5_16.grid(row=5,column=1)
    country32_6_16.grid(row=6,column=1)
    country32_7_16.grid(row=7,column=1)
    country32_8_16.grid(row=8,column=1)
    country32_9_16.grid(row=1,column=8)
    country32_10_16.grid(row=2,column=8)
    country32_11_16.grid(row=3,column=8)
    country32_12_16.grid(row=4,column=8)
    country32_13_16.grid(row=5,column=8)
    country32_14_16.grid(row=6,column=8)
    country32_15_16.grid(row=7,column=8)
    country32_16_16.grid(row=8,column=8)



def gotoround8():
    if match1entry!='' and match2entry!='' and match3entry!='' and match4entry!='' and match5entry!='' and match6entry!='' and match7entry!='' and match8entry!='' :
        finalstitle.config(text="1/4 Final")
        global Qround8
        
        Qround8=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qround16,0,1,Qround8)
        Result=finalsmatch2entry.get()
        treatfinals(Result,Qround16,2,3,Qround8)
        Result=finalsmatch3entry.get()
        treatfinals(Result,Qround16,4,5,Qround8)
        Result=finalsmatch4entry.get()
        treatfinals(Result,Qround16,6,7,Qround8)
        Result=finalsmatch5entry.get()
        treatfinals(Result,Qround16,8,9,Qround8)
        Result=finalsmatch6entry.get()
        treatfinals(Result,Qround16,10,11,Qround8)
        Result=finalsmatch7entry.get()
        treatfinals(Result,Qround16,12,13,Qround8)
        Result=finalsmatch8entry.get()
        treatfinals(Result,Qround16,14,15,Qround8)

        round8_matches=[
            Qround8[0]+" vs "+Qround8[1],
            Qround8[2]+" vs "+Qround8[3],
            Qround8[4]+" vs "+Qround8[5],
            Qround8[6]+" vs "+Qround8[7]
        ]

        finalsmatch1entry.delete(0,tk.END)
        finalsmatch2entry.delete(0,tk.END)
        finalsmatch3entry.delete(0,tk.END)
        finalsmatch4entry.delete(0,tk.END)
        finalsmatch1.config(text=round8_matches[0])
        finalsmatch2.config(text=round8_matches[1])
        finalsmatch3.config(text=round8_matches[2])
        finalsmatch4.config(text=round8_matches[3])
        
        finalsmatch5.grid_forget()
        finalsmatch5entry.grid_forget()
        finalsmatch6.grid_forget()
        finalsmatch6entry.grid_forget()
        finalsmatch7.grid_forget()
        finalsmatch7entry.grid_forget()
        finalsmatch8.grid_forget()
        finalsmatch8entry.grid_forget()

        country32_1_8=tk.Label(finalsroot,text=Qround8[0])
        country32_2_8=tk.Label(finalsroot,text=Qround8[1])
        country32_3_8=tk.Label(finalsroot,text=Qround8[2])
        country32_4_8=tk.Label(finalsroot,text=Qround8[3])
        country32_5_8=tk.Label(finalsroot,text=Qround8[4])
        country32_6_8=tk.Label(finalsroot,text=Qround8[5])
        country32_7_8=tk.Label(finalsroot,text=Qround8[6])
        country32_8_8=tk.Label(finalsroot,text=Qround8[7])

        country32_1_8.grid(row=1,column=2,rowspan=2)
        country32_2_8.grid(row=3,column=2,rowspan=2)
        country32_3_8.grid(row=5,column=2,rowspan=2)
        country32_4_8.grid(row=7,column=2,rowspan=2)
        country32_5_8.grid(row=1,column=7,rowspan=2)
        country32_6_8.grid(row=3,column=7,rowspan=2)
        country32_7_8.grid(row=5,column=7,rowspan=2)
        country32_8_8.grid(row=7,column=7,rowspan=2)

        global round4

        round8.pack_forget()
        round4=tk.Button(finalscheduleroot,text="1/2 Final",command=gotoround4)
        round4.pack(pady=5)

def gotoround4():
    if match1entry!='' and match2entry!='' and match3entry!='' and match4entry!='' :
        finalstitle.config(text="1/2 Final")
        global Qround4
        
        Qround4=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qround8,0,1,Qround4)
        Result=finalsmatch2entry.get()
        treatfinals(Result,Qround8,2,3,Qround4)
        Result=finalsmatch3entry.get()
        treatfinals(Result,Qround8,4,5,Qround4)
        Result=finalsmatch4entry.get()
        treatfinals(Result,Qround8,6,7,Qround4)

        round4_matches=[
            Qround4[0]+" vs "+Qround4[1],
            Qround4[2]+" vs "+Qround4[3]
        ]

        finalsmatch1entry.delete(0,tk.END)
        finalsmatch2entry.delete(0,tk.END)
        finalsmatch1.config(text=round4_matches[0])
        finalsmatch2.config(text=round4_matches[1])
        
        finalsmatch3.grid_forget()
        finalsmatch3entry.grid_forget()
        finalsmatch4.grid_forget()
        finalsmatch4entry.grid_forget()

        country32_1_4=tk.Label(finalsroot,text=Qround4[0])
        country32_2_4=tk.Label(finalsroot,text=Qround4[1])
        country32_3_4=tk.Label(finalsroot,text=Qround4[2])
        country32_4_4=tk.Label(finalsroot,text=Qround4[3])

        country32_1_4.grid(row=1,column=3,rowspan=4)
        country32_2_4.grid(row=5,column=3,rowspan=4)
        country32_3_4.grid(row=1,column=6,rowspan=4)
        country32_4_4.grid(row=5,column=6,rowspan=4)

        global roundfinal

        round4.pack_forget()
        roundfinal=tk.Button(finalscheduleroot,text="Final",command=gotofinal)
        roundfinal.pack(pady=5)

def gotofinal():
    if match1entry!='' and match2entry!='' :
        finalstitle.config(text="Final")
        global Qroundfinal
        
        Qroundfinal=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qround4,0,1,Qroundfinal)
        Result=finalsmatch2entry.get()
        treatfinals(Result,Qround4,2,3,Qroundfinal)

        roundfinal_matches=[
            Qroundfinal[0]+" vs "+Qroundfinal[1]
        ]

        finalsmatch1entry.delete(0,tk.END)
        finalsmatch1.config(text=roundfinal_matches[0])
        
        finalsmatch2.grid_forget()
        finalsmatch2entry.grid_forget()

        country32_1_f=tk.Label(finalsroot,text=Qroundfinal[0])
        country32_2_f=tk.Label(finalsroot,text=Qroundfinal[1])

        country32_1_f.grid(row=1,column=4,rowspan=8)
        country32_2_f.grid(row=1,column=5,rowspan=8)

        global endwc

        roundfinal.pack_forget()
        endwc=tk.Button(finalscheduleroot,text="Final",command=endworldcup)
        endwc.pack(pady=5)

def endworldcup():
    if match1entry!='' :
        finalstitle.config(text="End of world cup")
        global Winner
        
        Winner=[]
        
        Result=finalsmatch1entry.get()
        treatfinals(Result,Qroundfinal,0,1,Winner)

        finalscheduleroot.destroy()

        country32_1_f=tk.Label(finalsroot,text=Winner[0])

        country32_1_f.grid(row=3,column=4,columnspan=2)

def goto32mode():
    if len(Euro)>=13 and len(Afro)>=5 and len(NA)>=4 and len(SA)>=5 and len(Asia)>=5 and len(Oceania)>=1:
        root.destroy()
        root32=tk.Tk()
        root32.title("World Cup Bilding : 32 countries mode")

        title=tk.Label(root32,text="Welcome to the world cup 32 counties mode bilding")
        grouplist=tk.Frame(root32)
        buttonsframe=tk.Frame(root32)

        g1frame=tk.Frame(grouplist)
        g2frame=tk.Frame(grouplist)
        g3frame=tk.Frame(grouplist)
        g4frame=tk.Frame(grouplist)
        g5frame=tk.Frame(grouplist)
        g6frame=tk.Frame(grouplist)
        g7frame=tk.Frame(grouplist)
        g8frame=tk.Frame(grouplist)

        global g1list,g2list,g3list,g4list,g5list,g6list,g7list,g8list

        g1title=tk.Label(g1frame,text="G1")
        g1list=scrolledtext.ScrolledText(g1frame, width=20, height=5)

        g2title=tk.Label(g2frame,text="G2")
        g2list=scrolledtext.ScrolledText(g2frame, width=20, height=5)

        g3title=tk.Label(g3frame,text="G3")
        g3list=scrolledtext.ScrolledText(g3frame, width=20, height=5)

        g4title=tk.Label(g4frame,text="G4")
        g4list=scrolledtext.ScrolledText(g4frame, width=20, height=5)

        g5title=tk.Label(g5frame,text="G5")
        g5list=scrolledtext.ScrolledText(g5frame, width=20, height=5)

        g6title=tk.Label(g6frame,text="G6")
        g6list=scrolledtext.ScrolledText(g6frame, width=20, height=5)

        g7title=tk.Label(g7frame,text="G7")
        g7list=scrolledtext.ScrolledText(g7frame, width=20, height=5)

        g8title=tk.Label(g8frame,text="G8")
        g8list=scrolledtext.ScrolledText(g8frame, width=20, height=5)

        g1title.pack(pady=5)
        g1list.pack(pady=5)

        g2title.pack(pady=5)
        g2list.pack(pady=5)

        g3title.pack(pady=5)
        g3list.pack(pady=5)

        g4title.pack(pady=5)
        g4list.pack(pady=5)

        g5title.pack(pady=5)
        g5list.pack(pady=5)

        g6title.pack(pady=5)
        g6list.pack(pady=5)

        g7title.pack(pady=5)
        g7list.pack(pady=5)

        g8title.pack(pady=5)
        g8list.pack(pady=5)

        g1frame.grid(row=1,column=1,padx=5)
        g2frame.grid(row=1,column=2,padx=5)
        g3frame.grid(row=1,column=3,padx=5)
        g4frame.grid(row=1,column=4,padx=5)
        g5frame.grid(row=2,column=1,padx=5)
        g6frame.grid(row=2,column=2,padx=5)
        g7frame.grid(row=2,column=3,padx=5)
        g8frame.grid(row=2,column=4,padx=5)

        global play32button,delete32button,schedule32

        play32button=tk.Button(buttonsframe,text="Execute the Bild",command=execute8g)
        delete32button=tk.Button(buttonsframe,text="Clear the Bild",command=clearbild8g)
        schedule32=tk.Button(buttonsframe,text="Show matches schedules",command=showschedule8g)


        play32button.pack(pady=5)

        title.pack()
        grouplist.pack()
        buttonsframe.pack()

        root32.mainloop()

def about():
    aboutwindow=tk.Toplevel()

    aboutframe = tk.Frame(aboutwindow,bg="#0E96CC")

    Name = tk.Label(aboutframe, text=("Professor Xenon"), fg="#0E96CC", font=("Arial", 20))
    image = tk.PhotoImage(file="C:/My files/Coding/programming_main/New projects _py/Calculator/Me.png")
    infos = tk.Label(aboutframe, font=("Arial", 10))
    infos.config(text="Real name: Med Amin Haffouz \nEmail:aminhfz01@gmail.com\nStudies at : Tunis National Institute of Applied Sciences and Technology (INSAT)")

    Name.grid(row=1, column=1, columnspan=2)
    image_label = tk.Label(aboutframe, image=image)
    image_label.grid(row=2, column=1)
    infos.grid(row=2, column=2)

    aboutframe.pack(padx=5,pady=5)

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
    satitle = tk.Label(cont, text="North America")
    satitle.grid(row=2, column=4)
    natitle = tk.Label(cont, text="South America")
    natitle.grid(row=2, column=5)
    oceantitle = tk.Label(cont, text="Oceania")
    oceantitle.grid(row=2, column=6)

    Eurolist = scrolledtext.ScrolledText(cont, width=20, height=20)
    Euroelements = EuroLib[0]
    for i in range(1, len(EuroLib)):
        Euroelements += "\n" + EuroLib[i]
    Eurolist.insert(tk.END, Euroelements)

    Afrolist = scrolledtext.ScrolledText(cont, width=20, height=20)
    Afroelements = AfroLib[0]
    for i in range(1, len(AfroLib)):
        Afroelements += "\n" + AfroLib[i]
    Afrolist.insert(tk.END, Afroelements)

    Asialist = scrolledtext.ScrolledText(cont, width=20, height=20)
    Asiaelements = AsiaLib[0]
    for i in range(1, len(AsiaLib)):
        Asiaelements += "\n" + AsiaLib[i]
    Asialist.insert(tk.END, Asiaelements)

    NAlist = scrolledtext.ScrolledText(cont, width=20, height=20)
    NAelements = NALib[0]
    for i in range(1, len(NALib)):
        NAelements += "\n" + NALib[i]
    NAlist.insert(tk.END, NAelements)

    SAlist = scrolledtext.ScrolledText(cont, width=20, height=20)
    SAelements = SALib[0]
    for i in range(1, len(SALib)):
        SAelements += "\n" + SALib[i]
    SAlist.insert(tk.END, SAelements)

    Oceanialist = scrolledtext.ScrolledText(cont, width=20, height=20)
    Oceaniaelements = OceaniaLib[0]
    for i in range(1, len(OceaniaLib)):
        Oceaniaelements += "\n" + OceaniaLib[i]
    Oceanialist.insert(tk.END, Oceaniaelements)

    Eurolist.grid(row=3, column=1)
    Afrolist.grid(row=3, column=2)
    Asialist.grid(row=3, column=3)
    NAlist.grid(row=3, column=4)
    SAlist.grid(row=3, column=5)
    Oceanialist.grid(row=3, column=6)

    hint = tk.Label(cont, text="Only countries with this synthax will be accepted")
    hint.grid(row=4, column=1, columnspan=6)

def addeuroplay():
    S = entryeuro.get()
    if S != "" and S in EuroLib:
        entryeuro.delete(0, tk.END)
        if len(Euro) == 0:
            Euroinsertlist.insert(tk.END, S)
            Euro.append(S)
        else:
            Euro.append(S)
            S = "\n" + S
            Euroinsertlist.insert(tk.END, S)

def addafroplay():
    S = entryafro.get()
    if S != "" and S in AfroLib:
        entryafro.delete(0, tk.END)
        if len(Afro) == 0:
            Afroinsertlist.insert(tk.END, S)
            Afro.append(S)
        else:
            Afro.append(S)
            S = "\n" + S
            Afroinsertlist.insert(tk.END, S)

def addasiaplay():
    S = entryasia.get()
    if S != "" and S in AsiaLib:
        entryasia.delete(0, tk.END)
        if len(Asia) == 0:
            Asiainsertlist.insert(tk.END, S)
            Asia.append(S)
        else:
            Asia.append(S)
            S = "\n" + S
            Asiainsertlist.insert(tk.END, S)

def addnaplay():
    S = entryna.get()
    if S != "" and S in NALib:
        entryna.delete(0, tk.END)
        if len(NA) == 0:
            NAinsertlist.insert(tk.END, S)
            NA.append(S)
        else:
            NA.append(S)
            S = "\n" + S
            NAinsertlist.insert(tk.END, S)

def addsaplay():
    S = entrysa.get()
    if S != "" and S in SALib:
        entrysa.delete(0, tk.END)
        if len(SA) == 0:
            SAinsertlist.insert(tk.END, S)
            SA.append(S)
        else:
            SA.append(S)
            S = "\n" + S
            SAinsertlist.insert(tk.END, S)

def addoceaniaplay():
    S = entryoceania.get()
    if S != "" and S in OceaniaLib:
        entryoceania.delete(0, tk.END)
        if len(Oceania) == 0:
            Oceaniainsertlist.insert(tk.END, S)
            Oceania.append(S)
        else:
            Oceania.append(S)
            S = "\n" + S
            Oceaniainsertlist.insert(tk.END, S)

def add_countries():
    countriesadd=tk.Toplevel()
    countriesadd.title("Countries list")

    conttitle = tk.Label(countriesadd, text="Countries")
    conttitle.grid(row=1, column=1, columnspan=6)

    eurotitle = tk.Label(countriesadd, text="Europe")
    eurotitle.grid(row=2, column=1)
    afrotitle = tk.Label(countriesadd, text="Africa")
    afrotitle.grid(row=2, column=2)
    asiatitle = tk.Label(countriesadd, text="Asia")
    asiatitle.grid(row=2, column=3)
    satitle = tk.Label(countriesadd, text="South America")
    satitle.grid(row=2, column=5)
    natitle = tk.Label(countriesadd, text="North America")
    natitle.grid(row=2, column=4)
    oceantitle = tk.Label(countriesadd, text="Oceania")
    oceantitle.grid(row=2, column=6)

    global Euroinsertlist,Afroinsertlist,Asiainsertlist,NAinsertlist,SAinsertlist,Oceaniainsertlist

    Euroinsertlist = scrolledtext.ScrolledText(countriesadd, width=20, height=20)
    Afroinsertlist = scrolledtext.ScrolledText(countriesadd, width=20, height=20)
    Asiainsertlist = scrolledtext.ScrolledText(countriesadd, width=20, height=20)
    NAinsertlist = scrolledtext.ScrolledText(countriesadd, width=20, height=20)
    SAinsertlist = scrolledtext.ScrolledText(countriesadd, width=20, height=20)
    Oceaniainsertlist = scrolledtext.ScrolledText(countriesadd, width=20, height=20)

    Euroinsertlist.grid(row=3,column=1)
    Afroinsertlist.grid(row=3,column=2)
    Asiainsertlist.grid(row=3,column=3)
    NAinsertlist.grid(row=3,column=4)
    SAinsertlist.grid(row=3,column=5)
    Oceaniainsertlist.grid(row=3,column=6)

    addeuro=tk.Button(countriesadd,text="Add inputted country",command=addeuroplay)
    addafro=tk.Button(countriesadd,text="Add inputted country",command=addafroplay)
    addasia=tk.Button(countriesadd,text="Add inputted country",command=addasiaplay)
    addna=tk.Button(countriesadd,text="Add inputted country",command=addnaplay)
    addsa=tk.Button(countriesadd,text="Add inputted country",command=addsaplay)
    addoceania=tk.Button(countriesadd,text="Add inputted country",command=addoceaniaplay)

    global entryeuro,entryafro,entryasia,entryna,entrysa,entryoceania

    entryeuro=tk.Entry(countriesadd,width=20)
    entryafro=tk.Entry(countriesadd,width=20)
    entryasia=tk.Entry(countriesadd,width=20)
    entryna=tk.Entry(countriesadd,width=20)
    entrysa=tk.Entry(countriesadd,width=20)
    entryoceania=tk.Entry(countriesadd,width=20)

    entryeuro.grid(row=4,column=1)
    entryafro.grid(row=4,column=2)
    entryasia.grid(row=4,column=3)
    entryna.grid(row=4,column=4)
    entrysa.grid(row=4,column=5)
    entryoceania.grid(row=4,column=6)

    addeuro.grid(row=5,column=1)
    addafro.grid(row=5,column=2)
    addasia.grid(row=5,column=3)
    addna.grid(row=5,column=4)
    addsa.grid(row=5,column=5)
    addoceania.grid(row=5,column=6)

    hint=tk.Label(countriesadd,text="You should add enough countries here first to make the bild happens")

    hint.grid(row=6,column=1,columnspan=6,pady=5)

def report():
    reportlvl=tk.Toplevel()
    reportlvl.title("Report bug")

    Content=tk.Label(reportlvl,text="Warning : This is just the beta version\nIn case of bugs , u can report everything to my email : aminhfz01@gmail.com\nWith ur interaction we can improve the app to the better =)")
    Content.pack()

def exit():
    root.destroy()

root=tk.Tk()
root.title("World Cup Bilding")

menu=tk.Menu(root)

countries=tk.Menu(menu)

menu.add_cascade(label="Countries Settings",menu=countries)
countries.add_command(label="Show Countries list",command=show)
countries.add_command(label="Config countries libs",command=add_countries)

howto=tk.Menu(menu)

menu.add_cascade(label="The How to",menu=howto)
howto.add_command(label="How to bild")
howto.add_command(label="How to use the app")
howto.add_command(label="How to report bugs",command=report)


menu.add_command(label="About",command=about)
menu.add_command(label="Exit",command=exit)

root.config(menu=menu)

title=tk.Label(root,text="Choose the number of countries in ur world cup : ")
choosing_frame=tk.Frame(root)
frame_of_46=tk.Frame(choosing_frame)
frame_of_32=tk.Frame(choosing_frame)

select32=tk.Button(frame_of_32,text="32 countries",command=goto32mode)
hint32=tk.Label(frame_of_32,text="* 32 Countries in total\n* 8 Groups on group stages\n* 2 Teams from each group qualify to the finals\n* 4 Final rounds : round of 16,1/4 finals,1/2 finals and the final")

select32.pack(pady=5,padx=5)
hint32.pack(padx=5,pady=5)

select46=tk.Button(frame_of_46,text="46 countries",command=goto46mode)
hint46=tk.Label(frame_of_46,text="* 46 Countries in total\n* 12 Groups on group stages\n* 2 Teams from each group qualify to the finals and\nthird teams in each group get classed so the only 8 first move with the 24 first teams\n* 5 Final rounds : round of 32,round of 16,1/4 finals,1/2 finals and the final")

select46.pack(pady=5,padx=5)
hint46.pack(padx=5,pady=5)

frame_of_32.grid(row=1,column=1,padx=5)
frame_of_46.grid(row=1,column=3,padx=5)

title.pack(pady=5)
choosing_frame.pack(padx=5)

root.mainloop()