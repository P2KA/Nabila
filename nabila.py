import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def falling_love():
    hearts = ['❤️', '💖', '💘', '💝', '💕']
    width = 40  # Width of the screen
    height = 20  # Height of the screen

    while True:
        clear_screen()
        print("Happy Valentine's Day, Nabila Meilani Putri!")
        print("\n" + " " * (width // 2 - len("Happy Valentine's Day, Nabila Meilani Putri!") // 2))
        
        for _ in range(height):
            line = [' ' for _ in range(width)]
            for _ in range(random.randint(1, 5)):  # Random number of hearts
                pos = random.randint(0, width - 1)
                line[pos] = random.choice(hearts)
            print(''.join(line))
            time.sleep(0.2)  # Delay for falling effect

if __name__ == "__main__":
    falling_love()