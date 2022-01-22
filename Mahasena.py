n = int(input())
ar = list(map(int,input().split()))

odd = 0
even = 0
for i in range(len(ar)):
    if ar[i]%2==0:
        even+=1
    else:
        odd+=1

if even>odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
