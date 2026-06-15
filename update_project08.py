from database import get_db
import json

db = get_db()

insights = json.dumps([
    "Netflix catalog is 69.1% Movies (5,377 titles) and 30.9% TV Shows (2,410 titles).",
    "Peak content growth was 2019 — 2,153 titles added in a single year.",
    "United States is the top content producing country by a significant margin.",
    "International Movies is the most common genre on the platform.",
    "Average movie duration is 99 minutes. Average TV show runs 1.8 seasons.",
])

tags = json.dumps([
    "Python", "Pandas", "Matplotlib", "EDA",
    "Business Insights", "7,787 Titles"
])

db.execute("""
    UPDATE projects SET
        status      = 'done',
        insights    = ?,
        tags        = ?,
        github_url  = 'https://github.com/Minga17/netflix-analysis',
        kaggle_url  = 'https://www.kaggle.com/code/mingangolo/netflix-analysis-ipynb',
        chart_image = 'images/chart2_content_per_year.png',
        what_i_did  = 'Loaded and cleaned 7,787 Netflix titles. Fixed date columns, filled missing directors/countries/ratings, and split the duration column which mixed minutes and seasons in one field. Built 4 visualizations — movies vs TV shows split, content added per year, top 10 producing countries, and top 10 genres. Used split-explode-strip pipeline to handle multi-value columns.'
    WHERE number = 8
""", [insights, tags])

db.commit()

row = db.execute("SELECT status, github_url, kaggle_url FROM projects WHERE number = 8").fetchone()
print("Status:", row[0])
print("GitHub:", row[1])
print("Kaggle:", row[2])
db.close()
