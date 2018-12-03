def squareFunction(n):
    multiplication(n, square)

def doubleFunction(n):
    multiplication(n, double)

def cubeFunction(n):
    multiplication(n, cube)

def square(n):
    return n*n

def double(n):
    return 2*n

def cube(n):
    return n**3

def multiplication(n, term):
    i = 1
    while n >= i:
        print(term(i))
        i+=1

if __name__ == '__main__':
    multiplication(3, square)
    print()
    multiplication(4, cube)
    print()
    cubeFunction(6)