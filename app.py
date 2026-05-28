import streamlit as st
import pickle

# Model & Vectorizer Load
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except:
    st.error("Error: Model files not found!")

st.set_page_config(page_title="ShieldAI Enterprise", page_icon="🛡️", layout="centered")

# Professional Theme Styling
st.markdown("""
    <style>
    .stApp { background-color: #ffffff !important; }
    h1, h2, h3, p, label, .stMarkdown { color: #000000 !important; font-family: 'Segoe UI', sans-serif !important; }
    
    /* Input Area */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        caret-color: #000000 !important;
        border: 2px solid #000000 !important;
    }

    /* Professional Button */
    div.stButton > button {
        background-color: #000000 !important;
        color: #ffffff !important;
        width: 100% !important;
        height: 50px !important;
        font-weight: bold !important;
        border: none !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div.stButton > button:hover { background-color: #333333 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- Dashboard UI (Enterprise Look) ---
st.title("🛡️ SHIELDAI: ENTERPRISE SPAM ARCHITECTURE")

st.markdown(f"""
    **Lead Developer:** Pritam Dash | **Affiliation:** GITAM | **System Status:** Operational
    
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
            st.warning("Protocol: Quarantining message recommended. Do not engage with links.")
        else:
            st.success(f"✅ SYSTEM VERIFIED SAFE (AI Confidence: {confidence:.2f}%)")
            st.info("Protocol: Message appears legitimate based on current datasets.")
    else:
        st.info("Please provide input for analysis.")
