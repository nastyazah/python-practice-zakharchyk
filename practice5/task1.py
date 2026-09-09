# First task. Anastasia Zakharchuk it-32
birth_day = 6
height_m = 1.60
group_name = "IT-32"
has_scholarship = True

print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"height_m = {height_m}, type = {type(height_m)}")
print(f"group_name = {group_name}, type = {type(group_name)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")

birth_day = "sixth of October"
has_scholarship = 1.0

print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")

try:
    birth_day_plus_one = birth_day + 1
    print(f"birth_day_plus_one = {birth_day_plus_one}")
except TypeError as error:
    print(f"TypeError: {error}")
