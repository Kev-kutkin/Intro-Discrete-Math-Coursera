
def squares(n,m):
    area = m * n
    while n>0 and m > 0:
        if n>=m:
            n = n%m
        else:
            m = m %n
    return int(area/(max(m,n))**2)
