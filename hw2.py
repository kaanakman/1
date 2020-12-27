first_name = input("Enter your first name: " )

last_name = input("Enter your last name: ")

age = int(input("Enter your age: "))   

birth_year = int(input("Enter your birth year: "))

user = [first_name, last_name, age, birth_year]

for i in user:
    print(i)

if age < 18:
    print("You can't go out, because it's too dangerous")
else:
    print("You can go out to the street")
