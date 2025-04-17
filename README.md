# DB Maintenance Toolkit

Welcome to the **DB Maintenance Toolkit**! 🎉 This is a simple, easy-to-use collection of scripts designed to help automate essential database maintenance tasks for SQL Server, ensuring that your database is always running at its best.

## What Does This Toolkit Do?

This toolkit provides a set of Python scripts to automate some common maintenance tasks for your SQL Server databases. These include:

- **Backup your database** 🗂️
- **Rebuild indexes** for better performance ⚡
- **Update statistics** to optimize query execution 📊
- **Clean up logs** to keep your database tidy 🧹
- **Audit users** to ensure proper database access and security 🔐

With just a few commands, you can automate these tasks, saving you time and ensuring your database stays optimized.

## Requirements

Before you start, make sure you have the following installed:

- Python 3.x 🐍
- `pyodbc` Python library (used for database connections) 🔗
- SQL Server (local or cloud-based, like Azure SQL) 💻

If you don't have `pyodbc` installed yet, you can easily install it with:

```bash
pip install pyodbc
```
You’ll also need to have a working connection to your SQL Server instance, and you can do that by editing the config/db_config_template.json file with your database details.

## Setup
1. Clone the repo: Start by cloning this repository to your local machine:

```bash
git clone https://github.com/yourusername/db-maintenance-toolkit.git
cd db-maintenance-toolkit
```

2. Configure your database connection: Open the config/db_config_template.json file and update it with your SQL Server details (server name, username, password, etc.).

3. Run the scripts: You can now run the individual maintenance scripts! Here are some examples:

> Backup your database:
```bash
python scripts/backup_db.py
```
> Rebuild indexes:
```bash
python scripts/rebuild_indexes.py
```
> Update statistics:
```bash
python scripts/update_stats.py
```
> Clean up old logs:
```bash
python scripts/clean_logs.py
```
> Audit user access:
```bash
python scripts/audit_users.py
```

## Configuration
Make sure to configure your database connection details in the config/db_config_template.json file. It should look like this:

```json
{
  "server": "your_server_name",
  "database": "your_database_name",
  "username": "your_username",
  "password": "your_password"
}
```

## Contributions
Feel free to contribute! If you have any improvements or new scripts that can make this toolkit even better, open a pull request. Your contributions are always welcome! 🙌
