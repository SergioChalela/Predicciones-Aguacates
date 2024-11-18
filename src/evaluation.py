import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Cargar el dataset de prueba
data = pd.read_csv('data/test.csv')

# Verificar si la columna Price está presente
if 'Price' not in data.columns:
    raise ValueError("La columna 'Price' no está presente en el dataset de prueba.")

# Separar las variables independientes (X) y la dependiente (y)
X_test = data.drop('Price', axis=1)
y_test = data['Price']

# Cargar el modelo entrenado
model = joblib.load('models/final_model.pkl')

# Realizar predicciones
y_pred = model.predict(X_test)

# Calcular métricas
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Mostrar métricas
print(f"MSE del modelo: {mse}")
print(f"MAE del modelo: {mae}")
print(f"R2 del modelo: {r2}")

