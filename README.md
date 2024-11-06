# Proyecto: Análisis y Predicción de Salarios en Data Science

## Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar un análisis detallado y un modelo predictivo para estimar los salarios de los profesionales en el campo de Data Science, basándonos en diversas características, como la experiencia, la ubicación, el nivel de educación, y el tipo de empresa. Utilizaremos el **dataset de Data Science Salaries 2024**, que contiene información sobre los salarios de diferentes roles de Data Science en distintos países. Este proyecto es ideal para aprender a aplicar técnicas de Machine Learning, en particular para problemas de regresión y análisis comparativo.

## Objetivo
El objetivo principal es construir un modelo que prediga con precisión el salario de un profesional de Data Science en función de sus características personales y laborales. Además, realizaremos un análisis exploratorio para entender los factores más influyentes en la determinación de los salarios.

## Dataset
- **Nombre:** Data Science Salaries 2024
- **Fuente:** Datos proporcionados en formato CSV
- **Descripción de las Características:**
  - `work_year`: Año en el que se reportó el salario.
  - `experience_level`: Nivel de experiencia del profesional (Junior, Middle, Senior, etc.).
  - `employment_type`: Tipo de empleo (Tiempo completo, Freelance, etc.).
  - `job_title`: Título del trabajo (Data Scientist, Data Engineer, etc.).
  - `salary`: Salario bruto anual.
  - `salary_currency`: Moneda en la que se reporta el salario.
  - `employee_residence`: País de residencia del empleado.
  - `remote_ratio`: Porcentaje de trabajo remoto.
  - `company_location`: Ubicación de la empresa.
  - `company_size`: Tamaño de la empresa (Pequeña, Mediana, Grande).

## Pasos del Proyecto
1. **Análisis Exploratorio de Datos (EDA):** Realizar un análisis detallado de las variables disponibles para entender mejor el dataset. Esto incluirá visualizaciones de la distribución de los salarios, análisis de los factores que afectan el salario, y detección de patrones relevantes.
2. **Limpieza y Preprocesamiento de Datos:** Tratar valores nulos, codificar variables categóricas, y normalizar/estandarizar las variables según sea necesario.
3. **Ingeniería de Características:** Crear nuevas variables relevantes que puedan mejorar el rendimiento del modelo. Por ejemplo, categorizar el nivel de experiencia o agrupar países por regiones económicas.
4. **Modelado:** Comenzar con un modelo de regresión lineal para establecer una base y luego probar modelos más complejos, como **Random Forest** o **XGBoost**, para mejorar el rendimiento.
5. **Evaluación del Modelo:** Utilizar métricas como **RMSE** (Root Mean Square Error) y **R²** para evaluar la calidad de las predicciones y ajustar el modelo según sea necesario.
6. **Implementación con Streamlit:** Crear una aplicación sencilla en **Streamlit** para que los usuarios puedan ingresar características de un profesional y obtener una predicción del salario.

## Tecnologías y Herramientas
- **Python:** Lenguaje principal para el análisis y modelado.
- **Bibliotecas:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `streamlit`.
- **Jupyter Notebook:** Para el desarrollo del análisis exploratorio y del modelo.
- **Streamlit:** Para construir una aplicación interactiva que permita a los usuarios ver predicciones en tiempo real.

## Resultados Esperados
- Un modelo que pueda predecir el salario de un profesional de Data Science con una buena precisión, ayudando a visualizar los factores más importantes que afectan el salario.
- Visualizaciones que muestren la relación entre las características del profesional y el salario, ayudando a entender cómo se valoran ciertos aspectos en la industria de Data Science.
- Una aplicación web sencilla donde el usuario pueda ingresar las características de un profesional y obtener una predicción del salario estimado.

## Contribución
Cualquier colaboración es bienvenida. Puedes contribuir mediante:
- Propuestas de mejora en la selección y el ajuste de los modelos.
- Sugerencias para la ingeniería de características.
- Mejora de la aplicación de Streamlit.

## Contacto
Para preguntas, comentarios o sugerencias, puedes contactarme a través de mi perfil de GitHub o directamente por correo electrónico.

## Código de los Gráficos del Análisis Exploratorio de Datos (EDA)

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")

# 1. Descripción de las columnas y resumen estadístico
data_description = data.describe()

# 2. Visualización de la distribución de la variable objetivo (salario)
plt.figure(figsize=(10, 6))
sns.histplot(data['salary'], kde=True, color='blue')
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='x')
plt.title('Distribución de los Salarios de Data Science')
plt.xlabel('Salario Bruto Anual')
plt.ylabel('Frecuencia')
plt.show()

# 3. Matriz de correlación para ver relaciones entre variables numéricas
# Seleccionar solo las columnas numéricas para la matriz de correlación
numerical_data = data.select_dtypes(include=['float64', 'int64'])

# Crear la matriz de correlación
plt.figure(figsize=(12, 8))
correlation_matrix = numerical_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlación entre las Variables Numéricas')
plt.show()

# 4. Visualización de la relación entre experiencia y salario
plt.figure(figsize=(10, 6))
sns.boxplot(x='experience_level', y='salary', data=data)
plt.title('Relación entre Nivel de Experiencia y Salario')
plt.xlabel('Nivel de Experiencia')
plt.ylabel('Salario Bruto Anual')
plt.show()

# 5. Conteo de las categorías de residencia del empleado (employee_residence)
plt.figure(figsize=(8, 5))
sns.countplot(x='employee_residence', data=data, palette='viridis')
plt.title('Distribución por País de Residencia del Empleado')
plt.xlabel('País de Residencia')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.show()
