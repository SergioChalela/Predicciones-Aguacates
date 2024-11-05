# Proyecto: Predicción de Precios de Viviendas en California

## Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar un modelo predictivo para estimar los precios de las viviendas en California, basándose en diversas características de las propiedades y de las zonas en las que se encuentran. Utilizaremos el **dataset de California Housing Prices**, que contiene información sobre viviendas, incluyendo el precio medio, el ingreso promedio de la zona, el número de habitaciones, la densidad poblacional, y otras características importantes. Este proyecto es ideal para aprender a aplicar técnicas de Machine Learning, en particular para problemas de regresión.

## Objetivo
El objetivo principal es construir un modelo que prediga con precisión el precio de una vivienda en función de sus características. Este tipo de predicción es útil tanto para compradores, vendedores y desarrolladores de bienes raíces, ya que les proporciona una herramienta para evaluar el valor de mercado de una propiedad de forma rápida y precisa.

## Dataset
- **Nombre:** California Housing Prices
- **Fuente:** Kaggle
- **Enlace:** [California Housing Prices Dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
- **Descripción de las Características:**
  - `MedInc`: Ingreso medio de la zona.
  - `HouseAge`: Edad de la vivienda.
  - `AveRooms`: Promedio de habitaciones por hogar.
  - `AveBedrms`: Promedio de dormitorios por hogar.
  - `Population`: Población de la zona.
  - `AveOccup`: Promedio de ocupantes por hogar.
  - `Latitude` y `Longitude`: Ubicación geográfica de la propiedad.
  - `MedianHouseValue`: Valor medio de la vivienda (variable objetivo).

## Pasos del Proyecto
1. **Análisis Exploratorio de Datos (EDA):** Realizar un análisis detallado de las variables disponibles para entender mejor el dataset. Esto incluirá visualizaciones de las relaciones entre las diferentes variables y la detección de patrones.
2. **Limpieza y Preprocesamiento de Datos:** Tratar valores nulos, eliminar valores atípicos y normalizar/estandarizar las variables según sea necesario.
3. **Ingeniería de Características:** Crear nuevas variables relevantes que puedan mejorar el rendimiento del modelo. Por ejemplo, densidad de población o categorías basadas en la ubicación.
4. **Modelado:** Comenzar con un modelo de regresión lineal para establecer una base y luego probar modelos más complejos, como **Random Forest** o **XGBoost**, para mejorar el rendimiento.
5. **Evaluación del Modelo:** Utilizar métricas como **RMSE** (Root Mean Square Error) y **R²** para evaluar la calidad de las predicciones y ajustar el modelo según sea necesario.
6. **Implementación con Streamlit:** Crear una aplicación sencilla en **Streamlit** para que los usuarios puedan ingresar características de una vivienda y obtener una predicción del precio.

## Tecnologías y Herramientas
- **Python:** Lenguaje principal para el análisis y modelado.
- **Bibliotecas:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `streamlit`.
- **Jupyter Notebook:** Para el desarrollo del análisis exploratorio y del modelo.
- **Streamlit:** Para construir una aplicación interactiva que permita a los usuarios ver predicciones en tiempo real.

## Resultados Esperados
- Un modelo que pueda predecir el precio de una vivienda con una buena precisión, ayudando a visualizar los factores más importantes que afectan el precio.
- Visualizaciones que muestren la relación entre las características de las propiedades y los precios, ayudando a entender cómo se valoran las viviendas en diferentes zonas.
- Una aplicación web sencilla donde el usuario pueda ingresar las características de una vivienda y obtener una predicción del precio estimado.

## Contribución
Cualquier colaboración es bienvenida. Puedes contribuir mediante:
- Propuestas de mejora en la selección y el ajuste de los modelos.
- Sugerencias para la ingeniería de características.
- Mejora de la aplicación de Streamlit.

## Contacto
Para preguntas, comentarios o sugerencias, puedes contactarme a través de mi perfil de GitHub o directamente por correo electrónico.

