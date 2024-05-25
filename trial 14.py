from random import randint, shuffle
from numpy import empty


Euro = ['Albania', 'Austria', 'Belgium', 'Bosnia & Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'England', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Montenegro', 'Netherlands', 'North Macedonia', 'Northern Ireland', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'Wales']

Afro = ['Algeria', 'Angola', 'Benin', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Comoros', 'Congo Rep.', 'DRC', 'Egypt', 'Equatorial Guinea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Morocco', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

SA = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']

NA = ['Bahamas', 'Barbados', 'Belize', 'Bermuda', 'Canada', 'Costa Rica', 'Cuba', 'Curaçao', 'Dominica', 'Dominican Republic', 'El Salvador', 'French Guiana', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guyana', 'Haiti', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Nicaragua', 'Panama', 'Saint Lucia', 'Snt Vincent & Gren.', 'Suriname', 'Trinidad and Tobago', 'USA']

Asia = ['Australia', 'Bahrain', 'Brunei', 'Cambodia', 'China', 'India', 'Indonesia', 'Iran', 'Iraq', 'Japan', 'Jordan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar (Burma)', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Turkmenistan', 'UAE', 'Uzbekistan', 'Vietnam', 'Yemen']

Oceania = ['Fiji', 'New Zealand', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Vanuatu']


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
        print("North African Countries :",end=" ")
        print(QNA)
        print("South African Countries :",end=" ")
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
                A2 = randint(0, 7)
                while P2[A2] in G:
                    A2 = randint(0, 11)
                G.append(P2[A2])
                A3 = randint(0, 7)
                while P3[A3] in G:
                    A3 = randint(0,11)
                G.append(P3[A3])
                A4 = randint(0, 7)
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
    except Exception as e:
        main()



if __name__ == "__main__":
    main()

