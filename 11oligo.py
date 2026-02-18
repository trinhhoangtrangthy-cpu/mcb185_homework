def tm(A, C, G, T):
    if A+C+G+T <= 15:
        return (A+T)*2 + (C+G)*4
    else:
        return 64.9 + 41*(G+C - 16.4)/(A+C+G+T)
    
print(tm(5, 5, 5, 5))