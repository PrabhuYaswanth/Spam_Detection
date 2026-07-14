import streamlit as st
import joblib

# Load trained pipeline
model = joblib.load("spam_model.pkl")

st.set_page_config(page_title="Spam Detection", page_icon="📧")

st.title("📧 Spam Email Detection")

message = st.text_area("Enter your message")

if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:
        prediction = model.predict([message])

        if prediction[0] == "spam":
            st.error("🚫 Spam Message")
        else:
            st.success("✅ Not Spam")