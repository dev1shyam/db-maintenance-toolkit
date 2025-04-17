import sys
import os
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.db_connection import get_connection

def backup_all_databases(backup_dir='backups'):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Query to get all database names except tempdb
    cursor.execute("SELECT name FROM sys.databases WHERE name NOT IN ('tempdb')")
    databases = cursor.fetchall()

    # Create backup directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)
    
    # Timestamp for backup filenames
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Loop through each database and back it up
    for (dbname,) in databases:
        backup_file = os.path.join(backup_dir, f"{dbname}_{timestamp}.bak")
        backup_query = f"""
        BACKUP DATABASE [{dbname}]
        TO DISK = N'{backup_file}'
        WITH NOFORMAT, NOINIT,
        NAME = '{dbname}-Full Backup',
        SKIP, NOREWIND, NOUNLOAD, STATS = 10;
        """
        print(f"Backing up: {dbname} → {backup_file}")
        cursor.execute(backup_query)
        conn.commit()

    conn.close()
    print("✅ Backup complete.")

if __name__ == "__main__":
    backup_all_databases()

