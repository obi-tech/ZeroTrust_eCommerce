from prometheus_client import Counter, Histogram, Gauge
import psutil

# Existing metrics
REQUEST_COUNT = Counter('request_count_total', 'Total Request Count', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['endpoint'])

# New metrics
LOG_ENTRY_COUNT = Counter('log_entry_count_total', 'Total Log Entry Count', ['service', 'level'])
ERROR_RATE = Gauge('error_rate', 'Error Rate', ['service'])
CPU_USAGE = Gauge('cpu_usage_percent', 'CPU Usage Percentage')
MEMORY_USAGE = Gauge('memory_usage_bytes', 'Memory Usage in Bytes')
LOG_ENTRY_RATE = Gauge('log_entry_rate', 'Log Entry Rate per Second', ['service'])

def update_cpu_memory_metrics():
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().used)

def increment_log_entry(service, level):
    LOG_ENTRY_COUNT.labels(service=service, level=level).inc()

def set_error_rate(service, rate):
    ERROR_RATE.labels(service=service).set(rate)

def set_log_entry_rate(service, rate):
    LOG_ENTRY_RATE.labels(service=service).set(rate)