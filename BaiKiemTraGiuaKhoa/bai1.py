x=int(input())
a=list(map(int,input().split(',')))
sum=0
for i in range(len(a)):
    sum+=a[i]*x**(x-i)
print(sum)