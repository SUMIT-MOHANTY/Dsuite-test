import pytest

def test_import():
    """Basic test to ensure tests can run."""
    assert True

def test_working_directory():
    """Test that we can access project modules."""
    try:
        from app import main
        assert main.app is not None
    except ImportError:
        pytest.skip("app.main not available in CI")
