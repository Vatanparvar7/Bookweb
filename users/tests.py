from django.test import TestCase
a=[[7,8],[8,9],[9,8],[8,7],[4,6]]
for i in range(0,len(a)):
    s=0
    for j in range(i+1,len(a)):
        if a[i][0]==a[j-s][1] and a[i][1]==a[j-s][0]:
            a.pop(j-s)
            s+=1
print(a)

