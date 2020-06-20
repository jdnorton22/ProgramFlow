name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
    print("You are not allowed, {}".format(name))