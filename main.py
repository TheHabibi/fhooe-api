from fastapi import FastAPI
from scraper import *

app = FastAPI()

@app.get('/bachelors')
def getHagenberg():
    return{
        "Hagenberg":hagenberg,
        "Linz":linz,
        "Steyr":steyr,
        "Wels":wels
    }