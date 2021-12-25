n = int(input())
ar=[]
# cook your dish here
for i in range (n):
    st = input()
    ar.append(st)

for numbers in ar:
    ar2 = []
    summ=0
    for one in numbers:
        ar2.append(int(one))
    summ=summ+sum(ar2)
    print(summ)
