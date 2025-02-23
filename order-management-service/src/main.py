from fastapi import FastAPI
from src.routers.orders import router
from src.metrics import setup_metrics

app = FastAPI()

# Include routers
app.include_router(router)

# Setup Prometheus metrics
setup_metrics(app)

@app.get("/")
def read_root():
    return {"message": "Order Management Service is running!"}
