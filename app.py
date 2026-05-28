import streamlit as st
import pickle

# Model & Vectorizer Load
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except:
    st.error("Error: Model files not found!")

st.set_page_config(page_title="ShieldAI Dark Ops", page_icon="🛡️", layout="centered")

# --- DARK MODE DESIGN OVERHAUL ---
st.markdown("""
    <style>
    /* 1. Background Pure Black */
    .stApp {
        background-color: #000000 !important;
    }

    /* 2. All Text to Pure White */
    h1, h2, h3, p, label, .stMarkdown, .stText, span {
        color: #ffffff !important;
        font-family: 'Courier New', Courier, monospace !important;
    }

    /* 3. Text Area - Black Background, White Border, White Text/Cursor */
    .stTextArea textarea {
        background-color: #000000 !important;
        color: #ffffff !important;
        caret-color: #ffffff !important; /* White Cursor */
        border: 2px solid #ffffff !important;
        font-size: 16px !important;
    }

    /* 4. Button - White Background with Black Text */
    div.stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 0px !important; /* Sharp edges for terminal look */
        width: 100% !important;
        height: 50px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border: none !important;
        text-transform: uppercase !important;
    }
    
    div.stButton > button:hover {
        background-color: #cccccc !important;
        color: #000000 !important;
    }

    /* 5. Result Boxes Styling */
    .stAlert {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Dashboard UI
st.title("🛡️ SHIELDAI: DARK SECURITY CONSOLE")

st.markdown(f"""
    **OPERATOR:** PRITAM KUMAR DASH | **SYSTEM:** LIVE | **ENCRYPTION:** ACTIVE
    
    ---
    **ANALYTICS ENGINE:** This console employs **Multinomial Naive Bayes** to dissect incoming telemetry. It is optimized for detecting adversarial phishing patterns and linguistic anomalies.
    """, unsafe_allow_html=True)

# Input area
input_sms = st.text_area("INCOMING DATA STREAM", 
                         placeholder="Paste encrypted or suspicious text for analysis...", 
                         height=150)

# Execution Logic
if st.button('INITIATE DEEP ANALYSIS'):
    if input_sms:
        vector_input = tfidf.transform([input_sms])
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]
        confidence = max(proba) * 100

        if result == 1:
            st.error(f"⚠️ THREAT DETECTED! (CONFIDENCE: {confidence:.2f}%)")
        else:
            st.success(f"✅ CLEAR: NO ANOMALIES FOUND (CONFIDENCE: {confidence:.2f}%)")
    else:
        st.info("System waiting for input telemetry...")
