# Account Service

This is the Account Service for managing user accounts.

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Generate gRPC code from the `.proto` file:
    ```sh
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. account_service.proto
    ```

3. Start MongoDB server (if not installed as a service):
    ```sh
    mongod --port 27018 --dbpath "C:\MongoDB\data"
    ```

4. Run the server:
    ```sh
    python src/main.py
    ```

## API

- [CreateAccount](http://_vscodecontentref_/0): Create a new account.
- [GetAccount](http://_vscodecontentref_/1): Get account details by ID.
- [UpdateAccount](http://_vscodecontentref_/2): Update account details.
- [DeleteAccount](http://_vscodecontentref_/3): Delete an account by ID.