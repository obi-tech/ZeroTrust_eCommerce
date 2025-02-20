from fastapi import FastAPI
import threading
from app.grpc_server import serve as serve_grpc
from prometheus_client import make_asgi_app

app = FastAPI()

# Add Prometheus metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.on_event("startup")
async def startup_event():
    # Start gRPC server in a separate thread
    threading.Thread(target=serve_grpc, daemon=True).start()

@app.get("/")
async def root():
    return {"message": "Logging service is running"}