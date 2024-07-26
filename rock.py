user_score = 0
computer_score = 0
def game():
    global user_score, computer_score
    import random
    print("Rock,Paper,Scissor")
    user = input("ENTER YOUR CHOICE : ").lower()
    l = ["rock", "paper", "scissor"]
    computer = random.choice(l)
    print(f"COMPUTER CHOICE: {computer}")

    if computer == user:
        print("IT'S A TIE")
    elif computer == "paper" and user == "rock":
        print("YOU LOST")
        computer_score += 1
    elif computer == "scissor" and user == "rock":
        print("YOU WIN")
        user_score += 1
    elif computer == "rock" and user == "paper":
        print("YOU WIN")
        user_score += 1
    elif computer == "scissor" and user == "paper":
        print("YOU LOST")
        computer_score += 1
    elif computer == "rock" and user == "scissor":
        print("YOU LOST")
        computer_score += 1
    else:
        print("Invalid choice. You lose this round.")
        computer_score += 1

    print(f"user score = {user_score}")
    print(f"computer score = {computer_score}")

while True:
    game()
    choice = input("Do you want to play again (y/n): ").lower()
    if choice != 'y':
        print("Thank you for playing!")
        break