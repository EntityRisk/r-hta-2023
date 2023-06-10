"""Some example unit tests."""

from aa_run import run_deterministic, run_psa


def test_run_deterministic():
    """Test that the deterministic model runs without error."""
    run_deterministic()


def test_run_psa():
    """Test that the probabilistic sensitivity analysis runs without error."""
    run_psa()


def test_dummy():
    """Dummy test that can be tweaked to show an example of a failing test."""
    assert 2 + 2 == 4
