from colorama import Fore, Style, init

init(autoreset=True)
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


# banner printer
def print_banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
 ____                  ____                     _
|  _ \ __ _ ___ ___  / ___|_   _  __ _ _ __ __| |
| |_) / _` / __/ __| \___ \ | | |/ _` | '__/ _` |
|  __/ (_| \__ \__ \  ___) || |_| (_| | | | (_| |
|_|   \__,_|___/___/ |____/  \__,_|\__,_|_|  \__,_|
    """)

    print(Fore.WHITE + "          PASSWORD SECURITY ANALYZER")
    print(Fore.CYAN + "       --------------------------------")
    print()


def print_score_bar(score):
    score = max(0, min(9, score))

    filled = score
    empty = 9 - score

    bar = (
        Fore.GREEN + "█" * filled +
        Fore.WHITE + "░" * empty
    )

    print(f"  [{bar}] {score}/9")


def print_section(title):
    print()
    print(Fore.CYAN + Style.BRIGHT + f"  {title}")
    print(Fore.WHITE + "  " + "-" * 38)


def display_pattern(name, detected):
    if detected:
        print(Fore.RED + f"  [!] {name}: DETECTED")
    else:
        print(Fore.GREEN + f"  [+] {name}: SAFE")


# password suggestions
def get_password_suggestions(password):
    suggestions = []

    if len(password) < 12:
        suggestions.append(
            "Increase password length to at least 12-16 characters."
        )

    if not any(c.islower() for c in password):
        suggestions.append(
            "Include lowercase letters (a-z)."
        )

    if not any(c.isupper() for c in password):
        suggestions.append(
            "Include uppercase letters (A-Z)."
        )

    if not any(c.isdigit() for c in password):
        suggestions.append(
            "Include numbers (0-9)."
        )

    if not any(c in string.punctuation for c in password):
        suggestions.append(
            "Include special characters such as @, #, ! or %."
        )

    if has_common_word(password):
        suggestions.append(
            "Avoid common passwords and predictable dictionary words."
        )

    if has_keyboard_sequence(password):
        suggestions.append(
            "Avoid keyboard sequences such as qwerty or 1234."
        )

    if has_repeated_characters(password):
        suggestions.append(
            "Avoid repeating the same character consecutively."
        )

    if has_year_pattern(password):
        suggestions.append(
            "Avoid predictable years such as birth years or calendar years."
        )

    if not suggestions:
        suggestions.append(
            "Your password meets the current checks. "
            "Consider using a longer, randomly generated password."
        )

    suggestions.append(
        "Use a unique password for every account."
    )

    suggestions.append(
        "Consider using a trusted password manager."
    )

    return suggestions

#display results
def display_results(password):
    base_score = calculate_base_score(password)
    score = calculate_score(password)
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    rating = get_rating(score)

    if rating == "Strong":
        color = Fore.GREEN
    elif rating == "Medium":
        color = Fore.YELLOW
    else:
        color = Fore.RED

    print_banner()

    print_section("PASSWORD STRENGTH")

    print(f"  Rating: {color}{Style.BRIGHT}{rating}")
    print(f"  Score : {score}/9")
    print_score_bar(score)

    print_section("SECURITY ANALYSIS")

    print(f"  Estimated entropy : {entropy:.2f} bits")
    print(f"  Estimated crack time: {crack_time}")

    print_section("THREAT DETECTION")

    display_pattern(
        "Common password",
        has_common_word(password)
    )

    display_pattern(
        "Keyboard sequence",
        has_keyboard_sequence(password)
    )

    display_pattern(
        "Repeated characters",
        has_repeated_characters(password)
    )

    display_pattern(
        "Year pattern",
        has_year_pattern(password)
    )

    print_section("FINAL REPORT")

    if rating == "Strong":
        print(Fore.GREEN + "  Your password looks strong!")
    elif rating == "Medium":
        print(Fore.YELLOW + "  Your password needs improvement.")
    else:
        print(Fore.RED + "  Your password is weak!")

    print_section("PASSWORD IMPROVEMENT SUGGESTIONS")

    suggestions = get_password_suggestions(password)

    for suggestion in suggestions:
       print(Fore.YELLOW + f"  [TIP] {suggestion}")
    print(Fore.CYAN + "\n  Thank you for using PassGuard!")
    print(Fore.WHITE + "  --------------------------------------")

# Main program
def main():
    password = getpass.getpass(
        Fore.YELLOW + "\n  Enter password to check: "
    )

    if not password:
        print(Fore.RED + "\n  No password entered!")
        return

    display_results(password)


if __name__ == "__main__":
    main()