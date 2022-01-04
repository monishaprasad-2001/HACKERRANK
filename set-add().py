# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
sett = set()
for i in range(n):
    sett.add(input())
print(len(set(sett)))
