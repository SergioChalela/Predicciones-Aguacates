import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import os

def evaluate_models(test_path, models_dir):
    # Cargar datos de prueba
    X_test = pd.read_csv(test_path)
    
    # Variables
    y_test = X_test["Price"]
    X_test = X_test.drop("Price", axis=1)
    
    # Obtener la lista de modelos
    model_files = [f for f in os.listdir(models_dir) if f.endswith(".pkl")]
    
    results = []
    for model_file in model_files:
        # Cargar modelo
        model_path = os.path.join(models_dir, model_file)
        model = joblib.load(model_path)
        
        # Predicciones
        y_pred = model.predict(X_test)
        
        # Métricas
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results.append({
            "Modelo": model_file.replace("_model.pkl", ""),
            "MSE": mse,
            "MAE": mae,
            "R2": r2
        })
    
    # Mostrar resultados
    results_df = pd.DataFrame(results)
    print(results_df)
    return results_df

if __name__ == "__main__":
    evaluate_models("data/test/test_data.csv", "models")
