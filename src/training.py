import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_models(processed_data_path, train_path, test_path, models_dir):
    # Cargar los datos procesados
    df = pd.read_csv(processed_data_path)
    
    # Dividir en variables
    X = df.drop("Price", axis=1)
    y = df["Price"]
    
    # Dividir en train y test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Guardar train y test
    os.makedirs(os.path.dirname(train_path), exist_ok=True)
    X_train.to_csv(train_path, index=False)
    X_test.to_csv(test_path, index=False)
    
    # Crear modelos
    models = {
        "decision_tree": DecisionTreeRegressor(random_state=42),
        "random_forest": RandomForestRegressor(random_state=42, n_estimators=100),
        "gradient_boosting": GradientBoostingRegressor(random_state=42),
        "knn": KNeighborsRegressor(n_neighbors=5),
        "linear_regression": LinearRegression()
    }
    
    # Entrenar y guardar modelos
    os.makedirs(models_dir, exist_ok=True)
    for name, model in models.items():
        model.fit(X_train, y_train)
        model_path = os.path.join(models_dir, f"{name}_model.pkl")
        joblib.dump(model, model_path)
        print(f"Modelo {name} guardado en: {model_path}")

if __name__ == "__main__":
    train_models(
        "data/processed/processed_data.csv", 
        "data/train/train_data.csv", 
        "data/test/test_data.csv", 
        "models"
    )
