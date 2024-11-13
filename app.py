import streamlit as st
import numpy as np
import joblib

# Cargar el modelo y los encoders
model = joblib.load("decision_tree_model.pkl")
make_encoder = joblib.load("make_encoder.pkl")
model_encoder = joblib.load("model_encoder.pkl")
mileage_scaler = joblib.load("mileage_scaler.pkl")

st.title("Predicción de Precios de Carros")

# Selección de la marca y el modelo del carro usando las clases originales
make = st.selectbox("Marca del carro (codificado)", make_encoder.classes_)
model_option = st.selectbox("Modelo del carro (codificado)", model_encoder.classes_)

# Input de kilometraje y año del vehículo
mileage = st.slider("Kilometraje (escala 0-1)", 0.0, 1.0, 0.5)
year = st.number_input("Año del vehículo", min_value=1980, max_value=2023, step=1, value=2015)

# Transformar las entradas de marca y modelo a sus códigos numéricos
try:
    encoded_make = make_encoder.transform([make])[0]
    encoded_model = model_encoder.transform([model_option])[0]
except ValueError as e:
    st.error(f"Error al transformar los datos de entrada: {e}")
    st.stop()

# Escalar el kilometraje
scaled_mileage = mileage_scaler.transform([[mileage]])[0][0]

# Crear el array de entrada para la predicción
input_data = np.array([[year, scaled_mileage, encoded_make, encoded_model]])

# Botón para predecir el precio
if st.button("Predecir Precio"):
    try:
        predicted_price = model.predict(input_data)[0]
        st.write(f"El precio estimado del vehículo es: ${predicted_price:.2f}")
    except Exception as e:
        st.error(f"Error en la predicción: {e}")

