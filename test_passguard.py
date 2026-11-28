
from passguard import (
    calculate_base_score,
    calculate_score,
    calculate_entropy,
    get_rating,
    has_common_word,
    has_keyboard_sequence,
    has_repeated_characters,
    has_year_pattern,
    estimate_crack_time
)


# Test 1: Weak password
def test_weak_password():
    assert calculate_score("abc123") == 0


# Test 2: Medium password
def test_medium_password():
    assert calculate_score("Hello123") == 4


# Test 3: Strong password
def test_strong_password():
    assert calculate_score("River!Cloud92#Stone") == 9


# Test 4: Entropy calculation
def test_entropy():
    entropy = calculate_entropy("abc123")
    assert entropy > 0


# Test 5: Common password detection
def test_common_word():
    assert has_common_word("Password123!")


# Test 6: Keyboard sequence detection
def test_keyboard_sequence():
    assert has_keyboard_sequence("myqwerty123")


# Test 7: Repeated characters
def test_repeated_characters():
    assert has_repeated_characters("Helloooo123!")


# Test 8: Year detection
def test_year_pattern():
    assert has_year_pattern("Password2004!")


# Test 9: Password without year
def test_no_year_pattern():
    assert not has_year_pattern("StrongPassword!")


# Test 10: Password rating
def test_rating():
    assert get_rating(2) == "Weak"
    assert get_rating(5) == "Medium"
    assert get_rating(9) == "Strong"


# Test 11: Common word and year reduce score
def test_pattern_penalties():
    password = "Password2024!"
    assert calculate_score(password) < calculate_base_score(password)


# Test 12: Empty password entropy
def test_empty_password_entropy():
    assert calculate_entropy("") == 0

# Test 13: crack time check

def test_instant_crack_time():
    assert estimate_crack_time(0) == "Instant"

def test_less_than_one_second():
    result = estimate_crack_time(1, 2)
    assert result == "Less than a second"

def test_crack_time_seconds():
    result = estimate_crack_time(10, 100)
    assert "seconds" in result

def test_crack_time_minutes():
    result = estimate_crack_time(10, 1)
    assert "minutes" in result


def test_crack_time_years():
    result = estimate_crack_time(50, 1)
    assert "years" in result
