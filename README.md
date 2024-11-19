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


---

## Preparación de los Datos

### Dataset Original
El dataset incluye las siguientes columnas principales:
- **Price**: Precio del vehículo (variable objetivo).
- **Year**: Año del vehículo.
- **Mileage**: Kilometraje del vehículo.
- **Make** y **Model**: Marca y modelo del vehículo.
- **City**, **State**, **Vin**: Información no relevante eliminada.

### Transformaciones
1. Eliminación de columnas irrelevantes: `City`, `State`, `Vin`.
2. Codificación:
   - `Make` y `Model` utilizando `LabelEncoder`.
3. Escalado:
   - `Mileage` escalado con `MinMaxScaler`.
4. Generación de clusters con KMeans:
   - **Número óptimo de clusters (k): 4.**

---

## Modelos Probados

**Modelos supervisados:**
1. **Linear Regression**
   - MSE: 1.4598e+08
   - R²: 0.205
2. **Decision Tree Regressor**
   - MSE (optimizado): 3.46e+07
   - R²: 0.811
3. **Random Forest Regressor**
   - MSE: 1.99e+07
   - R²: 0.891
4. **KNN**
   - MSE: 1.89e+07
   - R²: 0.897
5. **Gradient Boosting**
   - MSE: 4.41e+07
   - R²: 0.759

**No supervisado:**
- **KMeans Clustering**
   - Identificación de 4 clusters para segmentación del dataset.

**Modelo final seleccionado:** KNN, con preprocessing adicional usando clustering KMeans.

---

## Modelo Final

### Detalles del modelo seleccionado
- **Modelo:** K-Nearest Neighbors (KNN).
- **Hiperparámetros:**
  - n_neighbors: 5
  - metric: Minkowski
  - weights: uniform
- **Preprocesamiento:**
  - Clustering: KMeans con 4 clusters.
  - Escalado: MinMaxScaler.
  - Codificación: LabelEncoder.
- **Rendimiento:**
  - MSE: 1.89e+07
  - MAE: 2368.78
  - R²: 0.897

---

## Resultados

**Gráficos Generados:**
- Distribución de los precios iniciales y por cluster.
- Relación entre precio y kilometraje.
- Representación 3D del clustering aplicado al dataset.

---

## Limitaciones y Próximos Pasos

### Limitaciones
- El modelo se basa en datos históricos y no tiene en cuenta variables externas como fluctuaciones económicas.
- La inclusión de clusters puede no siempre mejorar el rendimiento en todos los contextos.

### Mejoras Futuras
1. Añadir más datos relevantes (tipo de combustible, condiciones del mercado).
2. Implementar modelos más avanzados (XGBoost, redes neuronales con tuning).
3. Crear una API para integrar el modelo en aplicaciones web o móviles.
4. Evaluar la robustez del modelo en diferentes mercados geográficos.

---

¡Gracias por leer!








