# This is a sample Python script.
from fastapi import FastAPI

app = FastAPI()

# here is out first method


@app.get('/')
def get_home():
    return {"Response": 'Hello World and welcome...'}


@app.get('/welcome/{name}')
def greating(name):
    return {'Response': 'Welcome {}'.format(name)}
