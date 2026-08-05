import random

options = ["rock", "paper", "scissors"]

print("=== ✂️ Rock, Paper, Scissors ===")

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing! Goodbye 👋")
        break
        
    if user_choice not in options:
        print("❌ Invalid input. Please choose rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!\n")
    else:
        print("💻 Computer wins!\n")