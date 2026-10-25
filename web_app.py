```python
import streamlit as st
from app import analyze_message

st.set_page_config(
    page_title="ScamSathi AI",
    page_icon="🛡️",
    layout="centered"
)

# Custom website design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1220, #132642);
    color: #f8fafc;
}
.block-container {
    max-width: 850px;
    padding-top: 2rem;
}
.hero {
    background: linear-gradient(120deg, #173b61, #245c78);
    padding: 28px;
    border-radius: 20px;
    border: 1px solid #3e6688;
    margin-bottom: 24px;
}
.hero h1 {
    color: white;
    font-size: 38px;
}
.hero p {
    color: #d7e7f5;
    font-size: 16px;
}
.stTextArea textarea {
    background-color: #f8fafc;
    color: #111827;
    border-radius: 12px;
}
.stButton button {
    background: #25b7a5;
    color: white;
    border: none;
    border-radius: 10px;
    min-height: 48px;
    font-weight: bold;
    width: 100%;
}
.footer {
    text-align: center;
    color: #a8bbcf;
    font-size: 13px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)


# Explain message clues
def explain_message(message):
    text = message.lower()
    reasons = []

    patterns = {
        "Urgent or pressure language": [
            "urgent", "immediately", "act now",
            "last chance", "within 24 hours"
        ],
        "OTP or password request": [
            "otp", "password", "pin", "cvv",
            "share your credentials"
        ],
        "Prize or reward claim": [
            "you won", "free prize", "lottery",
            "claim your reward", "congratulations"
        ],
        "Account threat": [
            "account blocked", "account suspended",
            "will be blocked", "verify your account"
        ],
        "Money request": [
            "send money", "pay now", "transfer money",
            "processing fee", "pay a fee"
        ],
        "Suspicious link wording": [
            "click here", "verify now", "http://",
            "https://", "bit.ly", "tinyurl"
        ]
    }

    for reason, keywords in patterns.items():
        matched = [word for word in keywords if word in text]
        if matched:
            reasons.append(f"⚠️ {reason}: '{matched[0]}'")

    if not reasons:
        reasons.append("No common suspicious wording was detected.")

    return reasons


# Header
st.markdown("""
<div class="hero">
    <h1>🛡️ ScamSathi AI</h1>
    <p>Your AI companion for identifying potentially suspicious messages.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("🔍 Analyze a Message")
st.write("Paste an SMS, email, or chat message below.")

message = st.text_area(
    "Message to check",
    placeholder="Example: Your bank account will be blocked. Share your OTP...",
    height=160,
    max_chars=5000
)

# Analyze button
if st.button("🔎 Analyze Message", use_container_width=True):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        try:
            with st.spinner("Analyzing message..."):
                status, risk_score = analyze_message(message.strip())
                reasons = explain_message(message.strip())

            # Analysis result
            st.divider()
            st.subheader("📋 Analysis Result")

            if status == "Potentially suspicious message":
                st.error("⚠️ " + status)
            else:
                st.success("✅ " + status)

            # Model score
            st.metric(
                label="Model scam score",
                value=f"{risk_score}%"
            )

            st.progress(
                max(0.0, min(1.0, risk_score / 100))
            )

            st.caption(
                "This is the model's estimated scam probability, "
                "not a verified fraud-risk measurement."
            )

            # Explanation
            st.divider()
            st.subheader("🔎 Why this result?")

            for reason in reasons:
                st.write(f"- {reason}")

            st.info(
                "These clues are based on message wording. "
                "They are not proof of fraud. Legitimate messages "
                "may contain similar words, and scams may not "
                "contain these clues."
            )

        except Exception:
            st.error("Analysis failed. Please check app.py and dataset.csv.")
            st.exception(Exception("Please check the app configuration and logs."))


# Safety tips
st.divider()
st.subheader("🔐 Safety Tips")

st.markdown("""
- Never share your OTP, password, or banking PIN.
- Avoid clicking unknown links.
- Verify suspicious requests using official contact details.
- Do not send money just because a message creates urgency.
""")

st.markdown("""
<div class="footer">
    ScamSathi AI • Machine Learning Project<br>
    Stay alert. Think before you click.
</div>
""", unsafe_allow_html=True)
```