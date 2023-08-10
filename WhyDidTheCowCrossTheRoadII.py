import sys
sys.stdin = open("circlecross.in","r")
sys.stdout = open("circlecross.out","w")
points = input()
letters = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
count = 0
for i in letters.keys():
    letters = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
    found = False
    for x in points:
        if x ==i and found != True:
            found = True
        elif found == True:
            if x == i:
                break
            letters[x] += 1
    for y in letters.values():
        if y == 1:
            count += 1
print(int(count/2))
