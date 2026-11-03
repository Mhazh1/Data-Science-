
import streamlit as st
import joblib
from pathlib import Path

# Locate the project and model
PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_DIR / "models" / "safetech_binary_model.pkl"

# Configure the application
st.set_page_config(
    page_title="SafeTech Insights",
    page_icon="🛡️",
    layout="centered"
)

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# Application interface
st.title("🛡️ SafeTech Insights")
st.subheader("Personal Safety App Review Analyzer")

st.write(
    "Analyze user reviews of personal safety applications "
    "using Natural Language Processing and Machine Learning."
)

st.divider()

# User input
review = st.text_area(
    "Enter a review:",
    placeholder="Example: This app is very helpful and easy to use.",
    height=130
)

# Predict sentiment
if st.button("Analyze Sentiment", type="primary"):
    if not review.strip():
        st.warning("Please enter a review first.")
    else:
        prediction = model.predict([review])[0]

        if prediction == "Positive":
            st.success("Predicted Sentiment: Positive 😊")
        else:
            st.error("Predicted Sentiment: Negative 😞")

st.divider()

st.caption(
    "Model: TF-IDF + Linear SVM | "
    "Trained on personal safety application reviews."
)
