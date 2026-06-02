from database import get_db
import json

db = get_db()

insights = json.dumps([
    "78,843,232 total confirmed cases across 228 countries and territories.",
    "Global death rate of 2.12% — 1,672,981 total deaths recorded.",
    "France was the most affected country with 5.9M confirmed cases.",
    "Sudan had the highest death rate at 7.4% among countries with significant case counts.",
    "65,604,778 people recovered globally — 83.2% recovery rate.",
])

tags = json.dumps([
    "Python", "Pandas", "Matplotlib", "Time Series",
    "Global Data", "EDA", "306,429 Rows"
])

db.execute("""
    UPDATE projects SET
        status      = 'done',
        insights    = ?,
        tags        = ?,
        github_url  = 'https://github.com/Minga17/covid19-analysis',
        kaggle_url  = 'https://www.kaggle.com/code/mingangolo/covid19-analysis-ipynb',
        chart_image = 'images/chart1_global_trend.png',
        what_i_did  = 'Loaded and cleaned 306,429 rows of global COVID-19 data. Fixed mixed-format dates, standardized country names, and filled missing values. Built 4 visualizations — global daily trend with 7-day rolling average, top 10 countries by confirmed cases, top 10 countries by death rate, and monthly global case totals.'
    WHERE number = 7
""", [insights, tags])

db.commit()

row = db.execute("SELECT status, github_url, kaggle_url FROM projects WHERE number = 7").fetchone()
print("Status:", row[0])
print("GitHub:", row[1])
print("Kaggle:", row[2])
db.close()
