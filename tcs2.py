n = int(input())
s = input()
l = ["-"] * n
for i in range(n):
    if s[i] != "-":
        l[i] = (s[i],0)
for i in range(n):
    if  l[i] == ("A",0) or l[i] == ("B",0):
        c , w = l[i][0] , l[i][1]
        if c == "A":
            for j in range(i-1,-1,-1):
                w += 1
                if l[j] == "-":
                    l[j] = ("A",w)
                else:
                    break
for i in range(n):
    if  l[i] == ("A",0) or l[i] == ("B",0):
        c , w = l[i][0] , l[i][1]
        if c == "B":
            for j in range(i+1,n):
                w += 1
                if l[j] == "-":
                    l[j] = ("b",w)
                else:
                    w1 = l[j][1]
                    if w1 == 0:
                        break
                    if w1 > w :
                        l[j] = ("B",w)
                    if w1 == w:
                        l[j] = "-"
a=0
b =0
for i in l:
    if i != "-":
        if i[0] == "A":
            a+=1
        else:
            b+=1
if a > b:
    print("A")
elif b > a :
    print("B")
else:
    print("coalition government.")
        
