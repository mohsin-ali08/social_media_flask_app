import pymongo
from faker import Faker
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# Connect MongoDB Atlas (same as app.py)
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client.get_default_database()

# Collections
users_collection = db["users"]
posts_collection = db["posts"]

# Clear old data (fresh start)
users_collection.drop()
posts_collection.drop()

fake = Faker()

# -----------------------------
# STEP 1: Insert Users
# -----------------------------
user_ids = []
print("Inserting users...")

for _ in range(100):
    user = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": "hashed_password",
        "avatar": "",
        "bio": fake.sentence(),
        "joined_at": datetime.now() - timedelta(days=random.randint(1, 365)),
    }
    result = users_collection.insert_one(user)
    user_ids.append(result.inserted_id)

print("✅ 100 users inserted")

# -----------------------------
# STEP 2: Insert Posts
# -----------------------------
print("Inserting posts...")

for _ in range(1000):
    post = {
        "user_id": random.choice(user_ids),
        "content": fake.text(),
        "likes": random.randint(0, 500),
        "created_at": datetime.now() - timedelta(hours=random.randint(0, 48)),
        "comments": [],
    }

    for _ in range(random.randint(1, 5)):
        comment = {
            "user_id": random.choice(user_ids),
            "text": fake.sentence(),
            "created_at": datetime.now(),
        }
        post["comments"].append(comment)

    posts_collection.insert_one(post)

print("✅ 1000 posts inserted")
print("\n🚀 Seeding complete! Now run: python app.py")