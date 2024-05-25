from random import randint

Euro=["austria","belgium","bulgaria","croatia","czech rep","denmark","england","finland","france","germany","greece","iceland","ireland","i5rel","italy","hungary","netherlands","norwege","poland","portugal","romania","russia","scotland","serbia","slovakia","slovenia","spain","sweeden","switherland","turkey","ukrania","wales"]
Afro=["algeria","egypt","cameroon","ghana","senegal","morocco","nigeria","south africa","tunisia"]
NA=["costa rica","canada","mexico","jamaica","usa"]
SA=["argentina","brazil","chile","colombia","ecuadro","panama","peru","uruguay"]
Asia=["australia","china","iran","irak","japan","new zeeland","north korea","ksa","south korea","qatar"]

print("World Cup : Winner Soccer Evolution")

G1,G2,G3,G4,G5,G6,G7,G8=[],[],[],[],[],[],[],[]
Gr1,Gr2,Gr3,Gr4,Gr5,Gr6,Gr7,Gr8=[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]


def FillGroupe(T,TG,Euro,Afro,Asia,NA,SA):
    for x in range (0,4) :
        print(T)
        NEuro=len(Euro)-1
        NAfro=len(Afro)-1
        NAsia=len(Asia)-1
        NNA=len(NA)-1
        NSA=len(SA)-1
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
                        T.append(Euro[Count])
                        del Euro[Count]
                    case 1:
                        Count=randint(0,NAfro)
                        T.append(Afro[Count])
                        del Afro[Count]
                    case 2:
                        Count=randint(0,NAsia)
                        T.append(Asia[Count])
                        del Asia[Count]
                    case 3:
                        Count=randint(0,NNA)
                        T.append(NA[Count])
                        del NA[Count]
                    case 4 :
                        Count=randint(0,NSA)
                        T.append(SA[Count])
                        del SA[Count]
    

FillGroupe(G1,Gr1,Euro,Afro,Asia,NA,SA)
FillGroupe(G2,Gr2,Euro,Afro,Asia,NA,SA)
FillGroupe(G3,Gr3,Euro,Afro,Asia,NA,SA)
FillGroupe(G4,Gr4,Euro,Afro,Asia,NA,SA)
FillGroupe(G5,Gr5,Euro,Afro,Asia,NA,SA)
FillGroupe(G6,Gr6,Euro,Afro,Asia,NA,SA)
FillGroupe(G7,Gr7,Euro,Afro,Asia,NA,SA)
FillGroupe(G8,Gr8,Euro,Afro,Asia,NA,SA)

def Check(T):
    if len(T)>4:
        del T[len(T)-1]

Check(G1)
Check(G2)
Check(G3)
Check(G4)
Check(G5)
Check(G6)
Check(G7)
Check(G8)

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