import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import joblib

# Cargar datos procesados
data = pd.read_csv('data/semiprocessed_data.csv')

# Dividir en características y objetivo
X = data.drop('Price', axis=1)
y = data['Price']

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar modelos
models = {
    "KNN": KNeighborsRegressor(n_neighbors=5),
    "DecisionTree": DecisionTreeRegressor(max_depth=20, min_samples_split=2, min_samples_leaf=5),
    "RandomForest": RandomForestRegressor(n_estimators=100, max_depth=20, random_state=42),
    "LinearRegression": LinearRegression(),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
}

# Entrenar y guardar cada modelo
for name, model in models.items():
    model.fit(X_train, y_train)
    joblib.dump(model, f'models/{name}_model.pkl')
    print(f"Modelo {name} entrenado y guardado.")

print("Todos los modelos han sido entrenados y guardados.")

