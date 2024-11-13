import streamlit as st
import joblib
import pandas as pd

# Cargar el modelo y los transformadores
make_encoder = joblib.load("make_encoder.pkl")
model_encoder = joblib.load("model_encoder.pkl")
mileage_scaler = joblib.load("mileage_scaler.pkl")
model = joblib.load("decision_tree_model.pkl")

# Título de la aplicación
st.title("Predicción de Precios de Carros")

# Entradas del usuario
make = st.selectbox("Marca del carro", make_encoder.classes_)
model_choice = st.selectbox("Modelo del carro", model_encoder.classes_)
mileage = st.number_input("Kilometraje", min_value=0)
age = st.number_input("Edad del vehículo (en años)", min_value=1)

# Transformar las entradas del usuario
make_encoded = make_encoder.transform([make])[0]
model_encoded = model_encoder.transform([model_choice])[0]
mileage_scaled = mileage_scaler.transform([[mileage]])[0][0]

# Crear DataFrame con los datos transformados
input_data = pd.DataFrame([[mileage_scaled, age, make_encoded, model_encoded]], 
                          columns=['Mileage', 'Age', 'Make', 'Model'])

# Predicción
if st.button("Predecir Precio"):
    predicted_log_price = model.predict(input_data)[0]
    predicted_price = round(10 ** predicted_log_price, 2)  # Convertir el precio de logarítmico a real
    st.write(f"Precio Predicho: ${predicted_price:,.2f}")
