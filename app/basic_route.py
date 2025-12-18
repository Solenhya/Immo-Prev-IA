from fastapi import APIRouter , Request
from fastapi.templating import Jinja2Templates
router  = APIRouter()
templates = Jinja2Templates(directory="app/templates")
from . import prediction
from . import handle_input
import logging
from prometheus_client import Counter,generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
logger = logging.getLogger(__name__)

#Pour l'instant set comme sa mais a generer en fonction du modèle en production
parameters = [{"label":"Surface du bati","id":"Surface_reelle_bati"},{"label":"Surface terrain","id":"Surface_terrain"},
              {"label":"Nombre de pieces","id":"Nombre_pieces_principales"},{"label":"Type (Appartement ou Maison)","id":"Type_local"}]

logger.info(f"Parametres static: {parameters}")
parameters = handle_input.get_parameters_dynamique()
logger.info(f"Parametres charger par le modèle : {parameters}")

REQUEST_COUNT = Counter("http_requests_total", "Total number of HTTP requests")

@router.get("/")
async def prediction_page(request:Request):
    REQUEST_COUNT.inc()
    return templates.TemplateResponse("prediction.html",{"request":request,"parametres_info":parameters})

@router.post("/predict_immo")
async def predict_immo(request:Request):
    REQUEST_COUNT.inc()
    form = await request.form()
    data = dict(form) 
    print(data)
    prix = prediction.model_predict(data)
    print(f"prix estimer:{prix}")
    return {"price":prix[0]}


@router.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)