def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_till_n(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Input from the user
n = int(input("Enter a number: "))
print(f"Prime numbers up to {n}: {prime_numbers_till_n(n)}")
