n = int(input())
k = int(input())

powk = k
while n > powk:
    powk *= k

x = n - (powk // k)
print(1 if n == powk else k * x + 1)