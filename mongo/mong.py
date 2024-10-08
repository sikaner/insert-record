from pymongo import MongoClient

# MongoDB connection string (replace <username>, <password>, and <host> with your MongoDB credentials)
client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB instance

# Access the 'cmp_db' database and 'users' collection
db = client["cmp_db"]
collection = db["users"]

# Inserting new record
users = [
    {"name": "John Doe", "age": 28, "performance": 7, "responsibility": 8},
    {"name": "Jane Smith", "age": 32, "performance": 9, "responsibility": 9},
    {"name": "Alice Johnson", "age": 25, "performance": 6, "responsibility": 7},
    {"name": "Bob Brown", "age": 30, "performance": 8, "responsibility": 8}
]

# Insert a new user into the collection
for user in users:
    insert_result = collection.insert_one(user)
    print(f"Inserted new user with ID: {insert_result.inserted_id}")

