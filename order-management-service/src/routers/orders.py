from http.client import HTTPException

from fastapi import APIRouter
from ..services.order_logic import create_order, get_order, delete_order, update_order

router = APIRouter()

@router.post("/orders/")
def create_new_order(order: dict):
    return create_order(order)

@router.get("/orders/{order_id}")
def get_existing_order(order_id: str):
    order = get_order(order_id)
    if not order:
        return {"error": "Order not found"}
    return order

@router.delete("/orders/{order_id}")
def delete_order_endpoint(order_id: str):
    result = delete_order(order_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.patch("/orders/{order_id}")
def partial_update_order_endpoint(order_id: str, update_data: dict):
    result = update_order(order_id, update_data)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
