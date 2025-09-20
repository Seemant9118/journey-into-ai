# snake, water, gun game
import random
print("Welcome to Snake, Water, Gun game!")
print("Rules:")
print("1. Snake drinks the water, so snake wins.")
print("2. Water douses the gun, so water wins.")
print("3. Gun shoots the snake, so gun wins.")
print("4. If both players choose the same, it's a tie.")

choices = ['snake', 'water', 'gun']

user_score = 0
computer_score = 0

rounds = int(input("Enter the number of rounds you want to play: "))

for round in range(rounds):
    user_choice = input("Enter your choice (snake, water, gun): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please choose snake, water, or gun.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print("Final Score:")
print(f"You: {user_score}, Computer: {computer_score}")
if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("Computer won the game! Better luck next time.")
else:
    print("The game is a tie!")