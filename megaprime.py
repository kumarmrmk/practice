def find_factors(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc
n=int(input())
fc=find_factors(n)
if fc==2:
    print("prime")
    while n:
        r=n%10
        n=n//10
        fc=find_factors(r)
        if fc!=2:
            print("not mega prime")
            break
    else:
        print("mega prime")
else:
    print("not prime")
