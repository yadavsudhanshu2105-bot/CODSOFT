import random

choices = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSOR =====")

while True:

    user = input("\nChoose Rock, Paper or Scissor: ").lower()

    if user not in choices:
        print("Invalid Input!")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (
        (user == "rock" and computer == "scissor")
        or (user == "paper" and computer == "rock")
        or (user == "scissor" and computer == "paper")
    ):
        print("Congratulations!You Win!")
        user_score += 1

    else:
        print("Computer Wins!Try again")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)
print("Thank You For Playing!")
