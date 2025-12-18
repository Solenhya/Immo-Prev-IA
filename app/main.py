from fastapi import FastAPI
from dotenv import load_dotenv
import os
load_dotenv()


from .basic_route import router

app = FastAPI()
app.include_router(router,tags=["basic"])