def prime(x):
    for i in range(2, x//2):
        if x % i == 0:
            return False
    return True


y =int(input('Enter number..'))

print(prime(y))
