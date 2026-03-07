import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="MarketMind", layout="wide")

# Function to load HTML file
def load_html(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

st.title("MarketMind - AI Sales & Marketing Intelligence Platform")

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Login", "Registration", "Dashboard"]
)

if page == "Home":
    html(load_html("homepage.html"), height=900)

elif page == "Login":
    html(load_html("login.html"), height=900)

elif page == "Registration":
    html(load_html("registration.html"), height=900)

elif page == "Dashboard":
    html(load_html("dashboard.html"), height=900)