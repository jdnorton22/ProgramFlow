activity=input("What would you like to do today? ")

# casefold checks case insensitivity
if "cinema" not in activity.casefold():
    print("But I want to go to cinema")
else:
    print("Me, too")