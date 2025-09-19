import streamlit as st
import pandas as pd
import joblib

# Custom styling
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;   /* Pure black background */
    }
    .stTitle {
        color: purple !important;
        font-size: 50px !important;   /* Heading size */
        font-weight: 900 !important;  /* Extra bold */
        text-align: center;
    }
    /* Input labels */
    .stSelectbox label, .stNumberInput label {
        color: #ffffff !important;    /* White labels for contrast */
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);
    }
    /* Button */
    .stButton > button {
        background: linear-gradient(45deg, #4158D0, #C850C0);
        color: white;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #3147B0, #B740B0);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    /* Input boxes */
    .stSelectbox, .stNumberInput {
        background-color: rgba(30,30,30,0.9);  /* Dark grey for inputs */
        color: white !important;
        border-radius: 10px;
        padding: 0.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        border: 1px solid #444;
    }
    .stSelectbox:hover, .stNumberInput:hover {
        border: 1px solid #C850C0;
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("🔒 SafeTransact App")

# Instructions with better formatting
st.markdown("""
    <h3 style='color:white; text-align: center; margin: 1rem 0; font-size: 2rem;'>
        💳 Enter Transaction Details Below
    </h3>
""", unsafe_allow_html=True)

st.divider()

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    transaction_type = st.selectbox("💱 Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])
    amount = st.number_input("💰 Amount", min_value=0.0, value=1000.0)
    oldbalanceOrg = st.number_input("📤 Old Balance (Sender)", min_value=0.0, value=10000.0)

with col2:
    newbalanceOrig = st.number_input("📥 New Balance (Sender)", min_value=0.0, value=9000.0)
    oldbalanceDest = st.number_input("📊 Old Balance (Receiver)", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("📈 New Balance (Receiver)", min_value=0.0, value=0.0)

# Centered button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    predict_button = st.button("🔍 Predict")

if predict_button:
    with st.spinner('Analyzing transaction...'):
        input_data = pd.DataFrame([{
            "type": transaction_type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest
        }])

        prediction = model.predict(input_data)[0]
        
        # Result
        with st.container():
            st.markdown("---")
            if prediction == 1:
                st.error("⚠ WARNING: This transaction appears to be fraudulent!")
            else:
                st.success("✅ Transaction appears to be legitimate!")