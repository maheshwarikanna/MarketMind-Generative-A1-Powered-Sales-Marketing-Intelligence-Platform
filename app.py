import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
from streamlit.components.v1 import html

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="MarketMind",
    layout="wide"
)

# -----------------------------
# Load HTML Function
# -----------------------------
def load_html(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

# -----------------------------
# Simple User Storage
# -----------------------------
USER_FILE = "users.json"

if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

# -----------------------------
# Session State
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("MarketMind")

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Register",
        "Login",
        "Dashboard",
        "Market Analysis",
        "AI Content Generator"
    ]
)

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "Home":

    html(load_html("homepage.html"), height=800)


# -----------------------------
# REGISTER
# -----------------------------
elif page == "Register":

    st.title("Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Register"):

        users = load_users()

        if password != confirm:
            st.error("Passwords do not match")

        elif username in users:
            st.error("User already exists")

        else:
            users[username] = {
                "email": email,
                "password": password
            }

            save_users(users)

            st.success("Registration Successful")


# -----------------------------
# LOGIN
# -----------------------------
elif page == "Login":

    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        users = load_users()

        if username in users and users[username]["password"] == password:
            st.session_state.logged_in = True
            st.success("Login Successful")

        else:
            st.error("Invalid credentials")


# -----------------------------
# DASHBOARD
# -----------------------------
elif page == "Dashboard":

    if not st.session_state.logged_in:
        st.warning("Please login first")
        st.stop()

    st.title("Sales Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sales", "$120,000")
    col2.metric("Customers", "3,200")
    col3.metric("Growth", "18%")

    data = pd.DataFrame({
        "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
        "Sales": [20000,30000,25000,40000,45000,50000]
    })

    fig = px.line(data, x="Month", y="Sales", title="Sales Trend")

    st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# MARKET ANALYSIS
# -----------------------------
elif page == "Market Analysis":

    if not st.session_state.logged_in:
        st.warning("Please login first")
        st.stop()

    st.title("Market Analysis")

    data = pd.DataFrame({
        "Product":["A","B","C","D"],
        "Sales":[400,600,300,500]
    })

    fig = px.bar(data, x="Product", y="Sales", title="Product Sales Comparison")

    st.plotly_chart(fig, use_container_width=True)

    customers = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr"],
        "Customers":[100,150,200,280]
    })

    fig2 = px.line(customers, x="Month", y="Customers", title="Customer Growth")

    st.plotly_chart(fig2, use_container_width=True)


# -----------------------------
# AI CONTENT GENERATOR
# -----------------------------
elif page == "AI Content Generator":

    if not st.session_state.logged_in:
        st.warning("Please login first")
        st.stop()

    st.title("AI Marketing Content Generator")

    product = st.text_input("Product Name")
    audience = st.text_input("Target Audience")

    platform = st.selectbox(
        "Platform",
        ["Instagram","LinkedIn","Email","Facebook"]
    )

    if st.button("Generate Content"):

        caption = f"""
🔥 Introducing {product}!

Perfect for {audience}.

Discover the future of innovation today.

#Innovation #Marketing #AI
"""

        ad_copy = f"""
Upgrade your experience with {product}.
Designed specifically for {audience}.
Try it today and transform your workflow.
"""

        st.subheader("Marketing Caption")
        st.write(caption)

        st.subheader("Ad Copy")
        st.write(ad_copy)
