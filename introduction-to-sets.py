def average(array):
    return "{:.3f}".format(sum(set(array))/len(set(array)))

    # your code goes here

    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
