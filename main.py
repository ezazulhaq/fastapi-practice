from fastapi import FastAPI

app = FastAPI()

@app.get("/api-request")
def first_request():
    return {"message": "Hello World"}

