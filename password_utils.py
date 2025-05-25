import re

COMMON_PASSWORDS = {
    'password', '123456', '12345678', 'qwerty', 'abc123', 'football', 'letmein',
    'monkey', 'dragon', '111111', 'baseball', 'iloveyou', 'master', 'sunshine'
}

def analyze_password(password: str) -> dict:
    score = 0
    length = len(password)

    # Check length
    if length >= 8:
        score += 2
    elif length >= 5:
        score += 1

    # Check for lowercase, uppercase, digits, special chars
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1

    # Check if password is common or too simple
    if password.lower() in COMMON_PASSWORDS or length < 4:
        score = 0  # Instantly mark as very weak

    # Determine strength label
    if score >= 6:
        strength = 'Very Strong'
    elif score >= 4:
        strength = 'Strong'
    elif score >= 2:
        strength = 'Moderate'
    elif score >= 1:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    return {
        'score': score,
        'strength': strength
    }

