def name_to_word(n):
    if n == 100:
        return "hundred"
    ones = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    if n < 20:
        return ones[n]

    if n < 100:
        t = (n // 10) * 10
        r = n % 10

        if r == 0:
            return tens[t]

        return tens[t] + " " + ones[r]




n = int(input())
arr = list(map(int,input().split()))
s = ""
for i in arr:
    s +=name_to_word(i)
print(s)

l =["a","e","i","o","u"]
c = 0
for i in s:
    if i in l:
        c+=1
print(c)
l = []
f=0
for i in range(n-1): 1 2 3 4 5
    if c - arr[i] in arr[i+1:n]:
        f+=1
print(name_to_word(f))

