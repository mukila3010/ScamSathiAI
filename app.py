
from pathlib import Path
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "scam_model.joblib"
DATASET_PATH = BASE_DIR / "dataset.csv"

# Load model or train it from the dataset
if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)
else:
    data = pd.read_csv(DATASET_PATH)
    data = data.dropna(subset=["message", "label"])
    data["message"] = data["message"].astype(str)
    data["label"] = data["label"].astype(str).str.strip().str.lower()

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    model.fit(data["message"], data["label"])
    joblib.dump(model, MODEL_PATH)


def analyze_message(message):
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]
    classes = list(model.classes_)
    scam_index = classes.index("scam")
    risk_score = round(probabilities[scam_index] * 100)

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
            break

        if not message.strip():
            print("Please enter a message.")
            continue

        status, risk_score = analyze_message(message.strip())
        print("\nResult:", status)
        print("Model scam score:", f"{risk_score}%")
        print("This experimental score does not prove fraud.")
