 #print multiplication table of 12 using recursion
def table(n,r):
    print(n*r)
    r=r+1
    if r<=10:
        table(n,r)
table(12,1)
