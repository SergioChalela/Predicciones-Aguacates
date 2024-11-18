import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import os

def process_data(raw_data_path, processed_data_path):
    # Cargar los datos
    df = pd.read_csv(raw_data_path)
    
    # Transformaciones
    make_encoder = LabelEncoder()
    model_encoder = LabelEncoder()
    mileage_scaler = MinMaxScaler()
    
    df["Make"] = make_encoder.fit_transform(df["Make"])
    df["Model"] = model_encoder.fit_transform(df["Model"])
    df["Mileage"] = mileage_scaler.fit_transform(df[["Mileage"]])
    
    # Guardar los datos procesados
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
    df.to_csv(processed_data_path, index=False)
    
    print(f"Datos procesados guardados en: {processed_data_path}")
    return make_encoder, model_encoder, mileage_scaler

if __name__ == "__main__":
    process_data("data/raw/raw_data.csv", "data/processed/processed_data.csv")
