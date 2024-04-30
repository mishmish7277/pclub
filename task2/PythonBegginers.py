def CheckPrime(num):
    for i in range(num - 1, 1,-1):
        if num % i == 0:
            return False
    return True


def FindPrimeNumbers(start,stop):
    for i in range(start,stop + 1):
        if (CheckPrime(i)):
            print(i)




