import pymysql

class MySql:
    def __init__(self, db_host, db_user, db_password, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
    
    def insert(self, body):
        # Connect to the database
        conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)

        try:
            # Creating the SQL query string for insertion
            columns = ', '.join(body['data'].keys())
            placeholders = ', '.join(['%s'] * len(body['data']))
            queryStr = f"INSERT INTO `{body['model']}` ({columns}) VALUES ({placeholders})"
            # Execute the SQL query
            with conn.cursor() as cursor:
                cursor.execute(queryStr, list(body['data'].values()))
            # Commit the changes
            conn.commit()

        finally:
            # Close the connection
            conn.close()

    def update(self, body):
        # Connect to the database
        conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)

        try:
            # Generating the SET part of the query
            set_values = ', '.join([f"{key} = %s" for key in body['data']])
            # Creating the SQL query string
            queryStr = f"UPDATE `{body['model']}` SET {set_values} WHERE `{body['field']}` = %s"
            # Combining data values for SET and WHERE clause
            query_values = list(body['data'].values()) + [body['value']]
            # Create a cursor object
            with conn.cursor() as cursor:
                # Execute the SQL query
                cursor.execute(queryStr, query_values)
            # Commit the changes
            conn.commit()

        finally:
            # Close the connection
            conn.close()

    def delete(self, body):
        # Connect to the database
        conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)

        try:
            # Creating the SQL query string for deletion
            queryStr = f"DELETE FROM `{body['model']}` WHERE `{body['field']}` = %s"
            # Execute the SQL query
            with conn.cursor() as cursor:
                cursor.execute(queryStr, [body['value']])
            # Commit the changes
            conn.commit()

        finally:
            # Close the connection
            conn.close()

    def get(self, body):
        # Connect to the database
        conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)

        try:
            # Create a cursor object
            with conn.cursor() as cursor:
                if 'field' in body and 'value' in body and body['field'] and body['value']:
                    # Constructing SQL query with WHERE clause
                    queryStr = f"SELECT * FROM `{body['model']}` WHERE `{body['field']}` = %s"
                    cursor.execute(queryStr, [body['value']])
                else:
                    # If no specific field and value provided, fetch all records
                    cursor.execute(f"SELECT * FROM `{body['model']}`")

                # Fetch all rows
                rows = cursor.fetchall()
                # Get column names from the description attribute
                columns = [col[0] for col in cursor.description]
                # Convert rows to dictionaries
                result_dicts = [dict(zip(columns, row)) for row in rows]

        finally:
            # Close the connection
            conn.close()

        return result_dicts