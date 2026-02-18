# Trees to manage each upgrade's state, cost, and effect
PROBABILITY_TREE = {
    "current_probability": 0.50,
    "probability_upgrades": [0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60],
    "probability_costs": [0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00]
}
CONSECUTIVE_HEADS_MULTIPLIER_TREE = {
    "current_multiplier": 2,
    "multiplier_upgrades": [1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00],
    "multiplier_costs": [0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00]
}
FLIP_SPEED_TREE = {
    "current_speed": 2.00,
    "speed_upgrades": [2.00, 1.75, 1.50, 1.25, 1.00, 0.90, 0.80, 0.70, 0.50],
    "speed_costs": [0.01, 0.05, 0.10, 0.25, 1.00, 10.00, 100.00, 1000.00, 10000.00]
}
COIN_VALUE_TREE = {
    "current_value": 0.01,
    "value_upgrades": [0.01, 0.05, 0.10, 0.25, 1.00, 3.00, 10.00, 100.00, 100.00],
    "value_costs": [0.01, 0.05, 0.10, 0.25, 1.00, 6.25, 100.00, 1000.00, 10000.00]
}

FINAL_FLIP_TREE = {
    "heads" : .10,
    "landed on side" : .20,
    "eggbug" : .20,
    "flipped too high" : .20,
    "exploded" : .30
}