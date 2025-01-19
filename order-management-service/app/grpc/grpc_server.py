
from concurrent import futures
import grpc
import order_management_pb2, order_management_pb2_grpc
from app.services.order_logic import create_order, get_order, update_order, delete_order

class OrderManagementService(order_management_pb2_grpc.OrderManagementServicer):
    def CreateOrder(self, request, context):
        """Handles the creation of an order."""
        order_data = {
            "item": request.item,
            "quantity": request.quantity,
            "price": request.price,
        }
        response_data = create_order(order_data)
        if "error" in response_data:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(response_data["error"])
            return order_management_pb2.OrderResponse()
        return order_management_pb2.OrderResponse(
            id=response_data["_id"],
            item=response_data["item"],
            quantity=response_data["quantity"],
            price=response_data["price"],
        )

    def GetOrder(self, request, context):
        """Handles fetching an order by ID."""
        response_data = get_order(request.id)
        if "error" in response_data:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(response_data["error"])
            return order_management_pb2.OrderResponse()
        return order_management_pb2.OrderResponse(
            id=response_data["_id"],
            item=response_data["item"],
            quantity=response_data["quantity"],
            price=response_data["price"],
        )

    def UpdateOrder(self, request, context):
        """Handles updating an order."""
        update_data = {
            "item": request.item,
            "quantity": request.quantity,
            "price": request.price,
        }
        response_data = update_order(request.id, update_data)
        if "error" in response_data:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(response_data["error"])
            return order_management_pb2.OrderResponse()
        return order_management_pb2.OrderResponse(
            id=request.id,
            item=update_data["item"],
            quantity=update_data["quantity"],
            price=update_data["price"],
        )

    def DeleteOrder(self, request, context):
        """Handles deleting an order."""
        response_data = delete_order(request.id)
        if "error" in response_data:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(response_data["error"])
            return order_management_pb2.DeleteResponse()
        return order_management_pb2.DeleteResponse(message=response_data["message"])


def serve():
    """Starts the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementService(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
