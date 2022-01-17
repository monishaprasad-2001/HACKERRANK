n,t = map(int,input().split())
width = list(map(int,input().split()))
for _ in range(t):
    i,j = map(int,input().split())
    print(min(width[i:j+1]))
