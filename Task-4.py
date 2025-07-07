import random

print(" Welcome to play Rock, Paper, Scissors!")
print(" Note the Instructions:")
print("-> Type 'rock', 'paper', or 'scissors' to play this game.")
print("-> Type 'exit' to quit the game.\n")

user_point = 0
computer_point = 0
while True:
    user_choice = input(" Choose your move (rock/paper/scissors): ").lower()

    if user_choice == "exit":
        print("\nThanks for playing!")
        print(f"Final Score - You: {user_point} | Computer: {computer_point}")
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print(" It's a tie!play again")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(" You win this round!")
        user_point += 1
    else:
        print(" You lose this round!")
        computer_point += 1
    print(f"Scoreboard - You: {user_point} | Computer: {computer_point}\n")
    play_again = input("Want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        print(f"Final Score - You: {user_point} | Computer: {computer_point}")
        break