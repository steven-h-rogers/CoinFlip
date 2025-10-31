# import time
# import sys

# for i in range(101):
#     print(f"\rProgress: {i}%", end="")
#     sys.stdout.flush()
#     time.sleep(0.05)

# print()  # move to a new line after finishing

import time
import random
import os
import sys

# Simple function to clear the console
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Dummy game variables
probability = 0.2
consecutive_mult = 1.0
flip_speed = 1
coin_value = 1.0
money = 100.0
last_flips = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Main loop (simulate dynamic values)
for t in range(50):  # 50 updates
    # Dummy changes
    outcome = random.choice(["H", "T"])
    last_flips.pop(0)
    last_flips.append(outcome)
    probability = min(0.95, probability + random.uniform(-0.01, 0.02))
    consecutive_mult += random.uniform(-0.05, 0.1)
    flip_speed = max(1, flip_speed + random.choice([-1, 0, 1]))
    coin_value += random.uniform(-0.2, 0.5)
    money += random.uniform(-5, 10)

    # Move cursor to top-left (ANSI escape: "\033[H") and clear to end ("\033[J")
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

    # Display "controls" header
    print("Controls: [Space] Flip | [1] +Prob | [2] +Consec Mult | [3] +Speed | [4] +Coin Value | [Q] Quit\n")

    # Display dynamic stats
    print(f"Probability:        {probability:.2%}")
    print(f"Consecutive Mult:   {consecutive_mult:.2f}x")
    print(f"Flip Speed:         {flip_speed} flips/sec")
    print(f"Coin Value:         ${coin_value:.2f}")
    print(f"Player Money:       ${money:,.2f}")
    print()
    print("Upgrade Costs:  Prob $10  |  Mult $25  |  Speed $50  |  Value $40")
    print()
    print("Last 10 Flips:   " + " ".join(last_flips))
    print()
    print(f"Update #{t+1}/50 (press Ctrl+C to stop)")
    time.sleep(0.2)