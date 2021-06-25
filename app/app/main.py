from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from db.config import connect_db, disconnect_db
from routes import routers
from time import time


app = FastAPI(
    title= "Lapi-API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[
        "Access-Control-Allow-Headers",
        "X-Process-Time",
    
    ]
)


for route in routers:
    app.include_router(route)


@app.middleware('http')
async def login_validate(request: Request, call_next):
    global root_path
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["Access-Control-Allow-Headers"] =  "Authorization, Content-Type"
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def root():
    v = app.title
    return {"message": v}


@app.on_event("startup")
async def startup():
    await connect_db()
    print("db connected")


@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()
    print("db disconnected")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",
                reload=True,   port=8000, workers=2)
