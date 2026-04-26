from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
import pymongo
from datetime import datetime, timedelta
from bson import ObjectId
from wsgi import app 

app = Flask(__name__)

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client.get_default_database()

users_col = db["users"]
posts_col = db["posts"]

def get_username(user_id):
    """Helper: get username from user_id"""
    user = users_col.find_one({"_id": ObjectId(user_id)})
    if user:
        return user.get("username", "Unknown")
    return "Unknown"


# ----------------------------------------
# ROUTE 0: Landing Page
# ----------------------------------------
@app.route("/")
def landing():
    return render_template("landing.html")


# ----------------------------------------
# ROUTE 1: Home — Posts Feed
# ----------------------------------------
@app.route("/feed")
def index():
    page = int(request.args.get("page", 1))
    per_page = 10
    skip = (page - 1) * per_page

    sort_by = request.args.get("sort", "recent")

    sort_field = "created_at" if sort_by == "recent" else "likes"
    sort_order = pymongo.DESCENDING

    total_posts = posts_col.count_documents({})
    posts_cursor = (
        posts_col.find().sort(sort_field, sort_order).skip(skip).limit(per_page)
    )

    posts = []
    for post in posts_cursor:
        user = users_col.find_one({"_id": post["user_id"]})
        posts.append(
            {
                "id": str(post["_id"]),
                "username": user["username"] if user else "Unknown",
                "avatar": user.get("avatar", "") if user else "",
                "content": post["content"],
                "likes": post["likes"],
                "comment_count": len(post.get("comments", [])),
                "created_at": post["created_at"].strftime("%b %d, %Y %I:%M %p"),
            }
        )

    total_pages = (total_posts + per_page - 1) // per_page

    return render_template(
        "index.html",
        posts=posts,
        page=page,
        total_pages=total_pages,
        sort_by=sort_by,
        total_posts=total_posts,
    )


# ----------------------------------------
# ROUTE 2: Users List
# ----------------------------------------
@app.route("/users")
def users():
    all_users = list(users_col.find())
    users_data = []

    for user in all_users:
        post_count = posts_col.count_documents({"user_id": user["_id"]})
        users_data.append(
            {
                "username": user["username"],
                "email": user["email"],
                "bio": user.get("bio", ""),
                "avatar": user.get("avatar", ""),
                "post_count": post_count,
                "joined_at": user.get("joined_at", datetime.now()).strftime("%b %Y"),
            }
        )

    # Sort by post count
    users_data.sort(key=lambda x: x["post_count"], reverse=True)

    return render_template("users.html", users=users_data)


# ----------------------------------------
# ROUTE 3: Top Posts (last 24 hours)
# ----------------------------------------
@app.route("/trending")
def trending():
    pipeline = [
        {"$match": {"created_at": {"$gte": datetime.now() - timedelta(hours=24)}}},
        {"$sort": {"likes": -1}},
        {"$limit": 10},
    ]
    top_posts = list(posts_col.aggregate(pipeline))

    posts = []
    for post in top_posts:
        user = users_col.find_one({"_id": post["user_id"]})
        posts.append(
            {
                "id": str(post["_id"]),
                "username": user["username"] if user else "Unknown",
                "avatar": user.get("avatar", "") if user else "",
                "content": post["content"],
                "likes": post["likes"],
                "comment_count": len(post.get("comments", [])),
                "created_at": post["created_at"].strftime("%b %d, %Y %I:%M %p"),
            }
        )

    return render_template("index.html",
        posts=posts,
        page=1,
        total_pages=1,
        sort_by="trending",
        total_posts=len(posts),
        is_trending=True,
    )


# if __name__ == "__main__":
#     app.run(debug=True)