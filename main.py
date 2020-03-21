#!/usr/bin/pyhon


def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False

    sqr = int(num**0.5) + 1
    for i in range(3, sqr, 2):
        if num % i == 0:
            return False
    return True


def filterFun(num):
    if(isPrime(num)==False):
        return False
    return True


def mapFun(num):
    if(isPrime(num)):
        return num
    return None


def quest5():
    print("\n\nQUEST 5\n")
    lis = [3, 10, 0, 2, 1, 2, 5, 7, 12]
    print("FILTER")
    filtered = filter(filterFun, lis)

    for i in filtered:
        print(i, end=", ")

    print("\nLIST COMPREHENSIONS")
    print([num for num in lis if isPrime(num)])


def callFunctionCounter(obj):
    def inner(*args, **kwargs):
        inner.calls += 1
        return obj(*args, **kwargs)

    inner.calls = 0
    return inner


@callFunctionCounter
def fib(num):
    if(num <= 1):
        return num
    return fib(num-1) + fib(num-2)


def quest7(obj):
    def inner(*args, **kwargs):
        print("\n\nQUEST 7")
        print("FUNCTION NAME: " + obj.__name__ + " , function args: " + str(args));
        return obj(*args, **kwargs)
    return inner


def quest6(num):
    print("\n\nQUEST 6")
    print("Fib of " + str(num) + "="+ str(fib(num)))


def quest8():
    print("\n\nQUEST 8")
    print("Function fib() was call:" + str(fib.calls) + " times")


@quest7
def quest9(dir):
    print("\n\nQUEST 9")
    file = open(dir, "r")
    print("Words in file: " + str(len( file.read().split(" ") )))



def main():
    quest5()
    quest6(7)
    quest8()
    quest9("test.txt")

if __name__ == '__main__':
    main()
