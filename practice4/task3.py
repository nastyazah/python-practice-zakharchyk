NAME = "Anastasiia"
SURNAME = "Zaharchyk"

print(f"{NAME} {SURNAME}")

full_name = NAME + SURNAME
vowel_letters = "aeiouy"

vowels = 0
consonants = 0

for character in full_name:
    if character.lower() in vowel_letters:
        vowels += 1
    else:
        consonants += 1

print(f"Vowels: {vowels}, consonants: {consonants}")
print(f"Total letters: {vowels + consonants}")

assert vowels + consonants == len(full_name)