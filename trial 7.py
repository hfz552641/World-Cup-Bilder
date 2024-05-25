

G=[]
i=0
for i in range(4):
    A=input("Give the "+str(i+1)+" element : ")
    G.append(A)
print(G)

def treat(G,Result,i,j,Score,GS,GC,GT):
    Teamigoals=int(Result[:Result.find("-")])
    Teamjgoals=int(Result[Result.find("-")+1:])
    if Teamigoals>Teamjgoals:
        Score[i]=Score[i]+3
    elif Teamjgoals>Teamigoals:
        Score[j]=Score[j]+3
    elif Teamigoals==Teamjgoals :
        Score[i]=Score[i]+1
        Score[j]=Score[j]+1
    GS[i]+=Teamigoals
    GS[j]+=Teamjgoals
    GC[i]-=Teamjgoals
    GC[j]-=Teamigoals
    GT[i]=GS[i]+GC[i]
    GT[j]=GS[j]+GC[j]

Score=[0,0,0,0]
GS=[0,0,0,0]
GC=[0,0,0,0]
GT=[0,0,0,0]

print("Round 1:")
Result=input(G[0] + " vs " + G[1]+" : ")
treat(G,Result,0,1,Score,GS,GC,GT)
Result=input(G[2] + " vs " + G[3]+" : ")
treat(G,Result,2,3,Score,GS,GC,GT)

print("Round 2:")
Result=input(G[0] + " vs " + G[2]+" : ")
treat(G,Result,0,2,Score,GS,GC,GT)
Result=input(G[1] + " vs " + G[3]+" : ")
treat(G,Result,1,3,Score,GS,GC,GT)

print("Round 3:")
Result=input(G[0] + " vs " + G[3]+" : ")
treat(G,Result,0,3,Score,GS,GC,GT)
Result=input(G[1] + " vs " + G[2]+" : ")
treat(G,Result,1,2,Score,GS,GC,GT)

def sort(G,Score,GS,GC,GT):
    Test=False
    while not(Test):
        Test=True
        for x in range(1,4):
            if Score[x-1]<Score[x]:
                Score[x-1],Score[x]=Score[x],Score[x-1]
                G[x-1],G[x]=G[x],G[x-1]
                GS[x-1],GS[x]=GS[x],GS[x-1]
                GC[x-1],GC[x]=GC[x],GC[x-1]
                GT[x-1],GT[x]=GT[x],GT[x-1]
                Test=False
            elif Score[x-1]==Score[x] and GT[x-1]<GT[x]:
                Score[x-1],Score[x]=Score[x],Score[x-1]
                G[x-1],G[x]=G[x],G[x-1]
                GS[x-1],GS[x]=GS[x],GS[x-1]
                GC[x-1],GC[x]=GC[x],GC[x-1]
                GT[x-1],GT[x]=GT[x],GT[x-1]
                Test=False

sort(G,Score,GS,GC,GT)

print(G)
print(Score)
print(GS)
print(GC)
print(GT)

