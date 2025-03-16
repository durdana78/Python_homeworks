import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("chinook.db")

# Read the customers table into a DataFrame
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)

# Close the database connection
conn.close()

# Display the first 10 rows
print(customers_df.head(10))