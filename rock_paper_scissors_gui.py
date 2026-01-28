"""
Rock Paper Scissors game with a Tkinter GUI
Player clicks buttons to make their choice and plays against the computer
"""
import random
import tkinter as tk
from tkinter import font

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x450")
        self.root.configure(bg='#2c3e50')
        
        self.player_score = 0
        self.computer_score = 0
        
        # Title
        title_font = font.Font(family='Arial', size=24, weight='bold')
        self.title_label = tk.Label(root, text="Rock Paper Scissors", 
                                     font=title_font, bg='#2c3e50', fg='#ecf0f1')
        self.title_label.pack(pady=20)
        
        # Score display
        score_font = font.Font(family='Arial', size=14)
        self.score_label = tk.Label(root, text=f"You: {self.player_score}  |  Computer: {self.computer_score}",
                                     font=score_font, bg='#2c3e50', fg='#ecf0f1')
        self.score_label.pack(pady=10)
        
        # Result display
        result_font = font.Font(family='Arial', size=16, weight='bold')
        self.result_label = tk.Label(root, text="Choose your weapon!", 
                                      font=result_font, bg='#2c3e50', fg='#f39c12', wraplength=400)
        self.result_label.pack(pady=20)
        
        # Choice display
        choice_font = font.Font(family='Arial', size=12)
        self.choice_label = tk.Label(root, text="", 
                                      font=choice_font, bg='#2c3e50', fg='#ecf0f1')
        self.choice_label.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(root, bg='#2c3e50')
        button_frame.pack(pady=20)
        
        button_font = font.Font(family='Arial', size=14, weight='bold')
        
        # Rock button
        self.rock_btn = tk.Button(button_frame, text="🪨 ROCK", 
                                   command=lambda: self.play('rock'),
                                   font=button_font, bg='#e74c3c', fg='white',
                                   width=10, height=2, cursor='hand2')
        self.rock_btn.grid(row=0, column=0, padx=10)
        
        # Paper button
        self.paper_btn = tk.Button(button_frame, text="📄 PAPER", 
                                    command=lambda: self.play('paper'),
                                    font=button_font, bg='#3498db', fg='white',
                                    width=10, height=2, cursor='hand2')
        self.paper_btn.grid(row=0, column=1, padx=10)
        
        # Scissors button
        self.scissors_btn = tk.Button(button_frame, text="✂️ SCISSORS", 
                                       command=lambda: self.play('scissors'),
                                       font=button_font, bg='#2ecc71', fg='white',
                                       width=10, height=2, cursor='hand2')
        self.scissors_btn.grid(row=0, column=2, padx=10)
        
        # Reset button
        self.reset_btn = tk.Button(root, text="Reset Score", 
                                    command=self.reset_score,
                                    font=font.Font(family='Arial', size=10),
                                    bg='#95a5a6', fg='white', cursor='hand2')
        self.reset_btn.pack(pady=10)
    
    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])
    
    def determine_winner(self, player, computer):
        if player == computer:
            return 'tie'
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            return 'player'
        else:
            return 'computer'
    
    def play(self, player_choice):
        computer_choice = self.get_computer_choice()
        
        # Display choices
        choice_emoji = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}

        # Validate player choice to avoid KeyError and invalid game state
        if player_choice not in choice_emoji:
            self.result_label.config(text="Invalid choice. Please select rock, paper, or scissors.", fg='#e74c3c')
            return
        self.choice_label.config(
            text=f"You chose: {choice_emoji[player_choice]} {player_choice.upper()}  |  "
                 f"Computer chose: {choice_emoji[computer_choice]} {computer_choice.upper()}"
        )
        
        # Determine winner
        winner = self.determine_winner(player_choice, computer_choice)
        
        if winner == 'player':
            self.player_score += 1
            self.result_label.config(text="🎉 You Win This Round! 🎉", fg='#2ecc71')
        elif winner == 'computer':
            self.computer_score += 1
            self.result_label.config(text="💔 Computer Wins This Round! 💔", fg='#e74c3c')
        else:
            self.result_label.config(text="🤝 It's a Tie! 🤝", fg='#f39c12')
        
        # Update score
        self.score_label.config(text=f"You: {self.player_score}  |  Computer: {self.computer_score}")
    
    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"You: {self.player_score}  |  Computer: {self.computer_score}")
        self.result_label.config(text="Choose your weapon!", fg='#f39c12')
        self.choice_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()
