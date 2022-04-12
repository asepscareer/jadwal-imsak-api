from starlette.responses import JSONResponse

def success(data):
    res = {
        "data" : data,
        "message": "Success"
    }

    return JSONResponse(content=res, status_code=200)

def fail(status):
    res = {
        "data" : None,
        "message": "Failed!"
    }

    return JSONResponse(content=res, status_code=status)