import pytest
import math
import src.game as game
from src.game import flip, consecutive_heads

def test_example():
    """An example test function."""
    assert True

"""test to verify that the flip method provides accurate results for 
given probability"""
def test_flip():
    probability = .20
    num_flips = 1_000_000
    results = [flip(probability) for _ in range(num_flips)]

    predicted_num_heads = probability*num_flips
    actual_num_heads = results.count('heads')
    print(f"Expected {predicted_num_heads}, got {actual_num_heads}")
    assert pytest.approx(predicted_num_heads, rel=1e-2) == actual_num_heads 




import math
import pytest
from src.game import flip

def test_consecutive_flip_probabilities():
    """Check consecutive heads runs: exact k=1..10 and an 11+ bucket."""
    p = 0.50
    n = 1_000_000

    # Run flips using your flip() (no seeding)
    results = [flip(p) for _ in range(n)]

    # Count runs of heads terminated by a tail
    # Keys 1..10 = exact run length; key 11 = 11+ bucket
    actual = {k: 0 for k in range(1, 12)}
    run = 0
    for outcome in results:
        if outcome == "heads":
            run += 1
        else:  # tails => close the run, if any
            if run:
                if run >= 11:
                    actual[11] += 1     # 11+ bucket
                else:
                    actual[run] += 1    # exact length
                run = 0

    # Expectations:
    # exact k: q_k = (1-p)^2 * p^k
    # 11+:     q_11plus = (1-p) * p^11  (sum_{k>=11} of (1-p)^2 * p^k)
    def prob_exact(k: int) -> float:
        return (1 - p) ** 2 * (p ** k)

    q_11plus = (1 - p) * (p ** 11)

    # Check k = 1..10
    for k in range(1, 11):
        qk = prob_exact(k)
        mu = n * qk
        sigma = math.sqrt(n * qk * (1 - qk))
        observed = actual[k]
        lower, upper = mu - 5 * sigma, mu + 5 * sigma
        print(f"{k} in a row: expected ≈ {mu:.2f} ± {5*sigma:.2f}, actual {observed}")
        assert lower <= observed <= upper, (
            f"Run length {k}: expected ≈ {mu:.2f} (±{5*sigma:.2f}), got {observed}"
        )

    # Check 11+ bucket
    mu = n * q_11plus
    sigma = math.sqrt(n * q_11plus * (1 - q_11plus))
    observed = actual[11]
    lower, upper = mu - 5 * sigma, mu + 5 * sigma
    print(f"11+ in a row: expected ≈ {mu:.2f} ± {5*sigma:.2f}, actual {observed}")
    assert lower <= observed <= upper, (
        f"Run length 11+: expected ≈ {mu:.2f} (±{5*sigma:.2f}), got {observed}"
    )