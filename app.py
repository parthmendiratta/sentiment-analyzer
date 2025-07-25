import streamlit as st
from sentiment_model import predict_sentiment

# Force light mode
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Set theme using CSS + Google Fonts
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #e3f2fd 0%, #ffffff 100%) !important;
            color: #222 !important;
        }

        .main-container {
            background-color: white;
            padding: 2.5rem;
            border-radius: 16px;
            box-shadow: 0 12px 32px rgba(0,0,0,0.07);
            max-width: 700px;
            margin: auto;
            margin-top: 3rem;
        }

        h1 {
            text-align: center;
            color: #d81b60;
            font-weight: 800;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .tagline {
            font-size: 1.1rem;
            color: #444;
            text-align: center;
            margin-bottom: 2rem;
        }

        .stTextArea textarea {
            background-color: #fff0f5;
            border: 1px solid #f8bbd0;
            font-size: 16px;
            border-radius: 10px;
            padding: 1rem;
            color: #333;
        }

        .stButton button {
            background-color: #d81b60;
            color: white;
            font-weight: bold;
            font-size: 16px;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            transition: 0.3s ease;
        }

        .stButton button:hover {
            background-color: #ad1457;
        }

        .result-box {
            font-size: 1.3rem;
            font-weight: bold;
            text-align: center;
            margin-top: 1.5rem;
            padding: 1rem;
            border-radius: 10px;
        }

        .positive {
            background-color: #e8f5e9;
            color: #2e7d32;
            border: 2px solid #66bb6a;
        }

        .negative {
            background-color: #ffebee;
            color: #c62828;
            border: 2px solid #ef5350;
        }
    </style>
""", unsafe_allow_html=True)

# App Layout
# st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<h1>🎬 Movie Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Transform emotion into actionable insight ✨</div>", unsafe_allow_html=True)

user_input = st.text_area("✍️ Write your movie review below:", height=200)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        prediction = predict_sentiment(user_input)
        if prediction == "Positive":
            st.markdown("<div class='result-box positive'>✅ It's a Positive Review! 😊</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-box negative'>❌ It's a Negative Review. 😠</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
