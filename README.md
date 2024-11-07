# Proyecto: Análisis y Predicción del Precio de Aguacates

## Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar un análisis detallado y un modelo predictivo para estimar el precio promedio de los aguacates, basándonos en diversas características, como el tipo de aguacate, el volumen de ventas, la región y otros factores relevantes. Utilizaremos un **dataset de ventas de aguacates**, que contiene información detallada sobre precios, volúmenes y características del producto a lo largo del tiempo. Este proyecto es ideal para aprender a aplicar técnicas de Machine Learning, particularmente en problemas de regresión y análisis temporal.

## Objetivo
El objetivo principal es construir un modelo que prediga con precisión el **precio promedio** (`AveragePrice`) de un aguacate en función de las características proporcionadas en el dataset. Además, realizaremos un **análisis exploratorio de datos (EDA)** para comprender mejor las tendencias, patrones y factores más influyentes en la determinación del precio.

## Dataset
- **Nombre:** Avocado Prices Dataset
- **Fuente:** Kaggle (avocado.csv)
- **Descripción de las Características:**
  - `Date`: Fecha de registro de los precios.
  - `AveragePrice`: Precio promedio de un aguacate.
  - `Total Volume`: Volumen total de aguacates vendidos.
  - `4046`, `4225`, `4770`: Volúmenes de ventas de diferentes tipos de aguacates.
  - `Total Bags`, `Small Bags`, `Large Bags`, `XLarge Bags`: Tipos y volúmenes de bolsas de aguacates vendidos.
  - `type`: Tipo de aguacate (convencional u orgánico).
  - `year`: Año de la observación.
  - `region`: Región donde se registraron las ventas.

## Pasos del Proyecto
1. **Análisis Exploratorio de Datos (EDA):** Realizar un análisis detallado de las variables disponibles para entender mejor el dataset. Esto incluirá visualizaciones de la distribución de los precios, análisis de patrones temporales y diferencias entre tipos de aguacates.
2. **Limpieza y Preprocesamiento de Datos:** Eliminar columnas innecesarias (`Unnamed: 0`), codificar variables categóricas (`type` y `region`) y crear nuevas características a partir de la columna `Date`.
3. **Ingeniería de Características:** Crear nuevas variables relevantes que puedan mejorar el rendimiento del modelo, como el mes o el día de la semana a partir de la columna `Date`.
4. **Modelado Baseline:** Comenzar con un modelo de **Regresión Lineal** simple para evaluar la viabilidad de un modelo predictivo con el dataset disponible.
5. **Evaluación del Modelo:** Utilizar métricas como **RMSE** (Root Mean Squared Error) y **R²** para evaluar la calidad de las predicciones y determinar la viabilidad del proyecto para el análisis predictivo.

## Tecnologías y Herramientas
- **Python:** Lenguaje principal para el análisis y modelado.
- **Bibliotecas:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`.
- **Jupyter Notebook:** Para el desarrollo del análisis exploratorio y del modelo.

## Resultados Esperados
- Un **análisis exploratorio de datos** que muestre la distribución de los precios de los aguacates y las tendencias a lo largo del tiempo, así como las diferencias de precios según el tipo de aguacate y la región.
- Un **modelo baseline de regresión lineal** que sea capaz de predecir el precio promedio de los aguacates y evaluar si hay potencial para seguir mejorando el modelo.
- Una conclusión sobre la **viabilidad** del modelo predictivo y las oportunidades para mejorar su rendimiento mediante técnicas más avanzadas o ingeniería de características.

## Contribución
Cualquier colaboración es bienvenida. Puedes contribuir mediante:
- Propuestas de mejora en la selección y el ajuste de los modelos.
- Sugerencias para la ingeniería de características.
- Mejora en las visualizaciones del análisis exploratorio.

## Contacto
Para preguntas, comentarios o sugerencias, puedes contactarme a través de mi perfil de GitHub o directamente por correo electrónico.

## Código de los Gráficos del Análisis Exploratorio de Datos (EDA)

```python
import matplotlib.pyplot as plt
import
