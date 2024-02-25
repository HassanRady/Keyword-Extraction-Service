import uvicorn
from fastapi import FastAPI, Request
from keywords_extractor import pipeline


app = FastAPI()


@app.post("/extract")
async def extract_keywords(request: Request):
    data = await request.json()
    keywords = pipeline(data)
    return {"keywords": keywords}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9004)
