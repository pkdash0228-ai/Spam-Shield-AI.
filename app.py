import streamlit as st
import pickle

# Model load karna
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="ShieldAI Live", page_icon="🛡️")

# Force styling for better visibility
st.markdown("""
    <style>
    .stApp { background-color: white; }
    h1, h2, h3, p, span, label { color: #1a5276 !important; font-weight: bold; }
    .stButton>button {
        width: 100%;
        background-color: #2E86C1 !important;
        color: white !important;
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
        border: none;
    }
    .stTextArea textarea {
        background-color: #f1f2f6 !important;
        color: #2f3542 !important;
        border: 2px solid #1a5276 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ShieldAI: Live Security Scanner")
st.write("Professional Spam Detection System - Designed by Pritam Dash")

# Input area
input_sms = st.text_area("Analyze Message Content", placeholder="Paste the suspicious text here...", height=150)

if st.button('🚀 EXECUTE DEEP SCAN'):
    if input_sms:
        vector_input = tfidf.transform([input_sms])
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]
        confidence = max(proba) * 100

        if result == 1:
            st.error(f"🚨 SPAM DETECTED! (AI Confidence: {confidence:.2f}%)")
            st.warning("⚠️ ACTION: Do not click any links or share personal info.")
        else:
            st.success(f"✅ VERIFIED SAFE (AI Confidence: {confidence:.2f}%)")
    else:
        st.info("ℹ️ Please enter a message to scan.")
