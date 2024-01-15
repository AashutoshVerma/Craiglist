from fastapi import  FastAPI

app = FastAPI()

@app.get("/")
def firstFunction():
    return {"message" : "Hello Guys I am  Fast APi Developer"}