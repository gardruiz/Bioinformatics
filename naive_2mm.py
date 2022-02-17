def naive(p, t):
    occurrences = []
    mismatch = 0
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mismatch += 1
                if mismatch > 2:
                    match = False
                    break
        if match:
          occurrences.append(i)
    return occurrences
    print('match at postion:', occurrences, )

t = 'GGCGCGG'
p = 'GCCC'

print(naive(p,t, ))