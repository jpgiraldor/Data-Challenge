from flask import Flask, request, jsonify
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

app = Flask(__name__)

# PostgreSQL Database Configuration
db_config = {
    "host": "35.184.247.12",
    "port": '5432',
    "database": "postgres",
    "user": "postgres",
    "password": "12345678"
}
connection = psycopg2.connect(
    host=db_config["host"],
    port=db_config["port"],
    dbname=db_config["database"],
    user=db_config["user"],
    password=db_config["password"]
)

@app.route('/upload', methods=['POST'])
def upload_csv():

    print(1)
    # Get uploaded file
    file = request.files['file']
    #print(file)

    # Get the table name from the filename (excluding extension)
    filename = file.filename
    table_name = filename.split('.')[0]  # Assumes filename has one dot and no path

    # Read CSV file using pandas
    df = pd.read_csv(file)
    #print(df.head)
    # Connect to PostgreSQL database


    # Create a cursor
    cursor = connection.cursor()

    # Loop through rows and insert into PostgreSQL
    for index, row in df.iterrows():
        query = f"INSERT INTO {table_name}  VALUES ({'%s, '*row.size})"
        query = query[:-3]+')'
        print(query)
        values = tuple(row)  # Assuming your CSV columns match the table columns
        cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": f"CSV data uploaded and stored in table {table_name}."})



if __name__ == '__main__':
    app.run(debug=True)
