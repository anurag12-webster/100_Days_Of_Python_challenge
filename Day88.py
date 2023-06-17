def rotate(p):
 i = p.index(0)
 return p[i : ] + p[: i]

def swap(p, i1, i2):
 i1 %= len(p)
 i2 %= len(p)
 rv = p.copy()
 rv[i1], rv[i2] = rv[i2], rv[i1]
 return rv

def swaps(p):
    j = 1
    while j != len(p) and p[j] == j:
      j += 1
      if j == len(p):
        return [p]
      i1 = p.index(1)
      tries = [(j, p.index(j)), (0, i1 - 1), (0, i1), (0, -1), (0, -2), (i1, i1 - 1)]
      if len(p) > 2:
        tries.append((i1, p.index(2) - 1))
        return [rotate(swap(p, j, k)) for j, k in tries]

for _ in range(int(input())):
    input()
    v = [int(x) - 1 for x in input().split()]
    for x in min(r for q in swaps(rotate(v)) for r in swaps(q)):
       print(x + 1, end = ' ')
       print()