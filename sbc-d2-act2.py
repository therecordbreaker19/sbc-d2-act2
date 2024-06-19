from random import randint

# User input
user_choice = int(input("Enter 0 (hayang) or 1 (kulob): "))

# Computer choices
comp1 = randint(0, 1)
comp2 = randint(0, 1)

# Display choices
choices = ["hayang", "kulob"]
print(f"Me: {choices[user_choice]}")
print(f"C2: {choices[comp1]}")
print(f"C3: {choices[comp2]}")

# Determine winner
if (user_choice == 0 and comp1 == 1 and comp2 == 1) or (user_choice == 1 and comp1 == 0 and comp2 == 0):
    print("You win!")
elif (user_choice == 1 and comp1 == 0 and comp2 == 1) or (user_choice == 0 and comp1 == 1 and comp2 == 0):
    print("C2 wins!")
elif (user_choice == 1 and comp1 == 1 and comp2 == 0) or (user_choice == 0 and comp1 == 0 and comp2 == 1):
    print("C2 wins!")
else:
    print("It's a draw!")
