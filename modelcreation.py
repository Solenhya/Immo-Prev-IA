import logging 
from app.model_training import train_model
import os
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    train_model(experiment_name="test_mlflow_integration",model_name="model_test",mlflow_uri=f"http://{os.getenv('MLFLOW_URI')}")      
