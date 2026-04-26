# ⚡ SocialFeed — Social Media App

A simple social media web app built with **Python Flask** and **MongoDB**.  
You can view posts, see trending content, and explore user profiles.

---

## 📁 Folder Structure

```
social_media_app/
├── app.py               ← Main Flask server (routes/logic)
├── seed.py              ← Inserts fake data into database
├── debug.py             ← Checks database connection
├── requirements.txt     ← Python packages list
├── vercel.json          ← Vercel deployment config
├── .env                 ← Secret keys (never share this!)
├── static/
│   ├── css/
│   │   └── style.css    ← All styling
│   └── js/
│       └── main.js      ← Frontend JavaScript
└── templates/
    ├── base.html        ← Common navbar/footer layout
    ├── landing.html     ← Home/landing page
    ├── index.html       ← Posts feed page
    └── users.html       ← Users list page
```

---

## 🛠️ Technologies Used

| Technology | What it does |
|---|---|
| **Python** | Main programming language |
| **Flask** | Web framework (creates routes/pages) |
| **MongoDB Atlas** | Cloud database (stores users & posts) |
| **PyMongo** | Connects Python to MongoDB |
| **Faker** | Generates fake users & posts for testing |
| **Jinja2** | HTML templating (comes with Flask) |
| **Vercel** | Free hosting/deployment platform |

---

## ⚙️ Local Setup (Step by Step)

### Step 1 — Install Python
Download Python from https://python.org  
Make sure to check ✅ **"Add Python to PATH"** during install.

### Step 2 — Download the Project
```bash
# If you have git:
git clone <your-repo-link>
cd social_media_app

# Or just download ZIP and extract it
```

### Step 3 — Create Virtual Environment
```bash
# Create
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate
```
> 💡 You will see `(.venv)` in your terminal — that means it worked!

### Step 4 — Install Packages
```bash
pip install -r requirements.txt
```

### Step 5 — Create `.env` File
Create a file named `.env` in the root folder and paste this:
```
MONGO_URI=your_mongodb_atlas_connection_string_here
```
> 💡 See "MongoDB Atlas Setup" section below to get your connection string.

### Step 6 — Insert Fake Data
```bash
python seed.py
```
This will insert 100 users and 1000 posts into your database.

### Step 7 — Run the App
```bash
python app.py
```
Open your browser and go to: **http://127.0.0.1:5000**

---

## 🍃 MongoDB Atlas Setup (Free Cloud Database)

1. Go to https://mongodb.com/atlas and create a **free account**
2. Click **"Create Cluster"** → choose **Free (M0)** tier
3. Go to **Database Access** → Add a new user with username & password
4. Go to **Network Access** → Click "Add IP Address" → Allow access from anywhere (`0.0.0.0/0`)
5. Go to **Clusters** → Click **"Connect"** → **"Drivers"**
6. Copy the connection string — it looks like this:
```
mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/social-media?retryWrites=true&w=majority
```
7. Paste it in your `.env` file as `MONGO_URI=...`

---

## 🌐 Pages & Routes

| Page | URL | Description |
|---|---|---|
| 🏠 Landing | `/` | Welcome/home page |
| 📰 Feed | `/feed` | All posts (paginated) |
| 🔥 Trending | `/trending` | Most liked posts (last 24h) |
| 👥 Users | `/users` | All users sorted by activity |

---

## 🚀 Deploy on Vercel (Free Hosting)

### Step 1 — Install Vercel CLI
```bash
npm install -g vercel
```
> 💡 You need Node.js installed. Download from https://nodejs.org

### Step 2 — Login to Vercel
```bash
vercel login
```

### Step 3 — Deploy
```bash
vercel --prod
```

### Step 4 — Add Environment Variable
1. Go to https://vercel.com → Your Project
2. Click **Settings** → **Environment Variables**
3. Add:
   - **Key:** `MONGO_URI`
   - **Value:** your MongoDB Atlas connection string
4. Click **Save** → Redeploy

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "0 users, 0 posts" showing
Run the debug script:
```bash
python debug.py
```
- If `URI: None` → your `.env` file is missing or wrong
- If `Users: 0` → run `python seed.py` again

### Page loading very slow
Check that your MongoDB Atlas **Network Access** allows all IPs (`0.0.0.0/0`)

### Vercel shows 500 error
Go to **Vercel Dashboard → Project → Deployments → Functions → View Logs** and check the error message.

---

## 📦 requirements.txt Explained

```
flask          ← Web framework
pymongo[srv]   ← MongoDB driver ([srv] needed for Atlas)
dnspython      ← Required for mongodb+srv:// connections
python-dotenv  ← Reads .env file
faker          ← Generates fake data for seed.py
```

---

## 🔐 Important Security Notes

- **Never share your `.env` file** — it contains your database password
- **Never push `.env` to GitHub** — add it to `.gitignore`
- The `.env` file is only for local development — on Vercel use Environment Variables

---

## 👨‍💻 Made With

- Python 3.x
- Flask
- MongoDB Atlas
- Deployed on Vercel
