import pytest
from src.game import flip

def test_example():
    """An example test function."""
    assert True


def test_flip():
    probability = .20
    num_flips = 1_000_000
    results = [flip(probability) for _ in range(num_flips)]

    predicted_num_heads = probability*num_flips
    actual_num_heads = results.count('heads')

    assert pytest.approx(predicted_num_heads) == actual_num_heads
