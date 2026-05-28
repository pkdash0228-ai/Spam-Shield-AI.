import streamlit as st
import pickle

# Model & Vectorizer Load
try:
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except:
    st.error("Error: Model files not found!")

st.set_page_config(page_title="ShieldAI Console", page_icon="🛡️", layout="centered")

# --- DARK CONFIGURATION ARCHITECTURE ---
st.markdown("""
    <style>
    /* 1. Global Dark Theme Override */
    .stApp {
        background-color: #0f111a !important; /* Premium dark background like references */
    }

    /* 2. Standard Text and Headings */
    h2, h3, p, label, .stMarkdown, .stText, span {
        color: #ffffff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }

    /* 3. The Custom Header Component to mimic 1000189947.jpg */
    .app-header-container {
        display: flex !important;
        align-items: center !important;
        gap: 15px !important;
        margin-top: 10px !important;
        margin-bottom: 25px !important;
    }
    .app-logo {
        font-size: 55px !important; /* Matches size of image logo */
        line-height: 1 !important;
    }
    .app-title-text {
        color: #ffffff !important;
        font-size: 42px !important; /* Clean, bold typography */
        font-weight: 700 !important;
        line-height: 1.2 !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    /* 4. Input Architecture Styling */
    .stTextArea label {
        font-size: 14px !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        color: #a0a5b5 !important; /* Muted silver for standard label look */
        margin-bottom: 8px !important;
    }
    .stTextArea textarea {
        background-color: #1a1c24 !important;
        color: #ffffff !important;
        caret-color: #ffffff !important;
        border: 1px solid #2d313f !important;
        border-radius: 8px !important;
        font-size: 16px !important;
    }
    .stTextArea textarea:focus {
        border-color: #ffffff !important;
    }

    /* 5. Minimalist Action Component */
    div.stButton > button {
        background-color: transparent !important;
        color: #ffffff !important;
        border: 1px solid #2d313f !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        border-color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
    }
    div.stButton > button p {
        color: #ffffff !important;
    }

    /* 6. Alert Architecture Modifiers */
    .stAlert {
        background-color: #1a1c24 !important;
        border: 1px solid #2d313f !important;
        border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CUSTOM HEADER LAYOUT (As requested per 1000189947.jpg) ---
st.markdown("""
    <div class="app-header-container">
        <div class="app-logo">🛡️</div>
        <div class="app-title-text">ShieldAI Spam Detection Web App</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    **Operator:** PRITAM KUMAR DASH | **System:** Live Deployment Architecture
    
    ---
    """, unsafe_allow_html=True)

# Input area
input_sms = st.text_area("Communication Telemetry Input", 
                         placeholder="Paste structural message telemetry stream here...", 
                         height=140)

# Execution Logic
if st.button('Run Deep Scan'):
    if input_sms:
        vector_input = tfidf.transform([input_sms])
        result = model.predict(vector_input)[0]
        proba = model.predict_proba(vector_input)[0]
        confidence = max(proba) * 100

        if result == 1:
            st.error(f"🚨 CRITICAL THREAT DETECTED! (AI Confidence: {confidence:.2f}%)")
        else:
            st.success(f"✅ VERIFIED SAFE (AI Confidence: {confidence:.2f}%)")
    else:
        st.info("System initializing... Provide tracking telemetry.")
