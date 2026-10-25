import joblib

# Load the trained machine learning model
model = joblib.load("scam_model.joblib")


def analyze_message(message):
    prediction = model.predict([message])[0]

    probabilities = model.predict_proba([message])[0]
    classes = list(model.classes_)
    scam_index = classes.index("scam")
    scam_probability = probabilities[scam_index]

    risk_score = round(scam_probability * 100)

    if prediction == "scam":
        status = "Potentially suspicious message"
    else:
        status = "No obvious scam pattern detected"

    return status, risk_score


if __name__ == "__main__":
    print("=== ScamSathi AI ===")
    print("Enter 'exit' to quit.")

    while True:
        message = input("\nEnter a message: ")

        if message.strip().lower() == "exit":
            print("Thank you for using ScamSathi AI!")
            break

        if not message.strip():
            print("Please enter a message.")
            continue

        status, risk_score = analyze_message(message)

        print("\nResult:", status)
        print("Model scam score:", f"{risk_score}%")
        print("Note: This is an experimental model, not proof of fraud.")