import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Cargar el modelo y los encoders
model = joblib.load("models/final_model.pkl")
make_encoder = joblib.load("encoders_scalers/make_encoder.pkl")
model_encoder = joblib.load("encoders_scalers/model_encoder.pkl")
mileage_scaler = joblib.load("encoders_scalers/mileage_scaler.pkl")
kmeans = joblib.load("models/kmeans_model.pkl")  # Cargar el modelo de clustering

# Cargar datasets
processed_data = pd.read_csv("data/semiprocessed_data.csv")
raw_data = pd.read_csv("data/raw_data.csv")

# Crear mapas inversos para marcas y modelos
make_map = dict(zip(raw_data['Make'], processed_data['Make']))
model_map = dict(zip(raw_data['Model'], processed_data['Model']))

# Opciones de selección
make_options = list(make_map.keys())
model_options = list(model_map.keys())

# Encabezado principal con formato
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #FF5733;">🚗 Predicción de Precios de Vehículos 🚗</h1>
        <p style="font-size: 18px; color: #555;">Ingrese los datos del vehículo para predecir su precio estimado:</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Entrada del usuario
st.subheader("Datos del Vehículo")
make = st.selectbox("Marca del carro (por ejemplo: Ford, BMW, Toyota)", make_options)
model_option = st.selectbox("Modelo del carro (por ejemplo: Focus, Series 3, Corolla)", model_options)
mileage = st.slider("Kilometraje (km)", 0, 300000, 100000)
year = st.number_input("Año del vehículo", min_value=1980, max_value=2023, step=1, value=2015)

# Validar entradas y convertir a códigos
if make not in make_map or model_option not in model_map:
    st.error("❌ La marca o modelo ingresados no están en la base de datos. Intente nuevamente.")
    st.stop()

encoded_make = make_map[make]
encoded_model = model_map[model_option]

# Escalar el kilometraje
scaled_mileage = mileage_scaler.transform([[mileage]])[0][0]

# Predecir el cluster
cluster_input = np.array([[year, scaled_mileage, encoded_make, encoded_model]])
predicted_cluster = kmeans.predict(cluster_input)[0]

# Crear el array de entrada para la predicción final
input_data = np.array([[year, scaled_mileage, encoded_make, encoded_model, predicted_cluster]])

# Botón para predecir
st.subheader("Resultado de la Predicción")
if st.button("Predecir Precio"):
    try:
        predicted_price = model.predict(input_data)[0]
        st.success(f"💰 El precio estimado del vehículo es: ${predicted_price:,.2f}")
    except Exception as e:
        st.error(f"❌ Error en la predicción: {e}")

# Footer
st.markdown(
    """
    <hr>
    <div style="text-align: center;">
        <p style="color: #888;">Desarrollado por <b>Sergio Tech</b></p>
    </div>
    """,
    unsafe_allow_html=True,
)


















