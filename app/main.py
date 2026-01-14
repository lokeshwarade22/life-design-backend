from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Life Design API is running"}
