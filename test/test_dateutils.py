from src.utils import dateutils

def test_get_current_date():
    assert dateutils.get_current_date() == "2025-07-25"

