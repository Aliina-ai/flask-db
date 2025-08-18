import sqlite3

DB_PATH = "your_database.db"  # заміни на шлях до своєї бази

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Видаляємо таблицю okrugs
c.execute("DROP TABLE IF EXISTS okrugs")

conn.commit()
conn.close()

print("Таблиця okrugs успішно видалена.")
