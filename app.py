import streamlit as st

st.set_page_config(page_title="Mini Healthcare App", layout="centered")
st.title("🏥 Mini Healthcare App")
st.subheader("Patient Registration Form")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0)
gender = st.radio("Select Gender", ["Male", "Female", "Other"])
symptoms = st.text_area("Describe your symptoms")

if st.button("Submit"):
    st.success(f"Hello {name}, your registration is successful!")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Symptoms:** {symptoms}")
    st.balloons()