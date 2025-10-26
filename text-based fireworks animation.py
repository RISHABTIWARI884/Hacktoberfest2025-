import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fireworks(rows=20, columns=40, bursts=5):
    for _ in range(bursts):
        # Random explosion center
        x = random.randint(5, columns - 5)
        y = random.randint(5, rows - 5)

        for radius in range(1, 6):
            clear()
            for i in range(rows):
                line = ""
                for j in range(columns):
                    # Draw explosion pattern
                    if abs(i - y) + abs(j - x) == radius:
                        line += "*"
                    else:
                        line += " "
                print(line)
            time.sleep(0.2)

if __name__ == "__main__":
    fireworks()
