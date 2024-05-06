###Проверка параметра пути через Path



# from fastapi import FastAPI, Path

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: int = Path(..., ge=1)):
#     return {"item_id": item_id}

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item"), q: str = None):
    return {"item_id": item_id, "q": q}
