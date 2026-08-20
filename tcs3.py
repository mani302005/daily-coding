a , b = map(int,input().split())
n = int(input())
arr = list(map(float,input().split()))
lista = []
listb = []
for i in range(b-1,n):
    aavg = sum(arr[i-a+1:i+1])
    bavg = sum(arr[i-b+1:i+1])
    lista.append(aavg/a)
    listb.append(bavg/b)
l =[]
c = 0
if lista[0] < listb[0]:
    l.append("A")
else:
    l.append("B")
for i in range(1,len(list(lista))):
    if lista[i] < listb[i]:
        l.append("A")
    else:
        l.append("B")
    if l[-1]  != l[-2]:
        c+=1
print( c)

    
    
