import streamlit as st
import pickle

# Model load karna
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="ShieldAI Live", page_icon="🛡️", layout="centered")

# Sab kuch fix karne ke liye CSS
st.markdown("""
    <style>
    /* Pure White Background */
    .stApp { background-color: white !important; }
    
    /* Text Visibility Fix */
    h1, h2, h3, p, label, .stMarkdown { color: #1a5276 !important; }

    /* Input Box styling - Cursor & Text black */
    .stTextArea textarea {
        background-color: #f8f9fa !important;
        color: #000000 !important;
        caret-color: #000000 !important;
        border: 2px solid #1a5276 !important;
        font-size: 18px !important;
    }

    /* THE BUTTON FIX - Making text visible */
    div.stButton > button {
        background-color: #1a5276 !important;
        color: white !important;
        border-radius: 10px !important;
        width: 100% !important;
        height: 60px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: none !important;
        display: block !important;
    }
    
    /* Button Hover effect */
    div.stButton > button:hover {
        background-color: #2471a3 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ ShieldAI: Live Security Scanner")
st.write("Professional Spam Detection System - Designed by Pritam Dash")

# Input area
input_sms = st.text_area("Analyze Message Content", placeholder="Message yahan paste karein...", height=150)

# Scanning logic
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
        st.warning("⚠️ Please enter a message first.")
