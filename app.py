import streamlit as st
import pickle

# Model aur Vectorizer load karna
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Page Design
st.set_page_config(page_title="ShieldAI Live", page_icon="🛡️")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9f9; }
    h1 { color: #1a5276; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ShieldAI: Live Security Scanner")
st.markdown("---")
st.write("Professional SMS/Email Spam Detection System - Designed by Pritam")

# Input area
input_sms = st.text_area("Analyze Message Content", placeholder="Paste the suspicious text here...", height=150)

if st.button('Analyze Now'):
    if input_sms:
        # Preprocessing & Prediction
        vector_input = tfidf.transform([input_sms])
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]
        confidence = max(proba) * 100

        # Result Display
        if result == 1:
            st.error(f"🚨 SPAM DETECTED! (AI Confidence: {confidence:.2f}%)")
            st.warning("Recommendation: Do not click any links or share personal info.")
        else:
            st.success(f"✅ VERIFIED SAFE (AI Confidence: {confidence:.2f}%)")
            st.info("Recommendation: This message appears legitimate.")
    else:
        st.info("Please enter a message to scan.")
