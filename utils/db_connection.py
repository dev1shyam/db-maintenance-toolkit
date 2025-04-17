import json
import pyodbc

def get_connection(config_path='config/db_config.json'):
    with open(config_path) as f:
        config = json.load(f)
    
    conn_str = (
        f"DRIVER={{{config['driver']}}};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"UID={config['username']};"
        f"PWD={config['password']}"
    )

    return pyodbc.connect(conn_str)

