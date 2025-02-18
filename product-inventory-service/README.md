# Product Inventory service
This product inventory service consume order_created event from kafka and update
product stock accordingly.
## Prerequisite
1. Python >= 3.11
2. You have kafka docker running on port 9092
3. You have mongoDB docker running on port 27016
4. (Optional) MongoDBCompass tool to visualize data base
## Set up
1. Go to product-inventory-service folder
2. install dependencies
``pip install -r requirements.txt``
## Start Service
1. run kafka and mongodb docker
2. (Optional) Mock product data into database:
   1. enter db folder
   2. ``python insert_data.py``

3. enter app folder, run  ``python main.ts``
## Test
1. Run product-inventory-service (main.ts)
2. Run order-management-service
3. Create order from order-management-service, the order payload should include
product id that exists in mocked product data in database
4. You will see the stock of the product updated after creating order

