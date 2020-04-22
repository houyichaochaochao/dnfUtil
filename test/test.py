#-*-coding:utf-8-*-

aa = "123123"

print(aa[-1])
print(aa[-2])
print(aa[2:4]) # 时刻遵循着左闭右开的原则


bb = [(2,{3:"as"}),(2,3),(4,5)]

print(bb[0][0])
print(bb[0][1][3])
# print(bb[1][1][2])


print(aa[1:3])


a = [1,4,2,3,2,3,4,2]
from collections import Counter
print (Counter(a) )


a = [1,4,2,3,2,3,4,2]
from collections import Counter
print (Counter(a).most_common(1))
