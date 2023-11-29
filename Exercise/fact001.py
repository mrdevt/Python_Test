def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
num=input('please input:')
m=int(num)
print(fact(m))