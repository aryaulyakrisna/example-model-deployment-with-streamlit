import streamlit as st
import joblib
import numpy as np

model = joblib.load("models/house_price_model.pkl")

st.title("Prediksi Harga Rumah dengan Joblib Model")
st.markdown("- Rumah yang diprediksi harus berada atau di sekitar jakarta")

total_lb = st.number_input("Luas Bangunan (m2)", min_value=0)
total_lt = st.number_input("Luas Tanah (m2)", min_value=0)
jumlah_kt = st.number_input("Jumlah Kamar Tidur", min_value=0, step=1)
jumlah_km = st.number_input("Jumlah Kamar Mandi", min_value=0, step=1)
garasi = st.number_input("Jumlah Garasi", min_value=0, step=1)

if st.button("Prediksi Harga"):
    features = np.array([[total_lb, total_lt, jumlah_kt, jumlah_km, garasi]])
    prediction = model.predict(features)
    st.write(f"Perkiraan Harga Rumah: Rp {int(prediction[0]*1000000):,}".replace(",", "."))