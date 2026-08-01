def isPrime(x):
    if x <= 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

numsList = input("Enter Multiple Number: ")
numsStr = numsList.split()
nums = [int(n) for n in numsStr]

for y in nums:
    if isPrime(y):
        print(y, "is a Prime")
    else:
        print(y,"Is not a Prime")

for z in range (1,101):
    if isPrime(z):
        print(z, "is a Prime")
    else:
        print(z,"Is not a Prime")
    