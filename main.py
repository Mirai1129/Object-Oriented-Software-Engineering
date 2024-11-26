from fastapi import FastAPI

from routes import participation, rollcall

app = FastAPI()

app.include_router(participation.router)
app.include_router(rollcall.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
