from fastapi import FastAPI

app = FastAPI(title="PR Reviewer")


@app.get("/health")
def health():
    return {"status": "ok"}