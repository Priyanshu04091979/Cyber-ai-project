from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Cybersecurity AI API running"}

@app.post("/report")
async def report_incident(request: Request):
    data = await request.json()
    return {"status": "received", "data": data}
