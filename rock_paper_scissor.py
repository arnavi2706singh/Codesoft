import tkinter as tk
from tkinter import messagebox, ttk
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Rock-Paper-Scissors Game")
        self.root.geometry("600x700")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(False, False)
        
        # Game variables
        self.user_score = 0
        self.computer_score = 0
        self.total_games = 0
        
        # Choice emojis
        self.choice_emojis = {
            'rock': '🪨',
            'paper': '📄',
            'scissors': '✂️'
        }
        
        self.setup_gui()
    
    def setup_gui(self):
        """Setup the GUI elements"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🎮 Rock-Paper-Scissors 🎮",
            font=('Arial', 24, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack()
        
        # Score display
        self.score_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=2)
        self.score_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(
            self.score_frame,
            text="📊 SCOREBOARD",
            font=('Arial', 16, 'bold'),
            fg='#ecf0f1',
            bg='#34495e'
        ).pack(pady=5)
        
        score_info_frame = tk.Frame(self.score_frame, bg='#34495e')
        score_info_frame.pack(pady=5)
        
        self.user_score_label = tk.Label(
            score_info_frame,
            text=f"You: {self.user_score}",
            font=('Arial', 14, 'bold'),
            fg='#2ecc71',
            bg='#34495e'
        )
        self.user_score_label.grid(row=0, column=0, padx=20)
        
        tk.Label(
            score_info_frame,
            text="|",
            font=('Arial', 14, 'bold'),
            fg='#ecf0f1',
            bg='#34495e'
        ).grid(row=0, column=1, padx=10)
        
        self.computer_score_label = tk.Label(
            score_info_frame,
            text=f"Computer: {self.computer_score}",
            font=('Arial', 14, 'bold'),
            fg='#e74c3c',
            bg='#34495e'
        )
        self.computer_score_label.grid(row=0, column=2, padx=20)
        
        # Instructions
        instruction_label = tk.Label(
            self.root,
            text="Choose your move:",
            font=('Arial', 18, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        instruction_label.pack(pady=20)
        
        # Choice buttons
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=20)
        
        # Create choice buttons
        button_style = {
            'font': ('Arial', 16, 'bold'),
            'width': 12,
            'height': 3,
            'relief': 'raised',
            'bd': 3,
            'cursor': 'hand2'
        }
        
        self.rock_button = tk.Button(
            button_frame,
            text="🪨\nRock",
            bg='#95a5a6',
            fg='#2c3e50',
            activebackground='#7f8c8d',
            command=lambda: self.play_round('rock'),
            **button_style
        )
        self.rock_button.grid(row=0, column=0, padx=10)
        
        self.paper_button = tk.Button(
            button_frame,
            text="📄\nPaper",
            bg='#f39c12',
            fg='#2c3e50',
            activebackground='#e67e22',
            command=lambda: self.play_round('paper'),
            **button_style
        )
        self.paper_button.grid(row=0, column=1, padx=10)
        
        self.scissors_button = tk.Button(
            button_frame,
            text="✂️\nScissors",
            bg='#3498db',
            fg='#2c3e50',
            activebackground='#2980b9',
            command=lambda: self.play_round('scissors'),
            **button_style
        )
        self.scissors_button.grid(row=0, column=2, padx=10)
        
        # Game result display area
        self.result_frame = tk.Frame(self.root, bg='#34495e', relief='sunken', bd=2)
        self.result_frame.pack(pady=30, padx=20, fill='both', expand=True)
        
        tk.Label(
            self.result_frame,
            text="🎯 GAME RESULTS",
            font=('Arial', 16, 'bold'),
            fg='#ecf0f1',
            bg='#34495e'
        ).pack(pady=10)
        
        # Choices display
        choices_frame = tk.Frame(self.result_frame, bg='#34495e')
        choices_frame.pack(pady=10)
        
        self.user_choice_label = tk.Label(
            choices_frame,
            text="Your Choice:\n-",
            font=('Arial', 14),
            fg='#ecf0f1',
            bg='#34495e',
            width=15
        )
        self.user_choice_label.grid(row=0, column=0, padx=20)
        
        tk.Label(
            choices_frame,
            text="VS",
            font=('Arial', 14, 'bold'),
            fg='#e74c3c',
            bg='#34495e'
        ).grid(row=0, column=1, padx=10)
        
        self.computer_choice_label = tk.Label(
            choices_frame,
            text="Computer Choice:\n-",
            font=('Arial', 14),
            fg='#ecf0f1',
            bg='#34495e',
            width=15
        )
        self.computer_choice_label.grid(row=0, column=2, padx=20)
        
        # Result message
        self.result_label = tk.Label(
            self.result_frame,
            text="Make your first move!",
            font=('Arial', 16, 'bold'),
            fg='#f1c40f',
            bg='#34495e',
            wraplength=400
        )
        self.result_label.pack(pady=20)
        
        # Bottom buttons
        bottom_frame = tk.Frame(self.root, bg='#2c3e50')
        bottom_frame.pack(pady=20)
        
        reset_button = tk.Button(
            bottom_frame,
            text="🔄 Reset Score",
            font=('Arial', 12, 'bold'),
            bg='#e67e22',
            fg='white',
            activebackground='#d35400',
            relief='raised',
            bd=2,
            cursor='hand2',
            command=self.reset_score
        )
        reset_button.grid(row=0, column=0, padx=10)
        
        stats_button = tk.Button(
            bottom_frame,
            text="📊 Show Stats",
            font=('Arial', 12, 'bold'),
            bg='#9b59b6',
            fg='white',
            activebackground='#8e44ad',
            relief='raised',
            bd=2,
            cursor='hand2',
            command=self.show_stats
        )
        stats_button.grid(row=0, column=1, padx=10)
        
        quit_button = tk.Button(
            bottom_frame,
            text="❌ Quit Game",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            relief='raised',
            bd=2,
            cursor='hand2',
            command=self.quit_game
        )
        quit_button.grid(row=0, column=2, padx=10)
    
    def play_round(self, user_choice):
        """Play a single round of the game"""
        # Generate computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # Update choice displays
        self.user_choice_label.config(
            text=f"Your Choice:\n{self.choice_emojis[user_choice]} {user_choice.capitalize()}"
        )
        self.computer_choice_label.config(
            text=f"Computer Choice:\n{self.choice_emojis[computer_choice]} {computer_choice.capitalize()}"
        )
        
        # Determine winner
        winner = self.determine_winner(user_choice, computer_choice)
        
        # Update scores and display result
        if winner == 'user':
            self.user_score += 1
            result_text = "🎉 You Win!"
            result_color = '#2ecc71'
            explanation = self.get_win_explanation(user_choice, computer_choice)
        elif winner == 'computer':
            self.computer_score += 1
            result_text = "🤖 Computer Wins!"
            result_color = '#e74c3c'
            explanation = self.get_win_explanation(computer_choice, user_choice)
        else:
            result_text = "🤝 It's a Tie!"
            result_color = '#f39c12'
            explanation = "Same choice!"
        
        self.total_games += 1
        
        # Update result display
        self.result_label.config(
            text=f"{result_text}\n{explanation}",
            fg=result_color
        )
        
        # Update scoreboard
        self.update_scoreboard()
        
        # Add a small animation effect
        self.animate_result()
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of the round"""
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'
    
    def get_win_explanation(self, winning_choice, losing_choice):
        """Get explanation for why one choice beats another"""
        explanations = {
            ('rock', 'scissors'): 'Rock crushes Scissors!',
            ('scissors', 'paper'): 'Scissors cut Paper!',
            ('paper', 'rock'): 'Paper covers Rock!'
        }
        return explanations.get((winning_choice, losing_choice), '')
    
    def update_scoreboard(self):
        """Update the scoreboard display"""
        self.user_score_label.config(text=f"You: {self.user_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
    
    def animate_result(self):
        """Simple animation effect for result display"""
        original_font = self.result_label.cget('font')
        self.result_label.config(font=('Arial', 18, 'bold'))
        self.root.after(500, lambda: self.result_label.config(font=original_font))
    
    def reset_score(self):
        """Reset the game scores"""
        if messagebox.askyesno("Reset Score", "Are you sure you want to reset the score?"):
            self.user_score = 0
            self.computer_score = 0
            self.total_games = 0
            self.update_scoreboard()
            
            # Reset displays
            self.user_choice_label.config(text="Your Choice:\n-")
            self.computer_choice_label.config(text="Computer Choice:\n-")
            self.result_label.config(
                text="Score reset! Make your move!",
                fg='#f1c40f'
            )
    
    def show_stats(self):
        """Show detailed game statistics"""
        if self.total_games == 0:
            messagebox.showinfo("Statistics", "No games played yet!")
            return
        
        win_rate = (self.user_score / self.total_games) * 100
        ties = self.total_games - self.user_score - self.computer_score
        
        stats_message = f"""
🏆 GAME STATISTICS 🏆

Total Rounds: {self.total_games}
Your Wins: {self.user_score}
Computer Wins: {self.computer_score}
Ties: {ties}

Your Win Rate: {win_rate:.1f}%

Overall Result:
"""
        
        if self.user_score > self.computer_score:
            stats_message += "🎉 You're winning overall!"
        elif self.computer_score > self.user_score:
            stats_message += "🤖 Computer is winning overall!"
        else:
            stats_message += "🤝 It's tied overall!"
        
        messagebox.showinfo("Game Statistics", stats_message)
    
    def quit_game(self):
        """Quit the game with confirmation"""
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
            if self.total_games > 0:
                self.show_stats()
            self.root.quit()

def main():
    """Main function to run the GUI game"""
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    
    # Center the window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()