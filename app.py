import streamlit as st
import pickle

# Model load karna
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="ShieldAI Live", page_icon="🛡️")

# Custom CSS for Visibility and Cursor
st.markdown("""
    <style>
    /* Background and Text Colors */
    .stApp { background-color: #ffffff; }
    h1, p, label { color: #1a5276 !important; }
    
    /* Input Area - Cursor Fix */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #1a5276 !important;
        caret-color: #000000 !important; /* Isse likhne wala point/cursor dikhega */
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        background-color: #1a5276 !important;
        color: white !important;
        border-radius: 8px;
        height: 50px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ShieldAI: Live Security Scanner")
st.write("Professional Spam Detection System - Designed by Pritam Dash")

# Input area
input_sms = st.text_area("Analyze Message Content", placeholder="Yahan apna message paste karein...", height=150)

if st.button('🚀 EXECUTE DEEP SCAN'):
    if input_sms:
        vector_input = tfidf.transform([input_sms])
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]
        confidence = max(proba) * 100

        if result == 1:
            st.error(f"🚨 SPAM DETECTED! (AI Confidence: {confidence:.2f}%)")
        else:
            st.success(f"✅ VERIFIED SAFE (AI Confidence: {confidence:.2f}%)")
    else:
        st.info("ℹ️ Please enter a message to scan.")
