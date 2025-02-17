from fastapi import FastAPI
from app.routers import orders
from app.metrics import setup_metrics

app = FastAPI()

# Include routers
app.include_router(orders.router)

# Setup Prometheus metrics
setup_metrics(app)

@app.get("/")
def read_root():
    return {"message": "Order Management Service is running!"}
