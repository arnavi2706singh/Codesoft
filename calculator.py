import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.expression = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg='#f0f0f0')
        display_frame.pack(pady=10)
        
        # Result display
        self.display = tk.Entry(
            display_frame, 
            textvariable=self.result_var, 
            font=('Arial', 18, 'bold'),
            width=20,
            justify='right',
            state='readonly',
            bd=2,
            relief='solid'
        )
        self.display.pack(pady=5)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg='#f0f0f0')
        buttons_frame.pack(pady=10)
        
        # Button configuration
        button_config = {
            'font': ('Arial', 12, 'bold'),
            'width': 5,
            'height': 2,
            'relief': 'raised',
            'bd': 2
        }
        
        # First row - Clear and operations
        tk.Button(buttons_frame, text='C', bg='#ff6b6b', fg='white', 
                 command=self.clear, **button_config).grid(row=0, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text='⌫', bg='#ffa500', fg='white', 
                 command=self.backspace, **button_config).grid(row=0, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text='√', bg='#4ecdc4', fg='white', 
                 command=self.square_root, **button_config).grid(row=0, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text='÷', bg='#4ecdc4', fg='white', 
                 command=lambda: self.add_to_expression('/'), **button_config).grid(row=0, column=3, padx=2, pady=2)
        
        # Second row - Numbers 7, 8, 9, multiply
        tk.Button(buttons_frame, text='7', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('7'), **button_config).grid(row=1, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text='8', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('8'), **button_config).grid(row=1, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text='9', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('9'), **button_config).grid(row=1, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text='×', bg='#4ecdc4', fg='white', 
                 command=lambda: self.add_to_expression('*'), **button_config).grid(row=1, column=3, padx=2, pady=2)
        
        # Third row - Numbers 4, 5, 6, subtract
        tk.Button(buttons_frame, text='4', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('4'), **button_config).grid(row=2, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text='5', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('5'), **button_config).grid(row=2, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text='6', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('6'), **button_config).grid(row=2, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text='−', bg='#4ecdc4', fg='white', 
                 command=lambda: self.add_to_expression('-'), **button_config).grid(row=2, column=3, padx=2, pady=2)
        
        # Fourth row - Numbers 1, 2, 3, add
        tk.Button(buttons_frame, text='1', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('1'), **button_config).grid(row=3, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text='2', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('2'), **button_config).grid(row=3, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text='3', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('3'), **button_config).grid(row=3, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text='+', bg='#4ecdc4', fg='white', 
                 command=lambda: self.add_to_expression('+'), **button_config).grid(row=3, column=3, padx=2, pady=2)
        
        # Fifth row - Zero, decimal, equals
        tk.Button(buttons_frame, text='0', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('0'), **button_config).grid(row=4, column=0, columnspan=2, padx=2, pady=2, sticky='ew')
        tk.Button(buttons_frame, text='.', bg='#95a5a6', fg='white', 
                 command=lambda: self.add_to_expression('.'), **button_config).grid(row=4, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text='=', bg='#2ecc71', fg='white', 
                 command=self.calculate, **button_config).grid(row=4, column=3, padx=2, pady=2)
        
        # Configure grid weights for proper resizing
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
    
    def add_to_expression(self, value):
        """Add value to the current expression"""
        self.expression += str(value)
        self.result_var.set(self.expression)
    
    def clear(self):
        """Clear the display and reset expression"""
        self.expression = ""
        self.result_var.set("0")
    
    def backspace(self):
        """Remove the last character from expression"""
        if self.expression:
            self.expression = self.expression[:-1]
            if self.expression:
                self.result_var.set(self.expression)
            else:
                self.result_var.set("0")
    
    def square_root(self):
        """Calculate square root of current expression"""
        try:
            if self.expression:
                result = math.sqrt(float(self.expression))
                self.result_var.set(str(result))
                self.expression = str(result)
            else:
                messagebox.showerror("Error", "Please enter a number first")
        except ValueError:
            messagebox.showerror("Error", "Invalid input for square root")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
    
    def calculate(self):
        """Evaluate the expression and display result"""
        try:
            if self.expression:
                # Replace display symbols with actual operators
                expression = self.expression.replace('×', '*').replace('÷', '/').replace('−', '-')
                result = eval(expression)
                
                # Handle division by zero
                if result == float('inf') or result == float('-inf'):
                    messagebox.showerror("Error", "Division by zero!")
                    self.clear()
                    return
                
                # Format result
                if result == int(result):
                    result = int(result)
                
                self.result_var.set(str(result))
                self.expression = str(result)
            else:
                messagebox.showwarning("Warning", "Please enter an expression")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression")
            self.clear()
    
    def bind_keyboard(self):
        """Bind keyboard events for better user experience"""
        self.root.bind('<Return>', lambda event: self.calculate())
        self.root.bind('<KP_Enter>', lambda event: self.calculate())
        self.root.bind('<BackSpace>', lambda event: self.backspace())
        self.root.bind('<Escape>', lambda event: self.clear())
        
        # Bind number and operator keys
        for i in range(10):
            self.root.bind(str(i), lambda event, num=i: self.add_to_expression(str(num)))
        
        self.root.bind('+', lambda event: self.add_to_expression('+'))
        self.root.bind('-', lambda event: self.add_to_expression('-'))
        self.root.bind('*', lambda event: self.add_to_expression('*'))
        self.root.bind('/', lambda event: self.add_to_expression('/'))
        self.root.bind('.', lambda event: self.add_to_expression('.'))

def main():
    root = tk.Tk()
    calc = Calculator(root)
    calc.bind_keyboard()
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()