import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
from sklearn.compose import ColumnTransformer
import mlflow.sklearn, mlflow
from mlflow.models import infer_signature
import logging 

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

def get_data():
    file_path = "data/processed/2025.csv"
    nrows = 10000
    df = pd.read_csv(file_path, nrows=nrows )
    logger.info(f"📊 Données chargées: {len(df):,} lignes")
    return df

features = [
    'Surface_reelle_bati',
    'Surface_terrain',
    'Nombre_pieces_principales',
    'Type_local',
    
]

target = ['Valeur_fonciere']

def prepare_features(df):
    df = df[features + target]
    df = df[df['Type_local'].isin(['Maison', 'Appartement'])]
    "rempli les colonnes optionnelles pour ne pas supprimer les lignes"
    df['Surface_terrain'] = df['Surface_terrain'].fillna(0)
    df = df.dropna()
    logger.info(f"données préparées{df.shape}")
    return df

def train_model (experiment_name):
    df = prepare_features(get_data())
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = ['Type_local']  # Colonne catégorielle

    numeric_transformer = Pipeline(steps=[
            ('scaler', StandardScaler())])

    categorical_transformer = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])
    regressor = RandomForestRegressor(n_estimators=100, random_state=42)

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', regressor)
])

    mlflow.set_tracking_uri(uri='http://localhost:5000')
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
    # Exécuter la recherche sur les données d'entraînement
        model.fit(X_train, y_train)
        #grid_search.fit(dtrain)

        y_pred = model.predict(X_test)

        # Calcule le score R²
        r2 = r2_score(y_test, y_pred)

        # Enregistrer les paramètres et métriques
       
        mlflow.log_params({"df_shape": df.shape})
        mlflow.log_metric("r2_score", r2)  # Enregistre le score R²
        print(f"{r2=:.3f}")

        input_example = X_train.head(1)
        signature = infer_signature(X_train, model.predict(X_train))
        mlflow.sklearn.log_model(model, registered_model_name='model_test', signature=signature, input_example=input_example)


if __name__ == "__main__":
    train_model(experiment_name="test_mlflow_integration")      
