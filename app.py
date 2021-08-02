from fastapi import FastAPI
from starlette.requests import Request
from datetime import datetime
import requests

app = FastAPI()


@app.get("/pull.js")
def root(request: Request):
    ip = request.client.host
    time = datetime.utcnow()
    myobj = {"ip": ip, "time": time}
    r = requests.get("http://112.151.179.200:8123/get", params=myobj)
