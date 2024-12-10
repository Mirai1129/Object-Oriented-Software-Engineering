from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import api, participation, rollcall

app = FastAPI()

app.include_router(participation.router)
app.include_router(rollcall.router)
app.include_router(api.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有 HTTP 方法
    allow_headers=["*"],  # 允許所有 HTTP 標頭
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
