# import pymongo
# from faker import Faker
# import random
# from datetime import datetime, timedelta

# # connect MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["social_media"]

# # collections
# users_collection = db["users"]
# posts_collection = db["posts"]

# # faker object
# fake = Faker()

# # -----------------------------
# # STEP 1: Insert Users
# # -----------------------------
# user_ids = []

# print("Inserting users...")

# for _ in range(100):
#     user = {
#         "username": fake.user_name(),
#         "email": fake.email(),
#         "password": "hashed_password"
#     }
    
#     result = users_collection.insert_one(user)
#     user_ids.append(result.inserted_id)

# print("✅ 100 users inserted")

# # -----------------------------
# # STEP 2: Insert Posts
# # -----------------------------
# print("Inserting posts...")

# for _ in range(1000):
#     post = {
#         "user_id": random.choice(user_ids),
#         "content": fake.text(),
#         "likes": random.randint(0, 500),
#         "created_at": datetime.now() - timedelta(hours=random.randint(0, 48)),
#         "comments": []
#     }

#     # add comments
#     for _ in range(random.randint(1, 5)):
#         comment = {
#             "user_id": random.choice(user_ids),
#             "text": fake.sentence(),
#             "created_at": datetime.now(),
#             "replies": []
#         }
#         post["comments"].append(comment)

#     posts_collection.insert_one(post)

# print("✅ 1000 posts inserted")

# # -----------------------------
# # STEP 3: Aggregation Query
# # -----------------------------
# print("Finding most liked post in last 24 hours...")

# pipeline = [
#     {
#         "$match": {
#             "created_at": {
#                 "$gte": datetime.now() - timedelta(hours=24)
#             }
#         }
#     },
#     {"$sort": {"likes": -1}},
#     {"$limit": 1}
# ]

# result = list(posts_collection.aggregate(pipeline))

# # -----------------------------
# # STEP 4: Output
# # -----------------------------
# if result:
#     print("\n🔥 Most Liked Post (Last 24 Hours):")
#     print(result[0])
# else:
#     print("No posts found in last 24 hours")