import math
def spawnq(n,m):
    q = []
    np = 1  # natural parts
    rmd = 1 #remainder
    while rmd >= 1:
        rmd = m % n
        np = int(m/n)
        q.append(np)
        m = n
        n = rmd
    return q
def findpos(n,m):
    r = []
    rmd = 1
    pos = [] #position that the remainder = 1
    while rmd>0:
        rmd = m % n
        r.append(rmd)
        m = n
        n = rmd
    for i,x in enumerate(r):
        if x == 1:
            pos.append(i)
    return pos
def spawnans(q,pos):
    x = [0,1]
    y = [1,0]
    a = []
    for i in range(len(q)):
        x.append(x[i]-q[i]*x[i+1])
        y.append(y[i]-q[i]*y[i+1])
    for b in pos:
        if x[b+2] >= 0:
            a.append(x[b+2])
    print(x)
    return a

if __name__ == '__main__':
    print("Nhập số n:")
    n = int(input())
    print("Nhập số m:")
    m = int(input())
    if math.gcd(m,n) == 1:
        print("không có")
    else:
        pos = findpos(n,m)
        q = spawnq(n,m)
        print(q)
        print(spawnans(q,pos))