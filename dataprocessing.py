import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(source_file_name, output_name):
    filepath="data/raw/"+source_file_name
    logger.info(f"Chargement du fichier a l'emplacement : {filepath}")
    file = pd.read_csv(filepath, sep= "|" )
    logger.info(f"Fichier chargé")
    file = file.rename(columns= {"Type local":"Type_local", "Surface reelle bati":'Surface_reelle_bati', "Nombre pieces principales": "Nombre_pieces_principales", "Surface terrain":"Surface_terrain", "Valeur fonciere":"Valeur_fonciere" })
    
    # Convertir les colonnes numériques (virgule française -> point)
    numeric_columns = ['Surface_reelle_bati', 'Surface_terrain', 'Nombre_pieces_principales', 'Valeur_fonciere']
    
    for col in numeric_columns:
        if col in file.columns:
            file[col] = file[col].astype(str).str.replace(',', '.').astype(float, errors='raise')
    
    # Supprimer les lignes avec NaN
    file = file.dropna(subset=['Valeur_fonciere'])
    
    logger.info(f"Données nettoyées: {len(file)} lignes")
    
    outputpath ="data/processed/"+ output_name
    file.to_csv(outputpath, index=False)
    logger.info(f"Fichier Enregistrer dans {outputpath}")


if __name__=="__main__":
    process_data("brut2025.txt", "2025.csv")