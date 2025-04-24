import socket

host = "192.168.254.106"  
port = 7777

def get_difficulty_choice():
    print("\nAvailable Difficulty Levels:")
    print("1) Easy (1-10)")
    print("2) Medium (1-50)")
    print("3) Hard (1-100)")
    while True:
        try:
            choice = int(input("Select difficulty (1-3): "))
            if 1 <= choice <= 3:
                return choice
            print("Please enter a number between 1 and 3")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    s = socket.socket()
    s.connect((host, port))
    
    
    difficulty_msg = s.recv(1024).decode().strip()
    print(difficulty_msg)
    
    
    difficulty = get_difficulty_choice()
    s.sendall(f"{difficulty}\n".encode())
    
    
    if difficulty == 1:
        low, high = 1, 10
    elif difficulty == 2:
        low, high = 1, 50
    else:
        low, high = 1, 100
    
    
    banner = s.recv(1024).decode().strip()
    print(banner)
    
    
    attempts = 0
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        
        print(f"Attempt #{attempts}: Guessing {guess}")
        s.sendall(f"{guess}\n".encode())
        
        response = s.recv(1024).decode().strip()
        print(f"Server response: {response}")
        
        if "CORRECT" in response:
            print(f"\nCorrect number found: {guess}")
            print(f"Total attempts: {attempts}")
            break
        elif "Higher" in response:
            low = guess + 1
        elif "Lower" in response:
            high = guess - 1
    
    s.close()

if __name__ == "__main__":
    print("=== Automated Guessing Bot ===")
    play_game()