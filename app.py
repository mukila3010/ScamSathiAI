import joblib

# Load the trained machine learning model
model = joblib.load("scam_model.joblib")



from pathlib import Path
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "scam_model.joblib"
DATASET_PATH = BASE_DIR / "dataset.csv"

# Load existing model, or train one if it is missing
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
