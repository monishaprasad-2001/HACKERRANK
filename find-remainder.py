n = int(input())
ar1 = []
result = []
for i in range(n):
    ar1 = list(map(int,input().split()))
    result.append(int(ar1[0])%int(ar1[1]))
for j in range(len(result)):
    print(result[i])
