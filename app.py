import streamlit as st
import pickle

# Model aur Vectorizer load karna
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Page Design (Fixed for Streamlit Cloud)
st.set_page_config(page_title="ShieldAI Live", page_icon="🛡️")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    h1 { color: #1a5276 !important; text-align: center; }
    p { color: #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ShieldAI: Live Security Scanner")
st.write("Professional SMS/Email Spam Detection System - By Pritam Dash")

# Input area (Dark box for better visibility)
input_sms = st.text_area("Analyze Message Content", placeholder="Paste the suspicious text here...", height=150)

if st.button('Execute Deep Scan'):
    if input_sms:
        # Prediction logic
        vector_input = tfidf.transform([input_sms])
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]
        confidence = max(proba) * 100

        if result == 1:
            st.error(f"🚨 SPAM DETECTED! (AI Confidence: {confidence:.2f}%)")
            st.warning("Action: Do not click any links or share personal info.")
        else:
            st.success(f"✅ VERIFIED SAFE (AI Confidence: {confidence:.2f}%)")
    else:
        st.info("Please enter a message to scan.")
