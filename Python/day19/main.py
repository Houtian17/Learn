from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get('/user')
async def user(
        *,
        user_id: int = Query(..., title="The ID", gt=0)
):    return {'user_id': user_id}


@app.post('/user/update')
async def update_user(
        *,
        user_id: int,
        really_update: int = Query(...)
):    return {'user_id': user_id}
