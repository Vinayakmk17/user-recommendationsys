# 📸 Instagram Clone with AI Recommendation System

A full-stack Instagram-inspired social media application built with **React**, **FastAPI**, **Supabase**, and an **AI-powered Recommendation System**. Users can create accounts, share posts, interact with others, and receive personalized content recommendations.

---

## 🚀 Features

### 👤 User Authentication
- User Registration
- Secure Login
- JWT Authentication
- Protected Routes

### 📷 Posts
- Upload Images
- Create Captions
- Delete Posts
- View Feed

### ❤️ Social Features
- Like Posts
- Comment on Posts
- Follow / Unfollow Users
- User Profiles

### 🤖 AI Recommendation System
- Personalized User Recommendations
- Similar User Suggestions
- Machine Learning-based Recommendation Engine

### ☁️ Storage
- Supabase Storage for Images
- PostgreSQL Database (Supabase)

---

# 🛠 Tech Stack

## Frontend
- React.js
- Vite
- Axios
- React Router
- Context API
- CSS

## Backend
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication
- PostgreSQL

## Recommendation System
- Python
- FastAPI
- Pandas
- NumPy
- Scikit-learn

## Database
- Supabase PostgreSQL

## Storage
- Supabase Storage

## Deployment
- Frontend → Vercel
- Backend → Render
- Recommendation Service → Render

---

# 📂 Project Structure

```text
jitproject1/
│
├── frontend/
│   └── vite-project/
│       ├── public/
│       ├── src/
│       │   ├── api/
│       │   ├── assets/
│       │   ├── components/
│       │   ├── context/
│       │   └── pages/
│       └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── crud/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   └── requirements.txt
│
└── recoomendationsys/
    ├── app/
    └── requirements.txt
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Vinayakmk17/user-recommendationsy.git
cd user-recommendationsy
```

---

# Frontend Setup

```bash
cd frontend/vite-project

npm install

npm run dev
```

Runs on:

```
http://localhost:5173
```

---

# Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Runs on:

```
http://localhost:8000
```

---

# Recommendation System

```bash
cd recoomendationsys

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Runs on:

```
http://localhost:8001
```

---

# Environment Variables

Create a `.env` file.

Example:

```env
DATABASE_URL=your_database_url

SUPABASE_URL=your_supabase_url

SUPABASE_KEY=your_supabase_key

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Deployment

## Frontend

Deploy on **Vercel**

```
Root Directory:
frontend/vite-project
```

Build Command

```bash
npm run build
```

Output Directory

```
dist
```

---

## Backend

Deploy on **Render**

```
Root Directory:
backend
```

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## Recommendation System

Deploy on **Render**

```
Root Directory:
recoomendationsys
```

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---


# Future Improvements

- Stories Feature
- Real-time Chat
- Notifications
- Video Upload
- Search Users
- Explore Page
- Dark Mode
- Infinite Scrolling
- Reels Support

---

# Author

**Vinayak Kudlamath**

- GitHub: https://github.com/Vinayakmk17
- LinkedIn: https://www.linkedin.com/in/vinayak-kudlamath/

---

# License

This project is licensed under the MIT License.

---

⭐ If you like this project, don't forget to star the repository!
