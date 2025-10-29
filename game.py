import time
import random
from random import random, randint
from collections import deque

money = 0.0
playing = True
won = False
consecutive_heads = 0

# Trees to manage each upgrade's state, cost, and effect
PROBABILITY_TREE = {
    "current_probability": 0,
    "probability_upgrades": deque(0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60),
    "probability_costs": deque(0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00)
}
CONSECUTIVE_HEADS_MULTIPLIER_TREE = {
    "current_multiplier": 0,
    "multiplier_upgrades": deque(1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00),
    "multiplier_costs": deque(0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00)
}
FLIP_SPEED_TREE = {
    "current_speed": 0,
    "speed_upgrades": deque(2.00, 1.75, 1.50, 1.25, 1.00, 0.90, 0.80, 0.70, 0.50),
    "speed_costs": deque(0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00)
}
COIN_VALUE_TREE = {
    "current_value": 0,
    "value_upgrades": deque(0.01, 0.05, 0.10, 0.25, 1.00, 3.00, 10.00, 100.00, 100.00),
    "speed_costs": deque(0.01, 0.05, 0.10, 0.25, 1.00, 6.25, 100.00, 1000.00, 10000.00)
}

FINAL_FLIP_TREE = {
    "heads" : .10,
    "landed on side" : .20,
    "eggbug" : .20,
    "flipped too high" : .20,
    "exploded" : .30
}

def winning_flip(probability_of_heads):
    result = flip(probability_of_heads)
    if result == 'heads':
        endings, weights = FINAL_FLIP_TREE.items()
        return random.choices(endings, weights)

def flip(probability_of_heads):
    num = randint(0,100)
    if num <= int(probability_of_heads*100):
        consecutive_heads += 1
        return "heads"
    else:
        consecutive_heads = 0
        return "tails"

while playing:
    if won == True:
        print(f"Congratulations! The probability of that happening was {(PROBABILITY_TREE['probability_upgrades'][PROBABILITY_TREE['current_probability_index']]^10)*100}%")
        key_in = input("type play to keep playing \n type quit to quit")
        if key_in.lower() == 'play':
            won = False
        elif key_in.lower() == 'quit':
            print("thanks for playing!")
        else:
            print("Invalid input")

    while won == False:
        game_input = input("press space to flip \n press 1 to buy decrease flip time \n press 2 to buy better head proability \n press 3 to buy better consecutive multiplier, \n press 4 to buy increased coin value")
        match game_input:
            case' ':
                if consecutive_heads <= 9:
                    flip(PROBABILITY_TREE["current_probability"])
                else: winning_flip()
            case'1':
                pass
            case'2':
                pass
            case'3':
                pass
            case'4':
                pass


    


