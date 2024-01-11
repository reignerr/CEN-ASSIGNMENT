import mysql.connector

# Replace these with your actual database credentials
host = "your_host"
user = "your_user"
password = "your_password"
database = "your_database"

# Establish Connection
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a Cursor
mycursor = mydb.cursor()

# Example: Create a table
create_table_query = "CREATE TABLE IF NOT EXISTS example_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
mycursor.execute(create_table_query)

# Example: Insert data
insert_data_query = "INSERT INTO example_table (name) VALUES (%s)"
data_to_insert = ("John Doe",)
mycursor.execute(insert_data_query, data_to_insert)

# Example: Read data
mycursor.execute("SELECT * FROM example_table")
result = mycursor.fetchall()
print("Data in the table:")
for row in result:
    print(row)

# Example: Update data
update_data_query = "UPDATE example_table SET name = %s WHERE id = %s"
new_name = "Jane Doe"
row_id_to_update = 1
mycursor.execute(update_data_query, (new_name, row_id_to_update))

# Example: Read updated data
mycursor.execute("SELECT * FROM example_table")
result_after_update = mycursor.fetchall()
print("\nData after update:")
for row in result_after_update:
    print(row)

# Commit Changes
mydb.commit()

# Close the Connection
mycursor.close()
mydb.close()
