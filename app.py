import streamlit as st
import pickle

# Model & Vectorizer Load
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except:
    st.error("Error: Model files not found!")

st.set_page_config(page_title="ShieldAI Elite", page_icon="🛡️", layout="centered")

# --- COMPLETE DESIGN OVERHAUL (Glitch Fix) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    h1, h2, h3, p, label, .stMarkdown { color: #000000 !important; font-family: 'Segoe UI', sans-serif !important; }
    
    /* THE BUTTON GLITCH FIX: Using !important on every property */
    div.stButton > button {
        background-color: #000000 !important;
        color: #ffffff !important;
        width: 100% !important;
        height: 55px !important;
        font-weight: 800 !important;
        font-size: 20px !important;
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-transform: uppercase !important;
    }
    
    /* Making sure text is white and visible inside the button */
    div.stButton > button div p {
        color: #ffffff !important;
        font-weight: 800 !important;
    }

    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        caret-color: #000000 !important;
        border: 2px solid #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Dashboard UI (Gitam Name Removed) ---
st.title("🛡️ SHIELDAI: ELITE SECURITY ARCHITECTURE")

# College name removed from here
st.markdown(f"""
    **Lead Developer:** Pritam Kumar Dash | **System Status:** Operational | **Version:** 2.0.1
    
    ---
    **Technical Overview:** This utility utilizes high-precision **Multinomial Naive Bayes** logic to classify communication patterns. It is engineered to identify phishing attempts and social engineering threats with mathematical accuracy.
    """, unsafe_allow_html=True)

# Input area
input_sms = st.text_area("COMMUNICATION TELEMETRY INPUT", 
                         placeholder="Paste the message content here for deep analysis...", 
                         height=150)

# Execution Logic
if st.button('RUN SYSTEM ANALYSIS'):
    if input_sms:
        vector_input = tfidf.transform([input_sms])
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]
        confidence = max(proba) * 100

        if result == 1:
            st.error(f"🚨 CRITICAL THREAT DETECTED! (AI Confidence: {confidence:.2f}%)")
        else:
            st.success(f"✅ SYSTEM VERIFIED SAFE (AI Confidence: {confidence:.2f}%)")
    else:
        st.info("Please provide input for analysis.")
