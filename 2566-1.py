l = sum([list(map(int, input().split())) for _ in range(9)],[])
m= max(l)
mi = l.index(m)
print(m)
print(mi// 9 + 1, mi% 9 + 1)