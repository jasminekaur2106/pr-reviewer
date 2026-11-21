from fastapi import FastAPI, Request

app = FastAPI(title="PR Reviewer")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    action = payload.get("action")
    pr = payload.get("pull_request", {})
    print(f"PR event: action={action}, title={pr.get('title')}")
    return {"received": True}