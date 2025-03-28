from fastapi import FastAPI

minhaApi = FastAPI()

@minhaApi.get("/")
async def root():
  return {"message": "Hello World!"}

@minhaApi.get("/items")
async def getItems():
  return { "items": [ { "id": 1 }, { "id": 2 }, { "id": 3 } ]}

