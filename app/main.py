from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.post("/analyze-log")
async def analyze_log(file: UploadFile = File(...)):
    content = await file.read()
    log_text = content.decode("utf-8")
    return {"status": "ok", "length": len(log_text)}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
