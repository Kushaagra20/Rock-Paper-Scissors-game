import random
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("🎮 Rock Paper Scissors - Best of 3")
root.geometry("500x550")
root.configure(bg="#222831")  # Dark mode theme

# Score tracking
player_score = 0
computer_score = 0
ties = 0
round_count = 0

# Choices and Emojis
choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📜", "scissors": "✂"}

# Title
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Comic Sans MS", 20, "bold"), fg="#00FF00", bg="#222831")
title_label.pack(pady=10)

# Labels to show results
player_label = tk.Label(root, text="Your Choice: ❓", font=("Arial", 14), fg="white", bg="#222831")
player_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer's Choice: ❓", font=("Arial", 14), fg="white", bg="#222831")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="yellow", bg="#222831")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0 | Ties: 0", font=("Arial", 14), fg="cyan", bg="#222831")
score_label.pack(pady=10)

# Final Result Label (Initially Hidden)
final_result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), fg="red", bg="#222831")
final_result_label.pack(pady=10)

# Function to create a flashing effect
def flash_result(color):
    result_label.config(fg=color)
    root.after(200, lambda: result_label.config(fg="yellow"))

# Function to play a round
def play_round(player_choice):
    global player_score, computer_score, ties, round_count

    # Hide final result label when a new round starts
    final_result_label.config(text="")

    # Computer makes a choice
    computer_choice = random.choice(choices)

    # Update labels with emojis
    player_label.config(text=f"Your Choice: {emojis[player_choice]}")
    computer_label.config(text=f"Computer's Choice: {emojis[computer_choice]}")

    # Determine winner
    if player_choice == computer_choice:
        result = "It's a Tie! 🤝"
        ties += 1
        flash_result("orange")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You Win! 🎉"
        player_score += 1
        flash_result("green")
    else:
        result = "You Lose! 😢"
        computer_score += 1
        flash_result("red")

    # Update result and score labels
    result_label.config(text=result)
    round_count += 1
    score_label.config(text=f"Score - You: {player_score} | Computer: {computer_score} | Ties: {ties}")

    # Check if 3 rounds are done
    if round_count == 3:
        show_final_result()

# Function to show the final result in the game window
def show_final_result():
    if player_score > computer_score:
        final_result_text = "🎉 You won the game!"
        final_result_label.config(fg="lime")
    elif player_score < computer_score:
        final_result_text = "😢 You lost! Try again!"
        final_result_label.config(fg="red")
    else:
        final_result_text = "🤝 It's a tie!"
        final_result_label.config(fg="orange")

    final_result_text += f"\nFinal Score:\nYou: {player_score} | Computer: {computer_score} | Ties: {ties}"
    final_result_label.config(text=final_result_text)

    # Show restart button
    restart_button.pack(pady=10)

# Function to restart the game
def restart_game():
    global player_score, computer_score, ties, round_count
    player_score = 0
    computer_score = 0
    ties = 0
    round_count = 0

    # Reset labels
    player_label.config(text="Your Choice: ❓")
    computer_label.config(text="Computer's Choice: ❓")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0 | Ties: 0")
    final_result_label.config(text="")

    # Hide restart button
    restart_button.pack_forget()

# Buttons for user choices
btn_rock = tk.Button(root, text="🪨 Rock", font=("Arial", 12, "bold"), command=lambda: play_round("rock"), bg="gray", fg="white")
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="📜 Paper", font=("Arial", 12, "bold"), command=lambda: play_round("paper"), bg="blue", fg="white")
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="✂ Scissors", font=("Arial", 12, "bold"), command=lambda: play_round("scissors"), bg="red", fg="white")
btn_scissors.pack(pady=5)

# Restart Button (Initially Hidden)
restart_button = tk.Button(root, text="🔄 Restart Game", font=("Arial", 12, "bold"), command=restart_game, bg="yellow", fg="black")

# Run the Tkinter event loop
root.mainloop()
