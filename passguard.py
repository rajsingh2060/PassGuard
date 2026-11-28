
import string
import math
import re
import getpass
from pathlib import Path


#  Password length checking
def check_length(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 2

    return score


# Character checking
def calculate_base_score(password):
    score = check_length(password)

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 2

    return score


# Estimate password entropy
def calculate_entropy(password):
    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)

# Cracking Time Checking
def estimate_crack_time(entropy, guesses_per_second=1_000_000_000):
    """
    Estimate password cracking time.

    Assumes an attacker needs, on average,
    half of the total possible guesses.
    """

    if entropy <= 0:
        return "Instant"

    total_combinations = 2 ** entropy

    average_guesses = total_combinations / 2

    seconds = average_guesses / guesses_per_second

    if seconds < 1:
        return "Less than a second"

    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365.25

    if seconds < 60:
        return f"{seconds:.2f} seconds"

    elif minutes < 60:
        return f"{minutes:.2f} minutes"

    elif hours < 24:
        return f"{hours:.2f} hours"

    elif days < 365.25:
        return f"{days:.2f} days"

    elif years < 1000:
        return f"{years:.2f} years"

    else:
        return f"{years:,.2f} years"



# Load common passwords
def load_common_passwords():
    file_path = Path(__file__).with_name("common.txt")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return {
                line.strip().lower()
                for line in file
                if line.strip()
            }
    except FileNotFoundError:
        return set()


# Detect common passwords or words
def has_common_word(password, common_passwords=None):
    if common_passwords is None:
        common_passwords = load_common_passwords()

    password = password.lower()

    return any(word in password for word in common_passwords)


# Detect keyboard sequences
def has_keyboard_sequence(password):
    sequences = [
        "qwerty", "asdf", "zxcv",
        "1234", "2345", "3456",
        "abcd", "9876"
    ]

    password = password.lower()

    return any(sequence in password for sequence in sequences)


# Detect repeated characters
def has_repeated_characters(password):
    return bool(re.search(r"(.)\1{2,}", password))


# Detect years such as 2004 or 1999
def has_year_pattern(password):
    return bool(re.search(r"(19|20)\d{2}", password))


# Calculate final score
def calculate_score(password):
    score = calculate_base_score(password)

    if has_common_word(password):
        score -= 2

    if has_keyboard_sequence(password):
        score -= 2

    if has_repeated_characters(password):
        score -= 1

    if has_year_pattern(password):
        score -= 1

    return max(0, score)


# Password rating
def get_rating(score):
    if score <= 3:
        return "Weak"
    elif score <= 6:
        return "Medium"
    else:
        return "Strong"


# Main program
def main():
    password = getpass.getpass("Enter your password to check: ")

    base_score = calculate_base_score(password)
    final_score = calculate_score(password)
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    print("\n--- PassGuard Results ---")

    print(f"Base Score: {base_score}/9")
    print(f"Final Score: {final_score}/9")
    print(f"Rating: {get_rating(final_score)}")
    print(f"Estimated Entropy: {entropy:.2f} bits")
    print(f"Estimated Crack Time: {crack_time}")

    print("\nPattern Detection:")

    if has_common_word(password):
        print("- Contains a common password or word.")

    if has_keyboard_sequence(password):
        print("- Contains a keyboard sequence.")

    if has_repeated_characters(password):
        print("- Contains repeated characters.")

    if has_year_pattern(password):
        print("- Contains a year pattern.")

    print("\nPassword check completed.")


if __name__ == "__main__":
    main()
