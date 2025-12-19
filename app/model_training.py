from . import dataAccess
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
from sklearn.compose import ColumnTransformer
import mlflow.sklearn, mlflow
from mlflow.models import infer_signature

def train_model(experiment_name,model_name,mlflow_uri):
    df = dataAccess.prepare_features(dataAccess.get_data())
    X = df[dataAccess.features]
    y = df[dataAccess.target]
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

    mlflow.set_tracking_uri(uri=mlflow_uri)
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
        mlflow.sklearn.log_model(model, registered_model_name=model_name, signature=signature, input_example=input_example)