from pymongo import MongoClient
from config import Config
from bson import ObjectId
from app.utils.prometheus_metrics import increment_log_entry, set_error_rate, set_log_entry_rate, update_cpu_memory_metrics
import time

client = MongoClient(Config.MONGO_URI)
db = client.get_default_database()
logs_collection = db.logs

def store_log(log_data):
    increment_log_entry(log_data['service'], log_data['level'])
    update_cpu_memory_metrics()  # Update CPU and memory metrics on each log entry
    return logs_collection.insert_one(log_data)


def get_logs(filter_params=None):
    if filter_params is None:
        filter_params = {}
    return list(logs_collection.find(filter_params))

def get_filtered_logs(service=None, level=None, start_time=None, end_time=None):
    filter_params = {}
    if service:
        filter_params['service'] = service
    if level:
        filter_params['level'] = level
    if start_time or end_time:
        filter_params['timestamp'] = {}
        if start_time:
            filter_params['timestamp']['$gte'] = start_time
        if end_time:
            filter_params['timestamp']['$lte'] = end_time
    
    logs = logs_collection.find(filter_params)
    return [
        {**log, 'id': str(log['_id'])}
        for log in logs
    ]

def calculate_error_rate(service, time_window=300):  # 5 minutes window
    end_time = time.time()
    start_time = end_time - time_window
    
    total_logs = logs_collection.count_documents({
        'service': service,
        'timestamp': {'$gte': start_time, '$lte': end_time}
    })
    
    error_logs = logs_collection.count_documents({
        'service': service,
        'level': 'ERROR',
        'timestamp': {'$gte': start_time, '$lte': end_time}
    })
    
    error_rate = error_logs / total_logs if total_logs > 0 else 0
    set_error_rate(service, error_rate)
    return error_rate

def calculate_log_entry_rate(service, time_window=60):  # 1 minute window
    end_time = time.time()
    start_time = end_time - time_window
    
    log_count = logs_collection.count_documents({
        'service': service,
        'timestamp': {'$gte': start_time, '$lte': end_time}
    })
    
    rate = log_count / time_window
    set_log_entry_rate(service, rate)
    return rate