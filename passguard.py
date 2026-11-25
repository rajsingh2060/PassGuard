
import getpass
import string


# 1. Check password length
def check_length(pw):
    score = 0

    if len(pw) >= 8:
        score += 1

    if len(pw) >= 12:
        score += 1

    if len(pw) >= 16:
        score += 2

    return score


# 2. Check for lowercase letters
def check_lowercase(pw):
    return 1 if any(c.islower() for c in pw) else 0


# 3. Check for uppercase letters
def check_uppercase(pw):
    return 1 if any(c.isupper() for c in pw) else 0


# 4. Check for numbers
def check_digits(pw):
    return 1 if any(c.isdigit() for c in pw) else 0


# 5. Check for symbols
def check_symbols(pw):
    return 2 if any(c in string.punctuation for c in pw) else 0


# 6. Generate improvement tips
def get_tips(pw):
    tips = []

    if len(pw) < 8:
        tips.append("Use at least 8 characters.")

    if len(pw) < 12:
        tips.append("Consider using at least 12 characters.")

    if not any(c.islower() for c in pw):
        tips.append("Add at least one lowercase letter.")

    if not any(c.isupper() for c in pw):
        tips.append("Add at least one uppercase letter.")

    if not any(c.isdigit() for c in pw):
        tips.append("Add at least one number.")

    if not any(c in string.punctuation for c in pw):
        tips.append("Add at least one symbol.")

    return tips


# 7. Calculate total score
def calculate_score(pw):
    score = (
        check_length(pw)
        + check_lowercase(pw)
        + check_uppercase(pw)
        + check_digits(pw)
        + check_symbols(pw)
    )

    return score


# 8. Determine password strength
def get_strength(score):
    if score <= 3:
        return "Weak"
    elif score <= 6:
        return "Medium"
    else:
        return "Strong"


# 9. Main program
def main():
    print("=" * 40)
    print("       PASSGUARD PASSWORD CHECKER")
    print("=" * 40)

    password = getpass.getpass("Enter a sample password: ")

    score = calculate_score(password)
    strength = get_strength(score)
    tips = get_tips(password)

    print("\nPassword Analysis")
    print("-" * 40)

    print(f"Score: {score}/9")
    print(f"Strength: {strength}")

    if tips:
        print("\nSuggestions to improve your password:")

        for tip in tips:
            print("- " + tip)
    else:
        print("\nGreat! All basic password rules are satisfied.")

    print("\nYour password was not displayed or saved.")


if __name__ == "__main__":
    main()
