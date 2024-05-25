from random import randint

Euro=[]
Asia=[]
Afro=[]
NA=[]
SA=[]

EndFilling=False
while EndFilling==False :
    Continent=input("Pick a continent to add a country in it (Europe/Asia/Africa/North America/South America) : ")
    match Continent.upper() :
        case "EUROPE" :
            Country=input("Add an european country : ")
            Country=Country.upper()
            Euro.append(Country)
        case "AFRICA" :
            Country=input("Add an african country : ")
            Country=Country.upper()
            Afro.append(Country)
        case "ASIA" :
            Country=input("Add an asian country : ")
            Country=Country.upper()
            Asia.append(Country)
        case "NORTH AMERICA" :
            Country=input("Add a north american country : ")
            Country=Country.upper()
            NA.append(Country)
        case "SOUTH AMERICA" :
            Country=input("Add a south american country : ")
            Country=Country.upper()
            SA.append(Country)
        case _ :
            print("Write a valid continent (Europe/Asia/Africa/North America/South America)")
    EndAsk=input("u wanna end ? (Y/N) : ")
    while EndAsk not in {"Y"/"N"} :
        EndAsk=input("choose only Y/N : ")
    if EndAsk=="N":
        EndFilling=False
    else :
        EndFilling=((len(Euro)+len(Afro)+len(Asia)+len(NA)+len(SA)>=32)and(len(Euro)>=13)and(len(Afro)>=5)and(len(Asia)>=5)and(len(NA)+len(SA)>=9))

G1,G2,G3,G4,G5,G6,G7,G8=[],[],[],[],[],[],[],[]
Gr1,Gr2,Gr3,Gr4,Gr5,Gr6,Gr7,Gr8=[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]
NEuro=len(Euro)-1
NAfro=len(Afro)-1
NAsia=len(Asia)-1
NNA=len(NA)-1
NSA=len(SA)-1

def FillGroupe(T,TG,NEuro,NAfro,NAsia,NNA,NSA):
    for x in range (0,3):
        Test=False
        while Test==False :
            CCh=randint(0,4)
            match CCh :
                case 0:
                    Test=(TG[CCh]==2)
                case _ :
                    Test=(TG[CCh]==1)
            if Test==False :
                TG[CCh]=TG[CCh]+1
                match CCh :
                    case 0:
                        Count=randint(0,NEuro)
                        while Euro[Count]=="":
                            Count=randint(0,NEuro)
                        T.append(Euro[Count])
                        Euro[Count]=""
                    case 1:
                        Count=randint(0,NAfro)
                        while Afro[Count]=="":
                            Count=randint(0,NAfro)
                        T.append(Afro[Count])
                        Afro[Count]=""
                    case 2:
                        Count=randint(0,NAsia)
                        while Asia[Count]=="":
                            Count=randint(0,NAsia)
                        T.append(Asia[Count])
                        Asia[Count]=""
                    case 3:
                        Count=randint(0,NNA)
                        while NA[Count]=="":
                            Count=randint(0,NNA)
                        T.append(NA[Count])
                        NA[Count]=""
                    case 4 :
                        Count=randint(0,NSA)
                        while SA[Count]=="":
                            Count=randint(0,NSA)
                        T.append(SA[Count])
                        SA[Count]=""

FillGroupe(G1,Gr1,NEuro,NAfro,NAsia,NNA,NSA)
FillGroupe(G2,Gr2,NEuro,NAfro,NAsia,NNA,NSA)
FillGroupe(G3,Gr3,NEuro,NAfro,NAsia,NNA,NSA)
FillGroupe(G4,Gr4,NEuro,NAfro,NAsia,NNA,NSA)
FillGroupe(G5,Gr5,NEuro,NAfro,NAsia,NNA,NSA)
FillGroupe(G6,Gr6,NEuro,NAfro,NAsia,NNA,NSA)
FillGroupe(G7,Gr7,NEuro,NAfro,NAsia,NNA,NSA)
FillGroupe(G8,Gr8,NEuro,NAfro,NAsia,NNA,NSA)

print("G1:")
print(G1)
print("G2:")
print(G2)
print("G3:")
print(G3)
print("G4:")
print(G4)
print("G5:")
print(G5)
print("G6:")
print(G6)
print("G7:")
print(G7)
print("G8:")
print(G8)