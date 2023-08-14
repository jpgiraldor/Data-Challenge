from flask import Flask, request, jsonify
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

app = Flask(__name__)

# PostgreSQL Database Configuration
db_config = {
    "host": "35.184.247.12",
    "port": '5432',
    "database": "postgres",
    "user": "postgres",
    "password": "12345678"
}

@app.route('/upload', methods=['POST'])
def upload_csv():
    try:
        # Get uploaded file
        file = request.files['file']

        # Get the table name from the filename (excluding extension)
        filename = file.filename
        table_name = filename.split('.')[0]  # Assumes filename has one dot and no path

        # Read CSV file using pandas
        df = pd.read_csv(file, header=None, keep_default_na=False, na_values=None)

        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            host=db_config["host"],
            port=db_config["port"],
            dbname=db_config["database"],
            user=db_config["user"],
            password=db_config["password"]
        )

        # Create a cursor
        cursor = connection.cursor()

        success_count = 0
        failed_lines = []

        # Convert DataFrame to list of tuples
        data_values = [tuple(row) for _, row in df.iterrows()]

        # Build the bulk insert query
        insert_query = f"INSERT INTO {table_name} VALUES %s"

        # Execute bulk insert
        for i, values in enumerate(data_values):
            try:
                # Convert empty strings to None for integer columns
                converted_values = [v if v != '' else None for v in values]
                execute_values(cursor, insert_query, [converted_values])
                success_count += 1
            except Exception as e:
                failed_lines.append({"line_number": i + 1, "error": str(e)})

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({
            "message": f"{success_count} rows inserted successfully.",
            "failed_lines": failed_lines
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
