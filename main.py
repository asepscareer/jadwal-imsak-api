from importlib.resources import contents
from typing import Optional
from urllib import response
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.req import Data
from src.res import success, fail
from src.utils import getdaerah, getdata, baseurl

app = FastAPI()

@app.get("/api/v1/get-daerah")
def read_item():
    response  = getdaerah()
    if response is None:
        return fail(500)
    return success(response)

@app.post("/api/v1/get-data")
def read_item(item: Data):
    response  = getdata(item.daerah)
    if response is None:
        return fail(400)
    return success(response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)