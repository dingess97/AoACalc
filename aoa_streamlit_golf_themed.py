
import streamlit as st

st.set_page_config(
    page_title="AoA Calculator",
    page_icon="favicon.ico",
    layout="centered"
)

st.markdown("""
    <link rel="apple-touch-icon" sizes="180x180" href="static/apple-touch-icon.png">
    <link rel="apple-touch-icon-precomposed" href="static/apple-touch-icon.png">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
""", unsafe_allow_html=True)


import pandas as pd
from skops.io import load

# Load model
model = load("aoa_model.skops")

# Theme and UI
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Golf_course_view.jpg/1280px-Golf_course_view.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("## ⛳ **Golf Ball Flight Predictor**")
st.markdown("_Estimate your Angle of Attack based on ball speed, launch angle, and spin rate._")

ball_speed = st.slider("🏌️ Ball Speed (mph)", 150, 200, 165)
ball_speed_input = st.number_input("Or type Ball Speed", 150, 200, value=ball_speed, key="bs")
ball_speed = ball_speed_input

launch_angle = st.slider("🎯 Launch Angle (°)", 2.0, 18.0, 14.0, step=0.1)
launch_angle_input = st.number_input("Or type Launch Angle", 2.0, 18.0, value=launch_angle, step=0.1, key="la")
launch_angle = launch_angle_input

spin_rate = st.slider("🔁 Spin Rate (rpm)", 1500, 3600, 1950)
spin_rate_input = st.number_input("Or type Spin Rate", 1500, 3600, value=spin_rate, key="sr")
spin_rate = spin_rate_input

if st.button("🎬 Predict AoA"):
    input_df = pd.DataFrame([[ball_speed, launch_angle, spin_rate]],
                            columns=["BallSpeed", "LaunchAngle", "SpinRate"])
    prediction = model.predict(input_df)[0]
    st.success(f"🎉 Estimated Angle of Attack: **{prediction:.2f}°**")

with st.expander("💡 Pro Tip"):
    st.markdown("Optimize your launch for distance by balancing higher launch angles with lower spin.")
