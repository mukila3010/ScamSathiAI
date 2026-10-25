import streamlit as st
from app import analyze_message

st.set_page_config(
    page_title="ScamSathi AI",
    page_icon="🛡️",
    layout="centered"
)

# ---------- CUSTOM UI ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #07111f, #102a43);
    color: white;
}

.block-container {
    max-width: 850px;
    padding-top: 35px;
}

.hero {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(135deg, #12395b, #176b78);
    text-align: center;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 8px;
}

.hero p {
    color: #dcecf5;
    font-size: 17px;
}

.card {
    background: #142b43;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #31516c;
    margin-top: 20px;
}

.tip {
    background: #10263b;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #29465d;
}

.footer {
    text-align: center;
    color: #9fb3c8;
    margin-top: 30px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


# ---------- EXPLANATION ----------
def explain_message(message):
    text = message.lower()
    reasons = []

    patterns = {
        "Urgent or pressure language": [
            "urgent", "immediately", "act now", "last chance"
        ],
        "OTP or password request": [
            "otp", "password", "pin", "cvv"
        ],
        "Prize or reward claim": [
            "free prize", "you won", "lottery", "claim your reward"
        ],
        "Account threat": [
            "account blocked", "account suspended",
            "verify your account"
        ],
        "Money request": [
            "send money", "pay now",
            "transfer money", "processing fee"
        ],
        "Suspicious link wording": [
            "click here", "http://", "https://",
            "bit.ly", "tinyurl"
        ]
    }

    for reason, keywords in patterns.items():
        for word in keywords:
            if word in text:
                reasons.append(
                    f"⚠️ {reason}: detected '{word}'"
                )
                break

    if not reasons:
        reasons.append(
            "✅ No common suspicious wording was detected."
        )

    return reasons


# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <h1>🛡️ ScamSathi AI</h1>
    <p>AI-powered suspicious message analyzer</p>
</div>
""", unsafe_allow_html=True)


# ---------- INPUT ----------
st.subheader("📩 Check Your Message")

st.write(
    "Paste an SMS, email, or chat message below "
    "to check for suspicious patterns."
)

message = st.text_area(
    "Message",
    placeholder="Example: Your account will be blocked. Share your OTP immediately...",
    height=160,
    max_chars=5000
)


# ---------- ANALYZE ----------
if st.button("🔎 Analyze Message", use_container_width=True):

    if not message.strip():

        st.warning("⚠️ Please enter a message first.")

    else:

        try:

            with st.spinner("🤖 Analyzing your message..."):

                status, risk_score = analyze_message(
                    message.strip()
                )

                reasons = explain_message(
                    message.strip()
                )

            # RESULT
            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            st.subheader("📋 Analysis Result")

            if status == "Potentially suspicious message":
                st.error("⚠️ " + status)
            else:
                st.success("✅ " + status)

            st.subheader("📊 Model Scam Score")

            st.metric(
                "Estimated scam probability",
                f"{risk_score}%"
            )

            st.progress(
                min(max(risk_score / 100, 0.0), 1.0)
            )

            st.caption(
                "This is an experimental model score, "
                "not proof of fraud."
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

            # WHY RESULT
            st.divider()

            st.subheader("🔎 Why this result?")

            for reason in reasons:
                st.write(reason)

            st.info(
                "These are text-based warning clues. "
                "They are not proof of fraud."
            )

        except Exception as error:

            st.error(
                "❌ Analysis failed."
            )

            st.write(
                "Please check the application configuration."
            )


# ---------- SAFETY ----------
st.divider()

st.subheader("🔐 Safety Tips")

st.markdown("""
<div class="tip">

<b>🛑 Never share:</b><br>
OTP • Password • PIN • CVV

<br><br>

<b>🔗 Be careful with:</b><br>
Unknown links • Prize messages • Urgent payment requests

<br><br>

<b>✅ Always:</b><br>
Verify suspicious messages through official sources.

</div>
""", unsafe_allow_html=True)


# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    ScamSathi AI • Machine Learning Project<br>
    Stay Alert • Think Before You Click
</div>
""", unsafe_allow_html=True)