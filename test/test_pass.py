from password import check_password
import pytest

def test_valid_password():
    assert check_password("jaiwinGjoe1!") == True

def test_short_password():
    with pytest.raises(ValueError):
        check_password("Short1!")
def test_no_uppercase():
    with pytest.raises(ValueError):
        check_password("nouppercase1!")

def test_no_lowercase():
    with pytest.raises(ValueError):
        check_password("NOLOWERCASE1!")

def test_no_special_character():
    with pytest.raises(ValueError):
        check_password("NoSpecialChar1")

@pytest.mark.parametrize("invalid_password", [
    12345678,  
    None,
    5.5,
    0,
    True,
    ["list"],
    {"dict": "value"},
    (1, 2, 3)
])

def test_non_string_and_others_password(invalid_password):
    with pytest.raises(ValueError):
        check_password(invalid_password)
