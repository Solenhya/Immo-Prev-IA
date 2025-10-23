import mlflow.sklearn
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

model = None
def get_model():
    global model
    if model is None:
        run_id = "dd22668f957547749847199709266af8"

        commande_load = f"models:/model_test/latest"
        mlflow.set_tracking_uri(uri='http://localhost:5000')
        logger.debug(mlflow.get_tracking_uri())
        logger.info(f"Chargement du modèle depuis MLflow avec le run_id: {run_id}")
        model = mlflow.sklearn.load_model(commande_load)
        logger.info(f"Modèle chargé à l'adresse {commande_load}")
    return model


def model_predict(features:dict):
    nombre_piece = features.get("Nombre_pieces_principales", 0)
    model = get_model()
    dataframe= pd.DataFrame([features])
    prediction = model.predict(dataframe)
    return f'Resultat predicition : {prediction}'

if __name__ == "__main__":
    sample_features = {
        'Surface_reelle_bati': 80,
        'Surface_terrain': 0,
        'Nombre_pieces_principales': 3,
        'Type_local': 'Appartement',
    }
    result = model_predict(sample_features)
    print(result)


