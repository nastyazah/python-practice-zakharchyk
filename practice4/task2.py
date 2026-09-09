NAME = "Anastasiia"
SURNAME = "Zaharchyk"
GROUP = "It-32"

print(f"{NAME} {SURNAME}, {GROUP}")

number = int(input("Enter an integer: "))

if number <= 0:
    print("Error: please enter a positive integer")
else:
    digit_count = 0
    digit_sum = 0
    max_digit = -1
    min_digit = 10
    reversed_number = 0

    while number > 0:
        digit = number % 10
        digit_count += 1
        digit_sum += digit
        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
        reversed_number = reversed_number * 10 + digit
        number //= 10

    print(f"Digits: {digit_count}")
    print(f"Sum of digits: {digit_sum}")
    print(f"Max digit: {max_digit}, min digit: {min_digit}")
    print(f"Reversed: {reversed_number}")