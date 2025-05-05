
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('aoa_model_py312.pkl')

# Prediction function
def predict_aoa(ball_speed, launch_angle, spin_rate):
    input_data = pd.DataFrame([[ball_speed, launch_angle, spin_rate]],
                              columns=["BallSpeed", "LaunchAngle", "SpinRate"])
    return model.predict(input_data)[0]

# Example usage
if __name__ == "__main__":
    example = predict_aoa(165, 14.0, 1950)
    print(f"Predicted AoA: {example:.2f} degrees")
