import shap
from . import prediction
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging
logger = logging.getLogger(__name__)


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
    #shap.summary_plot(shap_values,X_value, feature_names=feature_names)
    shap.plots.waterfall(
        shap.Explanation(
            values=shap_values[0],
            base_values=explainer.expected_value,
            data=X_value[0],
            feature_names=feature_names
        )
    )
    return shap_values

def get_shap_waterfall_figure(input_data, max_display=20):
    """
    Generate a SHAP waterfall plot and return the Matplotlib figure.
    
    Parameters:
    - input_data: dict, input data for which to compute SHAP values
    - max_display: max features to display in the plot (default 20)
    
    Returns:
    - Matplotlib figure object
    """
    # Calculate figure height dynamically (0.35 inch per feature, capped)


    if not isinstance(input_data, dict):
        logger.error("Input data must be a dictionary.")
        raise ValueError("Input data must be a dictionary.")
        
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
    shap_value = explainer.shap_values(X_value)
    feature_names = preprocessor.get_feature_names_out()

    N = min(len(shap_value), max_display)
    height = max(4, min(0.35 * N, 20))

    fig = plt.figure(figsize=(8, height))

    #shap.summary_plot(shap_values,X_value, feature_names=feature_names)
    shap.plots.waterfall(
        shap.Explanation(
            values=shap_value[0],
            base_values=explainer.expected_value,
            data=X_value[0],
            feature_names=feature_names
        ),show = False
    )
    plt.tight_layout()
    return fig