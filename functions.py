import numpy as np

def predict_highest_dice(n): #n: amount of six sided dice
    sum = 0
    for i in range(6):
        sum += (i+1)*((i+1)**n-i**n)
    return sum/(6**n)


def chi(s):
    sum = 0
    for x in range(s):
        sum += (x+1)*((x+1)**2-x**2)
    return 1/(s**2) * (1/16*(9*s**3 + 8*s**2) + sum)

def create_hypercube(s, d):
    arr = []
    if d == 1:
        for i in range(s):
            arr.append([i+1])
    elif d == 2:
        for i in range(s):
            arr.append([])
            for j in range(s):
                arr[i].append([i+1, j+1])
    elif d == 3:
        for i in range(s):
            arr.append([])
            for j in range(s):
                arr[i].append([])
                for k in range(s):
                    arr[i][j].append([i+1, j+1, k+1])
    elif d == 4:
        for i in range(s):
            arr.append([])
            for j in range(s):
                arr[i].append([])
                for k in range(s):
                    arr[i][j].append([])
                    for l in range(s):
                        arr[i][j][k].append([i+1, j+1, k+1, l+1])
    elif d == 5:
        for i in range(s):
            arr.append([])
            for j in range(s):
                arr[i].append([])
                for k in range(s):
                    arr[i][j].append([])
                    for l in range(s):
                        arr[i][j][k].append([])
                        for m in range(s):
                            arr[i][j][k][l].append([i+1, j+1, k+1, l+1, m+1])
    elif d == 6:
        for i in range(s):
            arr.append([])
            for j in range(s):
                arr[i].append([])
                for k in range(s):
                    arr[i][j].append([])
                    for l in range(s):
                        arr[i][j][k].append([])
                        for m in range(s):
                            arr[i][j][k][l].append([])
                            for n in range(s):
                                arr[i][j][k][l][m].append([i+1, j+1, k+1, l+1, m+1, n+1])
    return arr
    [1], [0]
def find_highest_expval(x, chi): # x: a single possible dice throw, sorted in descending order || chi[y] gives the value of saving y amount of dice
        highest_expval = 3.5 # bad solution, ik, but it works

        saved = [] # saved[y] gives the value of saving y amount of dice
        for i in range(len(x)+1):
            sum = 0
            for j in range(i):
                sum += x[j]
            saved.append(sum)

        for i in range(1, len(x)): # now we want test which combination of  saved[a] + chi[b], (a + b = len(x)-1), (a>1), gives the highest value

            expval = saved[i] + chi[len(x)-i]
            if expval > highest_expval:
                highest_expval = expval 
        
        return highest_expval


def backprop(hypercubes, s):
    chi = [0]

    for i, hypercube in enumerate(hypercubes):
        if i == 0: # 1 dice
            sum = 0
            for a in hypercube:
                sum += find_highest_expval(a, chi)
            sum /= (s**(i+1))
            chi.append(sum)
        elif i == 1: # 2 dice
            sum = 0
            for b in hypercube:
                for a in b:
                    a.sort(reverse=True)
                    sum += find_highest_expval(a, chi)
            sum /= (s**(i+1))
            chi.append(sum)
        elif i == 2: # 3 dice
            sum = 0
            for c in hypercube:
                for b in c:
                    for a in b:
                        a.sort(reverse=True)
                        sum += find_highest_expval(a, chi)
            sum /= (s**(i+1))
            chi.append(sum)
        elif i == 3: # 4 dice
            for d in hypercube:
                for c in d:
                    for b in c:
                        for a in b:
                            a.sort(reverse=True)
                            sum += find_highest_expval(a, chi)
            sum /= (s**(i+1))
            chi.append(sum)
        elif i == 4: # 5 dice
            for e in hypercube:
                for d in e:
                    for c in d:
                        for b in c:
                            for a in b:
                                a.sort(reverse=True)
                                sum += find_highest_expval(a, chi)
            sum /= (s**(i+1))
            chi.append(sum)
        else: # 6 dice
            for f in hypercube:
                for e in f:
                    for d in e:
                        for c in d:
                            for b in c:
                                for a in b:
                                    a.sort(reverse=True)
                                    sum += find_highest_expval(a, chi)
            sum /= (s**(i+1))
            chi.append(sum)
    return(chi)

