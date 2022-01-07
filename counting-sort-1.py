def countingSort(arr):
    
    tot = [0]*100

    for j in range(0,len(arr)):
        temp = arr[j]
        tot[temp] += 1
    return(tot)    

        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
