import mysql.connector

# ==========================
# Connect to MySQL
# ==========================
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rach",
    port=3306
)

cursor = connection.cursor()

if connection.is_connected():
    print("✅ Connected to MySQL")


# ==========================
# Show all databases
# ==========================
print("\nAvailable Databases:")
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db[0])


# ==========================
# Create Database
# ==========================
cursor.execute("CREATE DATABASE IF NOT EXISTS storedb")
print("\n✅ Database 'storedb' created (or already exists).")


# ==========================
# Select Database
# ==========================
cursor.execute("USE storedb")


# ==========================
# Create Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS fruits(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    price DECIMAL(10,2)
)
""")

print("✅ Table 'fruits' created.")


# ==========================
# Show Tables
# ==========================
print("\nTables in storedb:")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table[0])


# ==========================
# Insert Data
# ==========================
sql = "INSERT INTO fruits(name, price) VALUES(%s, %s)"
values = ("Apple", 250)

cursor.execute(sql, values)
connection.commit()

print("\n✅ Record Inserted Successfully")


# ==========================
# Fetch Data
# ==========================
print("\nFruits Table:")

cursor.execute("SELECT * FROM fruits")

rows = cursor.fetchall()

for row in rows:
    print(row)


# ==========================
# Close Connection
# ==========================
cursor.close()
connection.close()

print("\n Connection Closed")