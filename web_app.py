
import streamlit as st
from app import analyze_message

st.set_page_config(
    page_title="ScamSathi AI",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1220, #132642);
    color: #f8fafc;
}
.block-container {
    max-width: 850px;
    padding-top: 2.5rem;
}
.hero {
    background: linear-gradient(120deg, #173b61, #245c78);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #3e6688;
    margin-bottom: 24px;
}
.hero h1 {
    color: white;
    font-size: 38px;
    margin-bottom: 8px;
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
    height: 48px;
    font-weight: bold;
    width: 100%;
}
.stButton button:hover {
    background: #159583;
    color: white;
}
.result-card {
    padding: 22px;
    border-radius: 16px;
    background: #172b43;
    border: 1px solid #35516d;
    margin-top: 20px;
}
.footer {
    text-align: center;
    color: #a8bbcf;
    font-size: 13px;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🛡️ ScamSathi AI</h1>
    <p>Your AI companion for identifying potentially suspicious messages.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("🔍 Analyze a Message")
st.write(
    "Paste a suspicious SMS, email, or chat message below."
)

message = st.text_area(
    "Message to check",
    placeholder="Example: Your bank account will be blocked. Verify your account now...",
    height=160,
    max_chars=5000
)

if st.button("🔎 Analyze Message"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        try:
            with st.spinner("Analyzing message..."):
                status, risk_score = analyze_message(message.strip())

            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.subheader("Analysis Result")

            if status == "Potentially suspicious message":
                st.error("⚠️ " + status)
            else:
                st.success("✅ " + status)

            st.metric("Model scam score", f"{risk_score}%")
            st.progress(risk_score / 100)

            st.caption(
                "This score is the model's estimated scam probability, "
                "not a verified fraud-risk measurement."
            )
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as error:
            st.error("Analysis failed. Check whether the model is trained.")
            st.caption(str(error))

st.divider()

st.markdown("""
<div class="footer">
    ScamSathi AI • Machine Learning Project<br>
    Stay alert. Never share OTPs, passwords, or banking PINs.
</div>
""", unsafe_allow_html=True)
