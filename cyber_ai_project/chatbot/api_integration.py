from fastapi import FastAPI
app = FastAPI()

@app.post("/report")
def report_incident(data: dict):
    # Save to database or forward to analyst
    return {"status": "received"}
