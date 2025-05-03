
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("aoa_model.pkl")

# Background image and styling
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Golf_course_view.jpg/1280px-Golf_course_view.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    .big-font {
        font-size:30px !important;
        color: #0B3D0B;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("## ⛳ **Golf Ball Flight Predictor**")
st.markdown("_Estimate your Angle of Attack based on shot metrics like ball speed, launch angle, and spin rate._")

# Ball Speed
st.write("### 🏌️ Ball Speed (mph)")
ball_speed = st.slider("Select Ball Speed", 150, 200, 165, key="ball_slider")
ball_speed_input = st.number_input("Or type Ball Speed", 150, 200, value=ball_speed, key="ball_input")
ball_speed = ball_speed_input

# Launch Angle
st.write("### 🎯 Launch Angle (°)")
launch_angle = st.slider("Select Launch Angle", 2.0, 18.0, 14.0, step=0.1, key="angle_slider")
launch_angle_input = st.number_input("Or type Launch Angle", 2.0, 18.0, value=launch_angle, step=0.1, key="angle_input")
launch_angle = launch_angle_input

# Spin Rate
st.write("### 🔁 Spin Rate (rpm)")
spin_rate = st.slider("Select Spin Rate", 1500, 3600, 1950, key="spin_slider")
spin_rate_input = st.number_input("Or type Spin Rate", 1500, 3600, value=spin_rate, key="spin_input")
spin_rate = spin_rate_input

# Prediction Button
if st.button("🎬 Predict AoA"):
    input_data = pd.DataFrame([[ball_speed, launch_angle, spin_rate]],
                              columns=["BallSpeed", "LaunchAngle", "SpinRate"])
    aoa = model.predict(input_data)[0]
    st.success(f"🎉 Predicted Angle of Attack: **{aoa:.2f}°**")

# Pro tip section
with st.expander("💡 Pro Tip"):
    st.markdown("Higher launch angles and lower spin rates often result in longer drives. Try optimizing your AoA for ideal launch conditions!")
