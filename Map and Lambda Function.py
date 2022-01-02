cube = lambda x:x**3

 # complete the lambda function 

def fibonacci(n):
    a,b = 0,1
    #for loop to find the fibonacci series upto n terms:
    for i in range(n):
        yield a
        a,b = b,a+b
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
