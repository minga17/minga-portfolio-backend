from database import get_db

db = get_db()
db.execute("UPDATE projects SET chart_image = 'images/dashboard.png' WHERE number = 11")
db.commit()

row = db.execute("SELECT chart_image FROM projects WHERE number = 11").fetchone()
print("chart_image value:", row[0])
db.close()
