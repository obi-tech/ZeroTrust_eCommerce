while ($true) { Invoke-WebRequest -Uri "http://127.0.0.1:58825/orders" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"product_id": "P78624", "quantity": 1, "created_by": "U193039"}' }