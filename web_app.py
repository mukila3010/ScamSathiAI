
import streamlit as st
from app import analyze_message

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ScamSathi AI",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(37,183,165,0.12), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(66,153,225,0.12), transparent 30%),
        #07111f;
    color: #f8fafc;
}

.block-container {
    max-width: 1150px;
    padding-top: 35px;
    padding-bottom: 40px;
}

/* NAVBAR */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 4px 28px 4px;
}

.logo {
    font-size: 23px;
    font-weight: 800;
    color: white;
}

.logo span {
    color: #25b7a5;
}

/* HERO */
.hero {
    text-align: center;
    padding: 75px 30px 65px 30px;
    border-radius: 28px;
    background:
        linear-gradient(135deg,
        rgba(18,57,91,0.96),
        rgba(20,79,91,0.92));
    border: 1px solid rgba(110,180,210,0.22);
    box-shadow: 0 20px 60px rgba(0,0,0,0.25);
}

.badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 30px;
    background: rgba(37,183,165,0.14);
    border: 1px solid rgba(37,183,165,0.35);
    color: #62e0d0;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 18px;
}

.hero h1 {
    font-size: 58px;
    line-height: 1.05;
    margin: 0;
    color: white;
    font-weight: 800;
}

.hero h1 span {
    color: #37d6c2;
}

.hero p {
    max-width: 680px;
    margin: 20px auto 0 auto;
    color: #c9dceb;
    font-size: 18px;
    line-height: 1.6;
}

/* FEATURE CARDS */
.feature-card {
    background: rgba(18,38,60,0.85);
    border: 1px solid #29445e;
    border-radius: 18px;
    padding: 25px;
    height: 150px;
    margin-top: 30px;
}

.feature-icon {
    font-size: 30px;
}

.feature-title {
    color: white;
    font-size: 17px;
    font-weight: 700;
    margin-top: 8px;
}

.feature-text {
    color: #9fb4c9;
    font-size: 13px;
    margin-top: 6px;
}

/* ANALYZER */
.analyzer {
    margin-top: 55px;
    padding: 38px;
    border-radius: 24px;
    background: #0e2033;
    border: 1px solid #29445e;
}

.section-title {
    font-size: 30px;
    font-weight: 750;
    color: white;
}

.section-subtitle {
    color: #9fb4c9;
    margin-bottom: 25px;
}

/* TEXT AREA */
.stTextArea textarea {
    background: #f8fafc !important;
    color: #111827 !important;
    border-radius: 14px !important;
    border: 2px solid transparent !important;
    font-size: 15px !important;
}

.stTextArea textarea:focus {
    border: 2px solid #25b7a5 !important;
}

/* BUTTON */
.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 13px;
    border: none;
    background: linear-gradient(90deg, #25b7a5, #1fae9d);
    color: white;
    font-size: 16px;
    font-weight: 700;
    transition: 0.2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* RESULT */
.result-box {
    background: #10263b;
    border: 1px solid #31516d;
    padding: 25px;
    border-radius: 18px;
    margin-top: 25px;
}

/* SAFETY */
.safety {
    margin-top: 50px;
    padding: 35px;
    border-radius: 22px;
    background: linear-gradient(135deg,#10263b,#0c1d30);
    border: 1px solid #29445e;
}

.safety h2 {
    color: white;
}

.safety p {
    color: #b5c8d8;
    line-height: 1.7;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #71879b;
    font-size: 13px;
    margin-top: 55px;
    padding-top: 25px;
    border-top: 1px solid #1d344a;
}

</style>
""", unsafe_allow_html=True)


# ---------------- EXPLANATION ----------------
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
            "send money", "pay now",
            "transfer money", "processing fee",
            "pay a fee"
        ],

        "Suspicious link wording": [
            "click here", "verify now",
            "http://", "https://",
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


# ---------------- NAVBAR ----------------
st.markdown("""
<div class="navbar">

<div class="logo">
🛡️ Scam<span>Sathi</span> AI
</div>

<div style="color:#9fb4c9;font-size:14px;">
AI-Powered Scam Awareness
</div>

</div>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------
st.markdown("""
<div class="hero">

<div class="badge">
🛡️ AI-POWERED MESSAGE SECURITY
</div>

<h1>
Think Before You <span>Click.</span>
</h1>

<p>
ScamSathi AI analyzes suspicious SMS, emails and chat messages
using machine learning and highlights potential warning signs
before you take action.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- FEATURES ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI Analysis</div>
        <div class="feature-text">
        Machine learning analyzes message patterns.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Risk Score</div>
        <div class="feature-text">
        Get an estimated scam probability score.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔎</div>
        <div class="feature-title">Explainable Result</div>
        <div class="feature-text">
        Understand the suspicious clues detected.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ---------------- ANALYZER ----------------
st.markdown("""
<div class="analyzer">

<div class="section-title">
🔍 Analyze a Message
</div>

<div class="section-subtitle">
Paste a suspicious SMS, email or chat message below.
We'll check it for potential scam patterns.
</div>

</div>
""", unsafe_allow_html=True)


message = st.text_area(
    "Message to analyze",
    placeholder=(
        "Example:\n"
        "URGENT! Your bank account will be blocked. "
        "Share your OTP immediately..."
    ),
    height=170,
    max_chars=5000
)


if st.button("🔎 Analyze Message"):

    if not message.strip():

        st.warning("⚠️ Please enter a message first.")

    else:

        try:

            with st.spinner("🤖 Analyzing message..."):

                status, risk_score = analyze_message(
                    message.strip()
                )

                reasons = explain_message(
                    message.strip()
                )

            # RESULT
            st.markdown(
                '<div class="result-box">',
                unsafe_allow_html=True
            )

            st.subheader("📋 Analysis Result")

            if status == "Potentially suspicious message":

                st.error(
                    "⚠️ " + status
                )

            else:

                st.success(
                    "✅ " + status
                )

            st.subheader("📊 Model Scam Score")

            st.metric(
                "Estimated scam probability",
                f"{risk_score}%"
            )

            st.progress(
                min(
                    max(risk_score / 100, 0.0),
                    1.0
                )
            )

            st.caption(
                "This score is an experimental model estimate, "
                "not proof of fraud."
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

            # EXPLANATION
            st.divider()

            st.subheader(
                "🔎 Why this result?"
            )

            for reason in reasons:

                st.write(reason)

            st.info(
                "These clues are based on message wording. "
                "They are not proof of fraud."
            )

        except Exception as error:

            st.error(
                "❌ Analysis failed."
            )

            st.caption(
                str(error)
            )


# ---------------- SAFETY ----------------
st.markdown("""
<div class="safety">

<h2>🔐 Stay Safe Online</h2>

<p>
🛑 <b>Never share</b> OTP, password, PIN or CVV with anyone.
</p>

<p>
🔗 <b>Think before clicking</b> unknown links or downloading files.
</p>

<p>
💳 <b>Verify payment requests</b> through official websites or numbers.
</p>

<p>
🚨 <b>Don't panic</b> when a message creates unnecessary urgency.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">

🛡️ <b>ScamSathi AI</b><br>

Machine Learning Project • Stay Alert • Think Before You Click

</div>
""", unsafe_allow_html=True)
