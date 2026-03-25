from fastapi import FastAPI
import uvicorn
from app.database import engine, Base
from app.routes.jobs import router

app = FastAPI()
Base.metadata.create_all(engine)
app.include_router(router)

@app.get("/")
def root():
    return {"Hello": "World"}

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
