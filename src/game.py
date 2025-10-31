import time
import random
from random import randint
from collections import deque

money = 0.0
playing = True
won = False
consecutive_heads = 0

# Trees to manage each upgrade's state, cost, and effect
PROBABILITY_TREE = {
    "current_probability": 0.20,
    "probability_upgrades": deque([0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60]),
    "probability_costs": deque([0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00])
}
CONSECUTIVE_HEADS_MULTIPLIER_TREE = {
    "current_multiplier": 1,
    "multiplier_upgrades": deque([1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00]),
    "multiplier_costs": deque([0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00])
}
FLIP_SPEED_TREE = {
    "current_speed": 2.00,
    "speed_upgrades": deque([2.00, 1.75, 1.50, 1.25, 1.00, 0.90, 0.80, 0.70, 0.50]),
    "speed_costs": deque([0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00])
}
COIN_VALUE_TREE = {
    "current_value": 0.01,
    "value_upgrades": deque([0.01, 0.05, 0.10, 0.25, 1.00, 3.00, 10.00, 100.00, 100.00]),
    "value_costs": deque([0.01, 0.05, 0.10, 0.25, 1.00, 6.25, 100.00, 1000.00, 10000.00])
}

FINAL_FLIP_TREE = {
    "heads" : .10,
    "landed on side" : .20,
    "eggbug" : .20,
    "flipped too high" : .20,
    "exploded" : .30
}

def upgrade_probability():
    global money
    if money <= PROBABILITY_TREE["probability_costs"][0]:
        money -= PROBABILITY_TREE["probability_costs"].popleft()
        PROBABILITY_TREE["current_probability"] = PROBABILITY_TREE['probability_upgrades'].popleft()

def upgrade_consecutive_mult():
    global money
    if money <= CONSECUTIVE_HEADS_MULTIPLIER_TREE["multiplier_costs"][0]:
        money -= CONSECUTIVE_HEADS_MULTIPLIER_TREE["multiplier_costs"].popleft()
        CONSECUTIVE_HEADS_MULTIPLIER_TREE["current_multiplier"] = CONSECUTIVE_HEADS_MULTIPLIER_TREE["multiplier_upgrades"].popleft()

def upgrade_flip_speed():
    global money
    if money <= FLIP_SPEED_TREE["speed_costs"][0]:
        money -= FLIP_SPEED_TREE["speed_costs"].popleft()
        FLIP_SPEED_TREE["current_speed"] = FLIP_SPEED_TREE["speed_upgrades"].popleft()

def upgrade_coin_value():
    global money
    if money <= COIN_VALUE_TREE["value_costs"][0]:
        money -= COIN_VALUE_TREE["value_costs"].popleft()
        COIN_VALUE_TREE["current_value"] = COIN_VALUE_TREE["value_upgrades"].popleft()


def winning_flip(probability_of_heads):
    result = flip(probability_of_heads)
    if result == 'heads':
        endings, weights = list(FINAL_FLIP_TREE.keys()), list(FINAL_FLIP_TREE.values())
        ending = random.choices(endings, weights)[0]
        print(ending)
        return ending
    else:
        print(result)

def flip(probability_of_heads):
    global consecutive_heads

    distribution = {
        "heads": probability_of_heads,
        "tails": 1-probability_of_heads
    }

    outcomes, weights = list(distribution.keys()), list(distribution.values())

    result = random.choices(outcomes, weights)[0]
    print(result)
    if result == "heads":
        consecutive_heads += 1
    else:
        consecutive_heads = 0
    return result

def game_loop():
    global won, playing, money, consecutive_heads
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
                    else:
                        outcome = winning_flip()
                        if outcome != 'tails':
                            won == True
                case'1':
                    pass
                case'2':
                    pass
                case'3':
                    pass
                case'4':
                    pass


game_loop()

    


