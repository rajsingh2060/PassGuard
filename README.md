# 🔐 PassGuard – Password Strength Checker

PassGuard is a Python-based password strength checker that evaluates password security using password length, character diversity, entropy estimation, and common pattern detection.

## 🚀 Features

- Password length checking
- Uppercase and lowercase character detection
- Number and special character detection
- Password strength scoring
- Weak, Medium, and Strong ratings
- Password entropy estimation (bits)
- Common password and dictionary word detection
- Keyboard sequence detection (qwerty, 1234, etc.)
- Repeated character detection
- Year pattern detection (e.g. 2004, 2024)
- Pattern-based score reduction
- Estimated password cracking time
- Automated unit testing using pytest

## 🛠️ Technologies Used

- Python 3
- Regular Expressions
- Math Library
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

Install pytest:

```bash
pip install pytest
```

## ▶️ Usage

Run the password checker:

```bash
python passguard.py
```

Run automated tests:

```bash
pytest -v
```

## 📊 Password Analysis

PassGuard provides:

- Password score out of 9
- Password strength rating
- Estimated entropy in bits
- Common pattern warnings
- Estimated password cracking time

Cracking time is a theoretical estimate based on the assumed number of guesses per second.

## 🧪 Testing

The project includes automated tests covering:

- Weak, medium, and strong passwords
- Entropy calculation
- Common password detection
- Keyboard sequence detection
- Repeated characters
- Year pattern detection
- Password rating
- Crack-time estimation

## 🔒 Disclaimer

PassGuard is an educational project. Entropy and cracking-time estimates are theoretical and do not guarantee actual password security.

## 👨‍💻 Author

Developed as a Python learning project.

**Project:** PassGuard  
**Version:** 2.0 (Week 2 Update)