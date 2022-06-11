from fastapi import FastAPI
from scraper import *

app = FastAPI()

@app.get('/hagenberg')
def bachelors():
    return{
        hagenberg
    }

@app.get('/linz')
def bachelors():
    return{
        linz
    }

@app.get('/steyr')
def bachelors():
    return{
        wels
    }

@app.get('/wels')
def bachelors():
    return{
        wels
    }



