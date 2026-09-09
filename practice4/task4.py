NAME = "Anastasiia"
SURNAME = "Zaharchyk"
GROUP = "It-32"

print(f"{NAME} {SURNAME}, {GROUP}")

attempts = 0

while True:
    value = input("Enter your score (0-100): ")
    attempts += 1

    if not value.lstrip("-").isdigit():
        print("Error: please enter a whole number")
        continue

    score = int(value)

    if score < 0:
        print("Score cannot be negative")
        continue
    if score > 100:
        print("Score is too big, maximum is 100")
        continue

    break

print(f"Accepted after {attempts} attempts")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")