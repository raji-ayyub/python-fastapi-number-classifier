# 📊 Number Classification API

A FastAPI-powered API that classifies numbers based on mathematical properties and provides a fun fact.

## 🌍 Live URL
🔗 **Base URL**: [`https://your-api-name.onrender.com`](https://python-fastapi-number-classifier.onrender.com)

## 🚀 Features
- Checks if a number is **prime**, **perfect**, **odd/even**, or an **Armstrong number**.
- Calculates the **digit sum**.
- Fetches a **fun fact** from the Numbers API.

## 🔥 Usage
### **GET `/api/classify-number`**
#### ✅ **Request Example**
```http
GET /api/classify-number?number=371


📌 Response (200 OK)

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number..."
}



❌ Error (400 Bad Request)

json
Copy
Edit
{
    "number": "invalid",
    "error": true
}


🏗️ Local Setup

bash
Copy
Edit
git clone https://github.com/raji-ayyub/python-fastapi-number-

local server - http://127.0.0.1:10000/docs


cd your-repo-name
pip install -r requirements.txt
uvicorn main:app --reload



🛠️ Deployment

Hosted on Render.
Start command:
bash
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 10000


✅ Ready for use! 🚀

yaml
Copy
Edit

---

### **Next Steps**

1. **Create the file**  
   ```bash
   touch README.md
Paste the above content into it
Commit and push to GitHub
bash
Copy
Edit
git add README.md
git commit -m "Added README"
git push origin main