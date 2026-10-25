import streamlit as st
from app import analyze_message

st.set_page_config(
    page_title="ScamSathi AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ ScamSathi AI")
st.write("AI-powered suspicious message analyzer")

message = st.text_area(
    "📩 Enter your message",
    placeholder="Example: Your account will be blocked. Share your OTP immediately...",
    height=180
)

def explain_message(message):
    text = message.lower()
    reasons = []

    if any(word in text for word in ["urgent", "immediately", "act now", "last chance"]):
        reasons.append("Urgent or pressure language detected")

    if any(word in text for word in ["otp", "password", "pin", "cvv"]):
        reasons.append("OTP, password, PIN or confidential information request detected")

    if any(word in text for word in ["free prize", "you won", "lottery", "claim your reward"]):
        reasons.append("Prize or reward claim detected")

    if any(word in text for word in ["account blocked", "account suspended", "verify your account"]):
        reasons.append("Account threat or verification request detected")

    if any(word in text for word in ["send money", "pay now", "transfer money", "processing fee"]):
        reasons.append("Money or payment request detected")

    if any(word in text for word in ["click here", "http://", "https://", "bit.ly", "tinyurl"]):
        reasons.append("Potentially suspicious link detected")

    if not reasons:
        reasons.append("No common suspicious wording was detected")

    return reasons


if st.button("🔎 Analyze Message"):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        status, risk_score = analyze_message(message.strip())

        st.divider()

        st.subheader("📋 Analysis Result")

        if status == "Potentially suspicious message":
            st.error("⚠️ " + status)
        else:
            st.success("✅ " + status)

        st.subheader("📊 Model Scam Score")
        st.metric(
            label="Estimated scam probability",
            value=f"{risk_score}%"
        )

        st.progress(
            min(max(risk_score / 100, 0.0), 1.0)
        )

        st.caption(
            "This is an experimental model score, not proof of fraud."
        )

        st.divider()

        st.subheader("🔎 Why this result?")

        reasons = explain_message(message.strip())

        for reason in reasons:
            st.write("• " + reason)

        st.info(
            "These are text-based warning clues. "
            "They are not proof that a message is fraudulent."
        )


st.divider()

st.subheader("🔐 Safety Tips")

st.write("• Never share OTP, password or banking PIN.")
st.write("• Avoid clicking unknown links.")
st.write("• Verify suspicious requests through official channels.")
st.write("• Do not send money because of urgent messages.")

st.divider()

st.caption(
    "ScamSathi AI • Machine Learning Project • Stay Alert"
)