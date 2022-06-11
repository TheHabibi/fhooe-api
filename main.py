from fastapi import FastAPI
from scraper import *

app = FastAPI()

@app.get('/hagenberg')
def getHagenberg():
    return{
        "Hagenberg":hagenberg
    }

@app.get('/linz')
def getLinz():
    return{
        "Linz":linz
    }

@app.get('/steyr')
def getWels():
    return{
        "Steyr":steyr
    }

@app.get('/wels')
def getWels():
    return{
        "Wels":wels
    }



