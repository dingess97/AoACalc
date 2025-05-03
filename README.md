
# ⛳ Golf Ball Flight Predictor (AoA)

This Streamlit web app predicts your **Angle of Attack (AoA)** using golf launch monitor metrics:  
**Ball Speed**, **Launch Angle**, and **Spin Rate**.

> Perfect for golf enthusiasts, coaches, and club fitters who want deeper insight into their swing dynamics.

---

## 📊 Features

- 🎛 Dual input: Use **sliders** or **manual entry** for each parameter  
- 🏌️‍♂️ Golf-themed UI with background and emojis  
- 🧠 Built with a trained **Random Forest Regressor**  
- 📱 **Mobile-friendly** (works great on phones/tablets)  
- 💡 Expandable **Pro Tips** section with launch insights

---

## 🚀 How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/aoa-golf-app.git
   cd aoa-golf-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run aoa_streamlit_golf_themed.py
   ```

---

## 🌐 How to Deploy on Streamlit Cloud

1. Push this folder to a public GitHub repo
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App**, select your repo
4. Set the main file to: `aoa_streamlit_golf_themed.py`
5. Click **Deploy**

Your live app will get a public URL!

---

## 📁 File Structure

```
.
├── aoa_streamlit_golf_themed.py   # Streamlit app
├── aoa_model_py312.pkl            # Trained ML model (Python 3.12 compatible)
├── requirements.txt               # Python dependencies
```

---

## 📬 Feedback

Have suggestions or want to contribute? Open an issue or submit a pull request. Let's optimize your golf swing together! 🏌️‍♂️
