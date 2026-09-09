NAME = "Anastasiia"
SURNAME = "Zaharchyk"
GROUP = "It-32"
D = 6
C = len(SURNAME)

print(f"{NAME} {SURNAME}, {GROUP}")

n = D * C
print(f"n = {D} * {C} = {n}")
divisors = []
divisors_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        divisors_sum += i

print("Divisors: " + " ".join(str(d) for d in divisors))
print(f"Divisors count: {len(divisors)}, sum: {divisors_sum}")

for divisor in range(2, n):
    if n % divisor == 0:
        print(f"{n} is not prime: divisible by {divisor}")
        break
else:
    print(f"{n} is prime")

primes = []
for candidate in range(2, n + 1):
    for divisor in range(2, candidate):
        if candidate % divisor == 0:
            break
    else:
        primes.append(candidate)

print(f"Primes up to {n}: " + " ".join(str(p) for p in primes))
print(f"Primes count: {len(primes)}")