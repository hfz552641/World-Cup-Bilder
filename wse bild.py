from numpy import array
from random import *

NAT=["austria","belgium","bulgaria","croatia","czech rep","denmark","england","finland","france","germany","greece","iceland","ireland","i5rel","italy","hungary","netherlands","norwege","poland","portugal","romania","russia","scotland","serbia","slovakia","slovenia","spain","sweeden","switherland","turkey","ukrania","wales","algeria","egypt","cameroon","ghana","senegal","morocco","nigeria","south africa","tunisia","costa rica","canada","mexico","jamaica","usa","argentina","brazil","chile","colombia","ecuadro","panama","peru","uruguay","australia","china","iran","irak","japan","new zeeland","north korea","ksa","south korea","qatar"]

print("World Cup : Winner Soccer Evolution")

G1=array([int(0)]*4)
G2=array([int(0)]*4)
G3=array([int(0)]*4)
G4=array([int(0)]*4)
G5=array([int(0)]*4)
G6=array([int(0)]*4)
G7=array([int(0)]*4)
G8=array([int(0)]*4)

EuMax=13
AfMax=5
AsMax=5
AmMax=9

def VerifLocal(T,A,occ):
    for i in range (0,4):
        if T[i]==A:
            occ=occ+1

def VerifOcc(A):
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

def VerifValid(T,A):
    Val=True
    eug=0
    afg=0
    amg=0
    asg=0
    for i in range(0,4):
        if 1<=T[i]<=32:
            eug=eug+1
        elif 33<=T[i]<=41:
            afg=afg+1
        elif 42<=T[i]<=54:
            amg=amg+1
        elif T[i]>=55:
            asg=asg+1
    if ((eug==2)and(1<=A<=32))or((afg==1)and(33<=A<=41))or((amg==1)and(42<=A<=54))or((asg==1)and(A>=55)):
        Val=False
    return Val

def Valid(T,A):
    Test=True
    Test=VerifValid(T,A)
    return Test

G1[0]=randint(1,56)
for i in range (1,4):
    G1[i]=randint(1,56)
    while Valid(G1,G1[i])==False or VerifOcc(G1[i])==False:
        G1[i]=randint(1,56)

def add(T):
    for i in range (0,4):
        T[i]=randint(1,56)
        while Valid(T,T[i])==False or VerifOcc(T[i])==False:
            T[i]=randint(1,56)
            
add(G2)
add(G3)
add(G4)
add(G5)
add(G6)
add(G7)
add(G8)

def show(T,NAT):
    for i in range(0,4):
        print(NAT[(T[i])])
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