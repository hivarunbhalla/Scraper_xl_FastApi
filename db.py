import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Create a cursor object
cur = conn.cursor()

# Define a function to save HTML content to the database
def save_html_to_database(url, html_content):
    # SQL statement to insert data into the table
    sql = "INSERT INTO html_content (url, content) VALUES (%s, %s)"
    # Execute the SQL statement
    cur.execute(sql, (url, html_content))
    # Commit the transaction
    conn.commit()

# Example usage
url = "https://example.com"
html_content = "<html><body><h1>Hello, World!</h1></body></html>"
save_html_to_database(url, html_content)

# Close cursor and connection
cur.close()
conn.close()
