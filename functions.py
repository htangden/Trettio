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
    

def backprop(hypercubes, s):
    chi = [0]

    for i, hypercube in enumerate(hypercubes):
        if i == 0: # 1 dice
            sum = 0
            for a in hypercube:
                sum += a[0]
            sum /= (s**(i+1))
            chi.append(sum)
        elif i == 1: # 2 dice
            sum = 0
            for b in hypercube:
                for a in b:
                    a.sort(reverse=True)
                    x = a
                    sum += x[0]
                    if x[1] > (chi[1]-chi[0]):
                        sum += x[1]
                        print(x)
                    else: 
                        sum += chi[1]
            sum /= (s**(i+1))
            chi.append(sum)
        elif i == 2: # 3 dice
            sum = 0
            for c in hypercube:
                for b in c:
                    for a in b:
                        a.sort(reverse=True)
                        x = a
                        sum += x[0]
                        if x[1] > (chi[2]-chi[1]):
                            sum += x[1]
                            if x[2] > (chi[1]-chi[0]):
                                sum += x[2]
                            else:
                                sum += chi[1]
                        else:
                            sum += chi[2]
            sum /= (s**(i+1))
            chi.append(sum)
        elif i == 3: # 4 dice
            for d in hypercube:
                for c in d:
                    for b in c:
                        for a in b:
                            a.sort(reverse=True)
                            x = a
                            sum += x[0]
                            if x[1] > (chi[3] - chi[2]):
                                sum += x[1]
                                if x[2] > (chi[2] - chi[1]):
                                    sum += x[2]
                                    if x[3] > (chi[1] - chi[0]):
                                        sum += x[3]
                                    else:
                                        sum += chi[1]
                                else:
                                    sum += chi[2]
                            else:
                                sum += chi[3]
            sum /= (s**(i+1))
            chi.append(sum)
        elif i == 4: # 5 dice
            for e in hypercube:
                for d in e:
                    for c in d:
                        for b in c:
                            for a in b:
                                a.sort(reverse=True)
                                x = a
                                sum += x[0]
                                if x[1] > (chi[4] - chi[3]):
                                    sum += x[1]
                                    if x[2] > (chi[3] - chi[2]):
                                        sum += x[2]
                                        if x[3] > (chi[2] - chi[1]):
                                            sum += x[3]
                                            if x[4] > (chi[1] - chi[0]):
                                                sum += x[4]
                                            else:
                                                sum += chi[1]
                                        else:
                                            sum += chi[2]
                                    else:
                                        sum += chi[3]
                                else:
                                    sum += chi[4]
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
                                    x = a
                                    sum += x[0]
                                    if x[1] > (chi[5] - chi[4]):
                                        sum += x[1]
                                        if x[2] > (chi[4] - chi[3]):
                                            sum += x[2]
                                            if x[3] > (chi[3] - chi[2]):
                                                sum += x[3]
                                                if x[4] > (chi[2] - chi[1]):
                                                    sum += x[4]
                                                    if x[5] > (chi[1] - chi[0]):
                                                        sum += x[5]
                                                    else:
                                                        sum += chi[1]
                                                else:
                                                    sum += chi[2]
                                            else:
                                                sum += chi[3]
                                        else:
                                            sum += chi[4]
                                    else:
                                        sum += chi[5]
            sum /= (s**(i+1))
            chi.append(sum)
    return(chi)

    def find_highest_expval(x, chi): # x: a single possible dice throw
        highest_expval = 0

        for i in range(len(x)):
            sum = 0
            for j in range(i):
                sum += x[j]
            expval = x[0] + sum + chi[len[x]-i]
            if expval > highest_expval:
                highest_expval = expval

