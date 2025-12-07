import sqlite3

# Connection to the database
CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
