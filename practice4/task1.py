NAME = "Anastasiia"
SURNAME = "Zakharchyk"
GROUP = "It-32"
D = 6
C = len(SURNAME)

print(f"{NAME} {SURNAME}, {GROUP}")

count = 0
total = 0
product = 1
even = 0
odd = 0

print(f"Numbers from {D} to 31: ", end="")
for number in range(D, 32):
    print(number, end=" ")
    count += 1
    total += number
    product *= number
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print()

average = total / count
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even}, odd: {odd}")

print()
print("# while version")

number = D
count_w = 0
total_w = 0
product_w = 1
even_w = 0
odd_w = 0

print(f"Numbers from {D} to 31: ", end="")
while number <= 31:
    print(number, end=" ")
    count_w += 1
    total_w += number
    product_w *= number
    if number % 2 == 0:
        even_w += 1
    else:
        odd_w += 1
    number += 1
print()

average_w = total_w / count_w
print(f"Count: {count_w}")
print(f"Sum: {total_w}")
print(f"Product: {product_w}")
print(f"Average: {average_w:.2f}")
print(f"Even: {even_w}, odd: {odd_w}")

same_result = (count == count_w and total == total_w and product == product_w
               and average == average_w and even == even_w and odd == odd_w)
print(f"Both versions match: {same_result}")

print("Countdown: ", end="")
for i in range(C, 0, -1):
    print(i, end=" ")
print()