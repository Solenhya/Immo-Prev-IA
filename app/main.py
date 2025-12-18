from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv()


from .basic_route import router
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()
app.include_router(router,tags=["basic"])

REQUEST_COUNT = Counter("http_requests_total", "Total number of HTTP requests")

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "Hello from FastAPI with Prometheus"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)