def analyze_message(message):
    suspicious_words = [
        "urgent",
        "verify account",
        "click link",
        "prize",
        "otp",
        "password",
        "upi"
    ]

    message_lower = message.lower()

    found_words = [
        word for word in suspicious_words
        if word in message_lower
    ]

    if found_words:
        risk = min(30 + len(found_words) * 15, 90)
        status = "Suspicious - Please verify"
    else:
        risk = 10
        status = "No obvious warning signs detected"

    return status, risk, found_words


if __name__ == "__main__":
    message = input("Enter a message to analyze: ")

    status, risk, words = analyze_message(message)

    print("\n--- ScamSathi AI ---")
    print("Result:", status)
    print("Risk score:", f"{risk}%")
    print("Warning signs:", words if words else "None detected")