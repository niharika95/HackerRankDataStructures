from __future__ import print_function

a = [1,2,3,4,5]
d = 4
for i in range(0,d):
    temp = a[0]
    del a[0]
    a.append(temp)

print (*a)