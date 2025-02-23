from concurrent import futures
import grpc
from src.grpc_service import product_catalog_pb2, product_catalog_pb2_grpc
from src.services.product_logic import add_product, get_product, update_product, delete_product


class ProductCatalogService(product_catalog_pb2_grpc.ProductCatalogServiceServicer):
    def AddProduct(self, request, context):
        response_data = add_product(request)
        return product_catalog_pb2.ProductResponse(**response_data)

    def GetProduct(self, request, context):
        response_data = get_product(request.id)
        if "error" in response_data:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(response_data["error"])
            return product_catalog_pb2.ProductResponse()
        return product_catalog_pb2.ProductResponse(**response_data)

    def UpdateProduct(self, request, context):
        response_data = update_product(request)
        return product_catalog_pb2.ProductResponse(**response_data)

    def DeleteProduct(self, request, context):
        response_data = delete_product(request.id)
        return product_catalog_pb2.DeleteResponse(message=response_data["message"])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_catalog_pb2_grpc.add_ProductCatalogServiceServicer_to_server(ProductCatalogService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
