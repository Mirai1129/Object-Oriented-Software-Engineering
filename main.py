from fastapi import FastAPI

from routes import api, participation, rollcall

app = FastAPI()

app.include_router(participation.router)
app.include_router(rollcall.router)
app.include_router(api.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
