def spawn(m):
    flag = []
    while m>=2:
        if m%2 == 0:
            flag.append(0)
        else:
            flag.append(1)
        #print(m,end=" ")
        m = int(m/2)
    return flag
def spawnfinaldig(m):
    final = []
    while m>=2:
        if m%2 == 0:
            final.append(int(m/2))
        else:
            final.append(int((m-1)/2))
        m = int(m/2)
    return final

def find(flag,a,final,n):

    if final[-1] == 1:
        fn = final[-2]
        result = (a**fn) % n
        print(result)
        for i in range(len(final)-1,0,-1):
            #print(i)
            if flag[i-1] == 1:
                result = ((result**2)*a) % n
                print(result, "1")
                #print(result, end=" ")
            else:
                result = (result**2) % n
                print(result, "0")
                #print(result, end=" ")
    else:
        for i in range(len(final),0,-1):
            if flag[i] == 1:
                result = (((a**fn)**2)*n) % n
            else:
                result = ((a**fn)**2) % n
    return result
if __name__ == '__main__':
    print(spawn(6217))
    flag = spawn(6217)
    print(spawnfinaldig(6217))
    final = spawnfinaldig(6217)
    print(find(flag,419,final,6216))