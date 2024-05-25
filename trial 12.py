from random import randint,shuffle

def checkseq(L):
    Ok=True
    for i in range(len(seq1)-2):
        if L[i][0]==L[i+1][0] or L[i][0]==L[i+2][0]:
            Ok=False
    return Ok

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

print(seq1)
print(seq2)

shuffle(seq1)
while not(checkseq(seq1)):
    shuffle(seq1)

shuffle(seq2)
while not(checkseq(seq2)):
    shuffle(seq2)

print(seq1)
print(seq2)