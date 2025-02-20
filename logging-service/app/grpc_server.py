import grpc
from concurrent import futures
from app import logging_pb2
from app import logging_pb2_grpc
from app.services.log_service import store_log, get_filtered_logs, calculate_error_rate, calculate_log_entry_rate
from app.utils.prometheus_metrics import REQUEST_COUNT, REQUEST_LATENCY, update_cpu_memory_metrics
import time

class LoggingService(logging_pb2_grpc.LoggingServiceServicer):
    def SendLog(self, request, context):
        start_time = time.time()
        try:
            log_data = {
                'service': request.service,
                'level': request.level,
                'message': request.message,
                'timestamp': request.timestamp
            }
            result = store_log(log_data)
            REQUEST_COUNT.labels(method='SendLog', endpoint='gRPC', http_status='OK').inc()
            
            # Calculate and update error rate and log entry rate
            calculate_error_rate(request.service)
            calculate_log_entry_rate(request.service)
            update_cpu_memory_metrics()
            
            return logging_pb2.LogResponse(id=str(result.inserted_id))
        except Exception as e:
            REQUEST_COUNT.labels(method='SendLog', endpoint='gRPC', http_status='ERROR').inc()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return logging_pb2.LogResponse()
        finally:
            REQUEST_LATENCY.labels(endpoint='SendLog').observe(time.time() - start_time)

    def GetLogs(self, request, context):
        start_time = time.time()
        try:
            logs = get_filtered_logs(
                service=request.service,
                level=request.level,
                start_time=request.start_time,
                end_time=request.end_time
            )
            REQUEST_COUNT.labels(method='GetLogs', endpoint='gRPC', http_status='OK').inc()
            return logging_pb2.GetLogsResponse(logs=[
                logging_pb2.LogEntry(
                    id=log['id'],
                    service=log['service'],
                    level=log['level'],
                    message=log['message'],
                    timestamp=log['timestamp']
                ) for log in logs
            ])
        except Exception as e:
            REQUEST_COUNT.labels(method='GetLogs', endpoint='gRPC', http_status='ERROR').inc()
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return logging_pb2.GetLogsResponse()
        finally:
            REQUEST_LATENCY.labels(endpoint='GetLogs').observe(time.time() - start_time)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    logging_pb2_grpc.add_LoggingServiceServicer_to_server(LoggingService(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()