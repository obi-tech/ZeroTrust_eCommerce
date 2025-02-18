# Order management service
This order management service provide order creation/delete/update methos and act
as kafka producer to produce order_created event
## Prerequisite
1. Python >= 3.11
2. You have kafka docker running on port 9092
3. You have mongoDB docker running on port 27017
4. (Optional) MongoDBCompass tool to visualize data base
## Set up
1. Go to order-management-service folder
2. install dependencies
``pip install -r requirements.txt``
## Start Service
1. run kafka and mongodb docker
2. ``uvicorn app.main:app --reload --port 8000``
## Test
1. Open
2.  Create an order using post api. Payload for test:
```{
"product_id": "P78624",
"quantity": 2,
"created_by": "U193039"
}
```
3. You will see the order inserted in orders table in your local database
