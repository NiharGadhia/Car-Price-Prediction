import streamlit as st
import pickle

# Load model
model = pickle.load(open("final_model.pkl", "rb"))

# Dictionaries
d1 = {
    "Comprehensive": 0,
    "Third Party insurance": 1,
    "Zero Dep": 2,
    "Not Available": 3,
    "Third Party": 1
}
d2 = {"Petrol": 0, "Diesel": 1, "CNG": 2}
d3 = {"Manual": 0, "Automatic": 1}
d4 = {
    "First Owner": 1,
    "Second Owner": 2,
    "Third Owner": 3,
    "Fourth Owner": 4,
    "Fifth Owner": 5
}

# Page
st.set_page_config(page_title="Car Price Prediction", layout="centered")

# Minimal CSS
st.markdown("""
<style>
/* Overall spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Title */
.title {
    font-size: 30px;
    font-weight: 600;
    text-align: center;
    margin-bottom: 25px;
}

/* Input spacing */
div[data-baseweb="select"] {
    margin-bottom: 12px;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 42px;
    border-radius: 8px;
    background-color: #111827;
    color: white;
    border: 1px solid #374151;
}

.stButton>button:hover {
    border: 1px solid #6366f1;
}

/* Result box */
.result-box {
    margin-top: 25px;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #e5e7eb;
    text-align: center;
}

.price {
    font-size: 28px;
    font-weight: 600;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>Car Price Prediction</div>", unsafe_allow_html=True)

# Inputs
col1, col2 = st.columns(2)

with col1:
    insurance_validity = st.selectbox("Insurance", list(d1.keys()))
    fuel_type = st.selectbox("Fuel Type", list(d2.keys()))

with col2:
    ownership = st.selectbox("Ownership", list(d4.keys()))
    transmission = st.selectbox("Transmission", list(d3.keys()))

kms_driven = st.slider("KMs Driven", 0, 300000, 50000, 5000)

# Predict
if st.button("Predict Price"):
    test = [[
        d1[insurance_validity],
        d2[fuel_type],
        int(kms_driven),
        d4[ownership],
        d3[transmission]
    ]]

    prediction = model.predict(test)[0]
    prediction = round(prediction, 2)

    formatted_price = f"₹ {prediction:,.2f} Lakhs"

    st.markdown(f"""
        <div class="result-box">
            Estimated Price
            <div class="price">{formatted_price}</div>
        </div>
    """, unsafe_allow_html=True)