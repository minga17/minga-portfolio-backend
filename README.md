# minga-portfolio-backend

> 🌐 **Live site:** [portfolio.mingangolo.com](https://portfolio.mingangolo.com)

Backend service powering Minga Ngolo's personal data analyst portfolio.

---

## ⚠️ Cold Start Notice

Hosted on **Render's free tier**. After 15 minutes of inactivity the server spins down. The **first request may take 30–60 seconds** to wake up. Subsequent requests are fast.

---

## 🚀 Tech Stack

- **Language:** Python 3
- **Framework:** Flask
- **Database:** SQLite
- **Hosting:** [Render](https://render.com)
- **Frontend:** HTML, CSS, JavaScript

---

## 📁 Project Structure

minga-portfolio-backend/
├── app.py              # Flask server + all API routes
├── database.py         # SQLite setup and connection
├── seed.py             # Seeds all 11 projects into DB
├── requirements.txt    # Python dependencies
├── Procfile            # Render start command
├── render.yaml         # Render deploy config
├── index.html          # Homepage
├── project.html        # Projects page (API-driven)
├── images/             # Chart screenshots
└── static/
└── js/
└── api.js      # Shared API helper
```

---

## 🛠️ Running Locally

```bash
# Clone the repo
git clone https://github.com/Minga17/minga-portfolio-backend.git
cd minga-portfolio-backend

# Install dependencies
pip install -r requirements.txt

# Seed the database
python seed.py

# Start the server
python app.py
```

Visit `http://localhost:5000`

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/projects` | All 11 portfolio projects |
| GET | `/api/projects/<id>` | Single project by ID |
| GET | `/api/stats` | Visitor counts and project stats |
| POST | `/api/pageview` | Log a page view |
| POST | `/api/contact` | Save a contact message |

---

## 🔗 Related

- **Live portfolio:** [portfolio.mingangolo.com](https://portfolio.mingangolo.com)
- **LinkedIn:** [linkedin.com/in/minga17](https://www.linkedin.com/in/minga17)
- **GitHub:** [github.com/Minga17](https://github.com/Minga17)
- **Kaggle:** [kaggle.com/mingangolo](https://www.kaggle.com/mingangolo)

---

## 📄 License

MIT
