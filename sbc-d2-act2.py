from random import randint


user_choice = int(input("Enter 0 (hayang) or 1 (kulob): "))


c1 = randint(0, 1)
c2 = randint(0, 1)


choices = ["hayang", "kulob"]
print(f"Me: {choices[user_choice]}")
print(f"C2: {choices[c1]}")
print(f"C3: {choices[c2]}")


if (user_choice == 0 and c1 == 1 and c2 == 1) or (user_choice == 1 and c1 == 0 and c2 == 0):
    print("You win!")
elif (user_choice == 1 and c1 == 0 and c2 == 1) or (user_choice == 0 and c1 == 1 and c2 == 0):
    print("C2 wins!")
elif (user_choice == 1 and c1 == 1 and c2 == 0) or (user_choice == 0 and c1 == 0 and c2 == 1):
    print("C2 wins!")
else:
    print("It's a draw!")
