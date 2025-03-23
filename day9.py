def is_prime(n):
    if n <2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True 
def separate_primes(list):
    primes=[]
    non_primes=[]

    for num in list:
        if is_prime(num):
            primes.append(num)
        else:
            non_primes.append(num)
    return primes,non_primes
numbers=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes, non_primes =separate_primes(numbers)
print("prime numbers:",primes)
print("non_prime numbers:",non_primes)
