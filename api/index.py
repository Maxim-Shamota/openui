from fastapi import FastAPI
from openui.backend.main import app as backend_app  # поправьте пути
app = FastAPI()
@app.get("/health")
def health():
    return {"ok": True}
app.mount("/", backend_app)
