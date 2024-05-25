from numpy import array
from random import *

NAT=["austria","belgium","bulgaria","croatia","czech rep","denmark","england","finland","france","germany","greece","iceland","ireland","i5rel","italy","hungary","netherlands","norwege","poland","portugal","romania","russia","scotland","serbia","slovakia","slovenia","spain","sweeden","switherland","turkey","ukrania","wales","algeria","egypt","cameroon","ghana","senegal","morocco","nigeria","south africa","tunisia","costa rica","canada","mexico","jamaica","usa","argentina","brazil","chile","colombia","ecuadro","panama","peru","uruguay","australia","china","iran","irak","japan","new zeeland","north korea","ksa","south korea","qatar"]

def Select(S,C):
    if S[C]==1:
        if C==0:
            M=randint(1,17)
        elif C==1:
            M=randint(1,33)
        elif C==2:
            M=randint(33,42)
        elif C==3:
            M=randint(42,55)
        elif C==4:
            M=randint(55,65)
    return M

def VerifLocal(T,A,occ):
    for i in range (0,4):
        if T[i]==A:
            occ=occ+1

def VerifOcc(A,G1,G2,G3,G4,G5,G6,G7,G8):
    Ok=False
    occ=0
    VerifLocal(G1,A,occ)
    VerifLocal(G2,A,occ)
    VerifLocal(G3,A,occ)
    VerifLocal(G4,A,occ)
    VerifLocal(G5,A,occ)
    VerifLocal(G6,A,occ)
    VerifLocal(G7,A,occ)
    VerifLocal(G8,A,occ)
    return occ<=1

def Groupfill(T,G1,G2,G3,G4,G5,G6,G7,G8):
    S=array([1]*5)
    for i in range (0,4):
        C=randint(0,5)
        while S[C]==0:
            C=randint(1,6)
        T[i]=Select(S,C)
        while VerifOcc(T[i],G1,G2,G3,G4,G5,G6,G7,G8)==False:
            T[i]=Select(S,C)
        S[C]=0

def show(T,NAT):
    for i in range(0,4):
        print(NAT[(T[i])])

G1=array([int(0)]*4)
G2=array([int(0)]*4)
G3=array([int(0)]*4)
G4=array([int(0)]*4)
G5=array([int(0)]*4)
G6=array([int(0)]*4)
G7=array([int(0)]*4)
G8=array([int(0)]*4)

Groupfill(G1,G1,G2,G3,G4,G5,G6,G7,G8)
Groupfill(G2,G1,G2,G3,G4,G5,G6,G7,G8)
Groupfill(G3,G1,G2,G3,G4,G5,G6,G7,G8)
Groupfill(G4,G1,G2,G3,G4,G5,G6,G7,G8)
Groupfill(G5,G1,G2,G3,G4,G5,G6,G7,G8)
Groupfill(G6,G1,G2,G3,G4,G5,G6,G7,G8)
Groupfill(G7,G1,G2,G3,G4,G5,G6,G7,G8)
Groupfill(G8,G1,G2,G3,G4,G5,G6,G7,G8)

print("Elements of group 1 are : ")
show(G1,NAT)
print("Elements of group 2 are : ")
show(G2,NAT)
print("Elements of group 3 are : ")
show(G3,NAT)
print("Elements of group 4 are : ")
show(G4,NAT)
print("Elements of group 5 are : ")
show(G5,NAT)
print("Elements of group 6 are : ")
show(G6,NAT)
print("Elements of group 7 are : ")
show(G7,NAT)
print("Elements of group 8 are : ")
show(G8,NAT)