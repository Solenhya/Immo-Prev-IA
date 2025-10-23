from fastapi import APIRouter , Request
from fastapi.templating import Jinja2Templates
router  = APIRouter()
templates = Jinja2Templates(directory="templates")
from . import prediction
#Pour l'instant set comme sa mais a generer en fonction du modèle en production
parameters = [{"label":"Surface du bati","id":"Surface_reelle_bati"},{"label":"Surface terrain","id":"Surface_terrain"},
              {"label":"Nombre de pieces","id":"Nombre_pieces_principales"},{"label":"Type (Appartement ou Maison)","id":"Type_local"}]

@router.get("/prediction_immo")
async def prediction_page(request:Request):
    return templates.TemplateResponse("prediction.html",{"request":request,"parametres_info":parameters})

@router.post("/predict_immo")
async def predict_immo(request:Request):
    form = await request.form()
    data = dict(form) 
    print(data)
    prix = prediction.model_predict(data)
    print(f"prix estimer:{prix}")
    return {"price":prix[0]}