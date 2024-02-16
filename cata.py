def calculate_year_of_birth(name, age):
    current_year = 2024

    birth_year = current_year - age + 100

    print(f"{name} will turn 100 years old in the year {birth_year}")

name1 = input("\nEnter name: ")
age1 = int(input("Enter age: "))

name2 = input("\nEnter name: ")
age2 = int(input("Enter age: "))

name3 = input("\nEnter name: ")
age3 = int(input("Enter age: "))

calculate_year_of_birth(name1, age1)
calculate_year_of_birth(name2, age2)
calculate_year_of_birth(name3, age3)

# Additional part
def calculate_year_of_birth_v2(name, age, target_age):
    current_year = 2024

    birth_year = current_year - age + target_age

    print(f"{name} will turn {target_age} years old in the year {birth_year}")

target_age = 100
calculate_year_of_birth_v2(name1, age1, target_age)
calculate_year_of_birth_v2(name2, age2, target_age)
calculate_year_of_birth_v2(name3, age3, target_age)
