# 🔐 PassGuard – Password Strength Checker

PassGuard is a Python-based password strength checker that evaluates password security using character diversity, entropy estimation, pattern detection, and password scoring. It also provides estimated cracking time and personalized suggestions to help users create stronger passwords.

## 🚀 Features

- Password length checking
- Uppercase and lowercase character detection
- Number and special character detection
- Password strength scoring (out of 9)
- Weak, Medium, and Strong ratings
- Password entropy estimation (bits)
- Common password and dictionary word detection
- Keyboard sequence detection (qwerty, 1234, etc.)
- Repeated character detection
- Year pattern detection (e.g. 2004, 2024)
- Pattern-based score reduction
- Estimated password cracking time
- Personalized password improvement suggestions
- Automated unit testing using pytest

### User Interface
- Colorful terminal dashboard using Colorama
- Visual password strength score bar
- Security analysis and threat detection report
- Easy-to-understand improvement recommendations

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (Regex)
- Math Library
- String Library
- Getpass
- Colorama
- Pytest

## 📂 Project Structure

```text
PassGuard/
│
├── passguard.py
├── common.txt
├── test_passguard.py
├── README.md
├── .gitignore
└── venv/
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd PassGuard
```

Install the required packages:

```bash
pip install colorama pytest
```

## ▶️ Usage

Run PassGuard:

```bash
python passguard.py
```

Run automated tests:

```bash
pytest -v
```

## 📊 Password Analysis

PassGuard evaluates passwords using:

- **Password Score:** Rates password strength out of 9.
- **Entropy:** Estimates password guessing difficulty in bits.
- **Pattern Detection:** Identifies common passwords, keyboard sequences, repeated characters, and year patterns.
- **Crack Time:** Estimates theoretical password cracking time using a configurable guessing speed.
- **Improvement Suggestions:** Provides recommendations based on detected weaknesses.

## 💡 Password Improvement Suggestions

PassGuard provides recommendations such as:

- Increase password length to at least 12–16 characters.
- Include uppercase and lowercase letters.
- Include numbers and special characters.
- Avoid common passwords and predictable words.
- Avoid repeated characters and keyboard sequences.
- Avoid predictable years.
- Use a unique password for every account.
- Consider using a trusted password manager.

## 🧪 Automated Testing

The project uses pytest to verify password-checking functionality.

Tests cover:

- Weak, medium, and strong passwords
- Entropy calculation
- Common password detection
- Keyboard sequence detection
- Repeated character detection
- Year pattern detection
- Password ratings
- Crack-time estimation
- Password improvement suggestions

Run tests using:

```bash
pytest -v
```

## 🔒 Disclaimer

PassGuard is an educational cybersecurity project. Entropy and cracking-time calculations are theoretical estimates and do not guarantee actual password security. Real-world cracking times depend on password predictability, attack methods, hardware, and other factors.

## 👨‍💻 Author

Developed as a Python learning project.

**Project:** PassGuard  
**Version:** 2.1  
**Category:** Python / Cybersecurity