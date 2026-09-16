import math

n = 1150
s = 0.15
p = 0.95

x = n / (1 + s)

d = x / n

ans = math.ceil(math.log(1 - p) / math.log(x / n) - 1)
print(ans)