import random
import string

def generate_password(length):
    """
    Generate a random password with the specified length.
    Uses a combination of uppercase letters, lowercase letters, digits, and special characters.
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all character sets
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Ensure password has at least one character from each category (for passwords >= 4)
    if length >= 4:
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special_chars)
        ]
        
        # Fill the rest with random characters from all sets
        for _ in range(length - 4):
            password.append(random.choice(all_chars))
        
        # Shuffle the password to randomize character positions
        random.shuffle(password)
        return ''.join(password)
    else:
        # For shorter passwords, just use random characters
        return ''.join(random.choice(all_chars) for _ in range(length))

def main():
    """
    Main function to run the password generator application.
    """
    print("🔐 PASSWORD GENERATOR 🔐")
    print("=" * 30)
    
    while True:
        try:
            # User Input: Prompt for password length
            length = int(input("\nEnter the desired password length (minimum 1): "))
            
            if length < 1:
                print("❌ Password length must be at least 1. Please try again.")
                continue
                
            # Generate Password
            password = generate_password(length)
            
            # Display the Password
            print("\n" + "=" * 30)
            print("🎉 Generated Password:")
            print(f"📋 {password}")
            print("=" * 30)
            
            # Ask if user wants to generate another password
            another = input("\nWould you like to generate another password? (y/n): ").lower().strip()
            if another not in ['y', 'yes']:
                print("\n👋 Thank you for using the Password Generator!")
                break
                
        except ValueError:
            print("❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()