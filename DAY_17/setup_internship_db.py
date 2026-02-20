import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('internship.db')
cursor = conn.cursor()

# Create interns table
cursor.execute('''
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
''')

# Insert 5 sample rows
sample_data = [
    ('Alice', 'Data Science', 15000),
    ('Bob', 'Web Dev', 12000),
    ('Charlie', 'Data Science', 14000),
    ('Diana', 'Web Dev', 13000),
    ('Eve', 'Data Science', 16000)
]
cursor.executemany('INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)', sample_data)
conn.commit()

# Query: Retrieve only name and track of all interns
cursor.execute('SELECT name, track FROM interns')
results = cursor.fetchall()
for row in results:
    print(row)

# Clean up
conn.close()
