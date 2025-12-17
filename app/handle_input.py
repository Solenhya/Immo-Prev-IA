# Essaie de programme qui récupere les parametres d'un modèle et les links a une liste de transformation possible


from mlflow.types import DataType
from . import prediction
import logging

logger = logging.getLogger(__name__)
#Basique genere l'UI avec label = id et transmets basiquement
def get_parameters_dynamique():
    info = prediction.get_model_info()
    logger.info(f"Info du modèle récupéré: {info}")
    signature_inputs = info.signature.inputs
    logger.info(f"Chargement de la signature depuis {signature_inputs}")
    retour = []
    for col in signature_inputs:
        logger.debug(f"Donnée extraite:{col.name}")
        ajout = {}
        ajout["label"]=col.name.replace("_"," ")
        ajout["id"]=col.name
        ajout["type"]="unknow"
        if(col.type==DataType.double):
            ajout["type"]="number"
        if(col.type==DataType.string):
            ajout["type"]="text"
        retour.append(ajout)
    return retour