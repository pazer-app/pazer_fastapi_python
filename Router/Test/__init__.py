from fastapi import APIRouter

route = APIRouter()


@route.get("/")
async def root():
    return {"message": "Hello Worlds"}


@route.get("/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
