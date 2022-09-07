
f = open("/Users/michaeltu/Downloads/rosalind_dna (5).txt", "r")

sequence = f.read()

A = 0
G = 0
T = 0
C = 0

for letter in sequence:
    if letter == "A":
        A += 1
    elif letter == "G":
        G += 1
    elif letter == "T":
        T += 1
    elif letter == "C":
        C += 1  #changed from else statement --> resulted in one more C because read() adds an extra white space
    else:
        misc += 1
print(str(A)+" "+str(C)+" "+str(G)+" "+str(T))



