from fastapi import APIRouter , Request
from fastapi.templating import Jinja2Templates
router  = APIRouter()
templates = Jinja2Templates(directory="templates")

#Pour l'instant set comme sa mais a generer en fonction du modèle en production
parameters = [{"label":"Surface bati","id":"surface_bati"},{"label":"Surface terrain","id":"surface_terrain"}]

@router.get("/prediction_immo")
async def prediction_page(request:Request):
    return templates.TemplateResponse("prediction.html",{"request":request,"parametres_info":parameters})

@router.post("/predict_immo")
async def predict_immo(request:Request):
    form = await request.form()
    data = dict(form) 
    print(data) #TODO rajouter la partie utilisation du modele
    return {"price":42}