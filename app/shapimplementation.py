import shap
from . import prediction
import numpy as np
import pandas as pd

def compute_shap_values(input_data):
    if isinstance(input_data, list):
        dataframe= pd.DataFrame(input_data)
    else:
        dataframe= pd.DataFrame([input_data])
    pipeline = prediction.get_model()
    if pipeline is None:
        raise ValueError("Le modèle n'a pas pu être chargé.")
    
    preprocessor = pipeline.named_steps["preprocessor"]

    model_steps = pipeline.named_steps["regressor"]
    # Utiliser TreeExplainer pour les modèles basés sur des arbres
    explainer = shap.TreeExplainer(model_steps)
    
    #input_data = np.array(input_data).reshape(1, -1)
    # Calculer les valeurs SHAP
    X_value = preprocessor.transform(dataframe)
    shap_values = explainer.shap_values(X_value)
    feature_names = preprocessor.get_feature_names_out()
    shap.summary_plot(shap_values,X_value, feature_names=feature_names)
    return shap_values