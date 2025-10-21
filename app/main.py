from fastapi import FastAPI
from basic_route import router

app = FastAPI()
app.include_router(router,tags=["basic"])