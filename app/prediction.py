import mlflow.sklearn
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model = None
model_info = None
commande_load = f"models:/model_test/latest"
mlflow.set_tracking_uri(uri='http://localhost:5000')
logger.debug(f"connection a {mlflow.get_tracking_uri()} et récuperation de {commande_load}")
def get_model():
    global model
    if model is None:
        try:
            logger.info(f"Chargement du modèle depuis MLflow avec la commande: {commande_load}")
            model = mlflow.sklearn.load_model(commande_load)
            logger.info(f"Modèle chargé à l'adresse {commande_load}")
        except:
            return None
    return model

def get_model_info():
    global model_info
    if model_info is None:
        try:
            logger.info(f"Chargement des informations du modèle depuis MLflow avec la commande: {commande_load}")
            model_info = mlflow.models.get_model_info(commande_load)
            logger.info(f"Information du modèle chargé à l'adresse {commande_load}")
        except:
            default = { "signature":{
                "input":[]
            }
            }
            return default
    return model_info


def model_predict(features:dict):
    model = get_model()
    dataframe= pd.DataFrame([features])
    prediction = model.predict(dataframe)
    logger.info(f"Prediction effectuer prix estimer : {prediction}")
    return prediction
    

if __name__ == "__main__":
    sample_features = {
        'Surface_reelle_bati': 80,
        'Surface_terrain': 0,
        'Nombre_pieces_principales': 3,
        'Type_local': 'Appartement',
    }
    result = model_predict(sample_features)
    print(result)


