import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import joblib
import os

def process_data(input_path, output_path):
    # Cargar datos semiprocesados
    data = pd.read_csv(input_path)

    # Crear transformadores
    make_encoder = LabelEncoder()
    model_encoder = LabelEncoder()
    mileage_scaler = MinMaxScaler()

    # Aplicar transformaciones
    data['Make'] = make_encoder.fit_transform(data['Make'])
    data['Model'] = model_encoder.fit_transform(data['Model'])
    data['Mileage'] = mileage_scaler.fit_transform(data[['Mileage']])

    # Guardar transformadores para su uso posterior
    os.makedirs('encoders_scalers', exist_ok=True)
    joblib.dump(make_encoder, 'encoders_scalers/make_encoder.pkl')
    joblib.dump(model_encoder, 'encoders_scalers/model_encoder.pkl')
    joblib.dump(mileage_scaler, 'encoders_scalers/mileage_scaler.pkl')

    # Agregar clusters
    kmeans_model = joblib.load('models/kmeans_model.pkl')
    data['Cluster'] = kmeans_model.predict(data[['Year', 'Mileage', 'Make', 'Model']])

    # Guardar datos procesados
    os.makedirs(output_path, exist_ok=True)
    data.to_csv(f'{output_path}/semiprocessed_data.csv', index=False)

    # Dividir en train y test
    train = data.sample(frac=0.8, random_state=42)
    test = data.drop(train.index)

    train.to_csv(f'{output_path}/train.csv', index=False)
    test.to_csv(f'{output_path}/test.csv', index=False)

if __name__ == "__main__":
    process_data(input_path='data/semiprocessed_data.csv', output_path='data')

