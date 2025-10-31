import random

#step 1: welcome screen
print("welcome to 'whose wallet?'")
print("you will give me a list of names, and i will pick a person to pay you're ready.")
list_of_names = input("Enter the names separated by comma.. ")

#step 2: create list of names and choose one person randomly
names = list_of_names.split(", ")
choose_person = random.choice(names)

#step 3: the final result
print(f"please ask, '{choose_person}' to take his wallet. dinner is o him")