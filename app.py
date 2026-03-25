import streamlit as st

# Page configuration
st.set_page_config(page_title="Healthcare App", layout="centered")

# Title
st.title("🏥 Cloud Healthcare Record System")
st.markdown("### Patient Registration Form")

# Form
with st.form("patient_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload Medical Report",
        type=["pdf", "png", "jpg", "jpeg"]
    )
    
    submit = st.form_submit_button("Register")

# After submission
if submit:
    if name == "" or age == 0:
        st.error("⚠️ Please fill all required fields")
    else:
        st.success("✅ Registration Successful")

        st.markdown("### 📋 Patient Details")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")

        # Show uploaded file
        if uploaded_file is not None:
            st.markdown("### 📁 Uploaded Report")

            if uploaded_file.type.startswith("image"):
                st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            elif uploaded_file.type == "application/pdf":
                st.info("📄 PDF file uploaded successfully")
        else:
            st.warning("No file uploaded")