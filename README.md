# 🏠 IMMO-PREV-IA

## 📋 Description

**Immo-Prev-IA** est un modèle d'intelligence artificielle pour prédire les prix immobiliers en France basé sur les données DVF (Demandes de Valeurs Foncières).

## 🎯 Fonctionnalités

- ✅ **Prédiction de prix** immobiliers (maisons/appartements)
- ✅ **Géolocalisation** par département et zones urbaines
- ✅ **Modèle optimisé** pour PC avec mémoire limitée
- ✅ **Tracking MLflow** pour suivi des expériences
- ✅ **Interface simple** de prédiction

## 📊 Données

- **Source** : DVF 2020-2025 consolidées
- **Échantillon** : 10k transactions pour entraînement rapide
- **Features** : Surface bâti, surface terrain, pièces, type

## 🚀 Installation

```bash
# 1. Cloner le projet
git clone <url-du-repo>
cd Immo-Prev-IA

# 2. Créer l'environnement virtuel
python -m venv env
env\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

## 🎮 Utilisation

### **1. Entraîner le modèle**
```bash
python modelcreation.py
```

### **2. Faire des prédictions**
```bash
python prediction.py
```

### **3. Interface MLflow**
```bash
mlflow ui --backend-store-uri file:./mlruns
# Ouvrir: http://localhost:5000
```

## 📁 Structure

```
Immo-Prev-IA/
├── data/
│   └── processed/
│       └── DVF_2020_2025_consolidated.csv
├── models/
│   └── micro_rf_YYYY_NNNN.pkl
├── mlruns/                    # MLflow tracking
├── modelcreation_micro.py     # Entraînement modèle
├── integrate_mlflow.py        # Intégration MLflow  
├── demo_prediction.py         # Tests prédictions
├── requirements.txt           # Dépendances
└── README.md
```

## 🧪 Exemple de prédiction

```python
from demo_prediction import predict_price_simple

# Appartement 70m² à Paris
result = predict_price_simple(
    surface_bati=70,
    surface_terrain=0,
    nb_pieces=3,
    type_local="Appartement",
    
)

print(f"Prix estimé: {result['prix_estime']:,}€")
# Prix estimé: 650,000€
```

## 📈 Performance

- **R² Score** : ~0.40 (40% de variance expliquée)
- **Entraînement** : <5 minutes
- **Modèle** : ~2 MB
- **Prédiction** : <1 seconde

## 🛠️ Technologies

- **Python 3.9+**
- **Scikit-learn** : Machine Learning
- **Pandas** : Manipulation données
- **MLflow** : Tracking expériences
- **Joblib** : Sérialisation modèles

## 📝 Licence

MIT License

## 👥 Contributeurs

- **Développeur Principal** : Herry Fabien / Rambourg Arnaud

---

*Projet créé en 2025 - Prédiction intelligente des prix immobiliers* 🏠🤖