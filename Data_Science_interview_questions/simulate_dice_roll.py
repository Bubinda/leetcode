import random

def simulate_game():
    amy_wins = False
    brad_wins = False

    while not amy_wins and not brad_wins:
        amy_roll = random.randint(1, 6)
        brad_roll = random.randint(1, 6)

        if amy_roll == 6:
            amy_wins = True
        elif brad_roll == 6:
            brad_wins = True

    return amy_wins

def calculate_probability(num_simulations):
    amy_wins_count = 0

    for _ in range(num_simulations):
        if simulate_game():
            amy_wins_count += 1

    probability_amy_wins = amy_wins_count / num_simulations
    return probability_amy_wins

# Example usage:
num_simulations = 100000
probability_amy_wins = calculate_probability(num_simulations)

print(f"The probability that Amy wins first is approximately: {probability_amy_wins:.4f}")
