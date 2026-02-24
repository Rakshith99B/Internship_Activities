import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\raksh\sqlite\sql_internship.db")

query = """
SELECT
    interns.name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track

"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()