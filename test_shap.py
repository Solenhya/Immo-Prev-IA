from dotenv import load_dotenv
load_dotenv()
from app.handle_input import get_parameters_dynamique
from app import shapimplementation
import shap
import os
import matplotlib.pyplot as plt

valueTest = [{"Surface_reelle_bati": 80,
              "Surface_terrain": 0,
              "Nombre_pieces_principales": 3,
              "Type_local": "Appartement"},{"Surface_reelle_bati": 120,
              "Surface_terrain": 300,
              "Nombre_pieces_principales": 5,
              "Type_local": "Maison"},{"Surface_reelle_bati": 60,
              "Surface_terrain": 0,
              "Nombre_pieces_principales": 2,
              "Type_local": "Appartement"}]

valueTest2 = valueTest[1]
if __name__ == "__main__":
    #params = shapimplementation.compute_shap_values(valueTest)
    fig = shapimplementation.get_shap_waterfall_figure(valueTest2)
    print(type(fig))
    fig.savefig("waterfall.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
