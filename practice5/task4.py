# Fourth task. Anastasia Zakharchuk it-32
a = 6
b = 10
surname = "Zakharchuk"
c = len(surname)

is_a_greater_than_b = a > b
is_a_less_than_b = a < b
is_c_greater_or_equal_b = c >= b
is_b_valid_month = 1 <= b <= 12
is_a_equal_to_c = a == c
is_b_not_equal_c = b != c

print(f"a = {a}, b = {b}, c = {c}")
print(f"is_a_greater_than_b: a > b -> {is_a_greater_than_b}, type = {type(is_a_greater_than_b)}")
print(f"is_a_less_than_b: a < b -> {is_a_less_than_b}, type = {type(is_a_less_than_b)}")
print(f"is_c_greater_or_equal_b: c >= b -> {is_c_greater_or_equal_b}, type = {type(is_c_greater_or_equal_b)}")
print(f"is_b_valid_month: 1 <= b <= 12 -> {is_b_valid_month}, type = {type(is_b_valid_month)}")
print(f"is_a_equal_to_c: a == c -> {is_a_equal_to_c}, type = {type(is_a_equal_to_c)}")
print(f"is_b_not_equal_c: b != c -> {is_b_not_equal_c}, type = {type(is_b_not_equal_c)}")
