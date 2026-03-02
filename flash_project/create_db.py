import sqlite3

DB_NAME = "flash_database.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS flash_history_customer (

session_id TEXT PRIMARY KEY,

ecu_id TEXT,

last_flash_status TEXT,

last_flash_timestamp TEXT,

binary_used TEXT,

existing_sw_version TEXT,

new_sw_version TEXT,

error_warning TEXT,

recovery_strategy TEXT

)
""")

conn.commit()
conn.close()

print("Flash History Table Created Successfully")