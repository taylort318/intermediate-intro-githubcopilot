import streamlit as st
# Add rose gold and playful style
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f6d1c1 0%, #b76e79 100%) !important;
    }
    .stApp {
        background: linear-gradient(135deg, #f6d1c1 0%, #b76e79 100%) !important;
    }
    .rose-gold-title {
        color: #b76e79;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive, sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1.5rem;
        letter-spacing: 1px;
    }
    label, .stTextInput > label {
        color: #b76e79 !important;
        font-weight: bold;
        font-size: 2.2rem;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive, sans-serif;
    }
    .stTextInput input[type="text"], .stTextInput input[type="email"] {
        background: #fff !important;
        color: #b76e79 !important;
        border: 1.5px solid #b76e79;
        border-radius: 8px;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .stTextInput > div > input {
        background: #fff !important;
        color: #b76e79 !important;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .stButton > button {
        background: linear-gradient(90deg, #f6d1c1 0%, #b76e79 100%);
        color: #fff;
        border: none;
        border-radius: 8px;
        font-size: 1.8rem;
        font-weight: bold;
        padding: 0.5rem 2rem;
        margin-top: 1rem;
        box-shadow: 0 2px 8px 0 rgba(183, 110, 121, 0.15);
        transition: 0.2s;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #b76e79 0%, #f6d1c1 100%);
        color: #b76e79;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="rose-gold-title">🌹 Tutoring Signup Form</div>', unsafe_allow_html=True)

with st.form("signup_form"):
    first_name = st.text_input("First Name:")
    last_name = st.text_input("Last Name:")
    background = st.text_input("Background:")
    courses = st.text_input("List of Courses:")
    email = st.text_input("Email Address:")
    submit = st.form_submit_button("Submit:")

    if submit:
        st.success(f"Thank you for signing up, {first_name} {last_name}! 🌟")
        st.write("**Background:**", background)
        st.write("**List of Courses:**", courses)
        st.write("**Email Address:**", email)