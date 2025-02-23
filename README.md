# ZeroTrust_eCommerce

### tools
 - Docker Desktop


### setting up
- Start Docker Desktop
- Go to the root directory of the project (ZeroTrust_eCommerce)
- open cmd here
- run ``docker-compose build``
- run ``docker-compose up -d``
- check your docker desktop to see if all the containers are running
- current containers are:
    - mongo orders
    - mongo inventory
    - zookeeper
    - kafka
    - order-management
    - product-inventory
- open browser and go to ``http://localhost:8000/doc`` to see available APIs, you can also test the APIs from here and check data from database (please check db port in docker desktop)


