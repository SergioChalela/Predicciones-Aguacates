# Proyecto de Predicción de Precios de Vehículos 🚗

Este proyecto tiene como objetivo construir un modelo de Machine Learning capaz de predecir el precio de un vehículo basado en sus características (año, kilometraje, marca, modelo). Incluye técnicas supervisadas y no supervisadas para mejorar la precisión y robustez del modelo.

---

## Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Requisitos](#requisitos)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Preparación de los Datos](#preparación-de-los-datos)
5. [Modelos Probados](#modelos-probados)
6. [Modelo Final](#modelo-final)
7. [Resultados](#resultados)
8. [Limitaciones y Mejoras Futuras](#limitaciones-y-mejoras-futuras)

---

## Descripción del Proyecto

Este proyecto se centra en:
- Limpiar y transformar datos de un dataset de 852,122 registros.
- Aplicar técnicas de clustering (KMeans) para segmentar datos en grupos homogéneos.
- Probar varios modelos supervisados para seleccionar el más adecuado.
- Generar un modelo final con KNN, optimizado para ofrecer precisión y eficiencia.

---

## Requisitos

### Librerías necesarias:
- Python 3.8 o superior
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `yaml`
- `joblib`

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt

📂 Predicciones-Precios-Carros
├── 📂 data
│   ├── raw_data.csv
│   ├── semiprocessed_data.csv
│   ├── processed_data.csv
│   ├── train.csv
│   ├── test.csv
├── 📂 models
│   ├── final_model.pkl
├── 📂 encoders_scalers
│   ├── make_encoder.pkl
│   ├── model_encoder.pkl
│   ├── mileage_scaler.pkl
├── 📂 src
│   ├── data_processing.py
│   ├── training.py
│   ├── evaluation.py
├── 📂 notebooks
│   ├── Exploración.ipynb
│   ├── ModelosSupervisados.ipynb
│   ├── Clustering.ipynb
│   ├── RedesNeuronales.ipynb
├── README.md







