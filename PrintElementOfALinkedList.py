N = 4
a = ['aba', 'baba', 'aba', 'xzxb']
Q = 3
b = ['aba', 'xzxb', 'ab']

countList = []

for i in range(0, len(Q)):
    count = 0
    for j in range(0,len(N)):
        if(b[i] == a[j]):
            count += 1
    countList.append(count)

for i in countList:
    print (i)