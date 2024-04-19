import sqlite3
from table_info import table_definitions

def create_tables(cursor):
    for table in table_definitions:
        try:
            cursor.execute(table["definition"])
            print(f"Table '{table['name']}' created successfully!")
        except Exception as e:
            print(f"Error creating table '{table['name']}': {str(e)}")

def insert_data(cursor):
    insert_queries = [
        '''INSERT INTO sales VALUES
            (1, '2022-01-01', '09:00:00', 1, 1, 100),
            (2, '2022-01-02', '10:00:00', 2, 2, 200),
            (3, '2022-01-03', '11:00:00', 3, 3, 300),
            (4, '2022-01-04', '12:00:00', 4, 4, 400),
            (5, '2022-01-05', '13:00:00', 5, 5, 500),
            (6, '2022-02-01', '09:00:00', 1, 1, 100),
            (7, '2022-02-02', '10:00:00', 2, 2, 200),
            (8, '2022-02-03', '11:00:00', 3, 3, 300),
            (9, '2022-02-04', '12:00:00', 4, 4, 400),
            (10, '2022-02-05', '13:00:00', 5, 5, 500),
            (11, '2023-01-01', '09:00:00', 1, 1, 100),
            (12, '2023-01-02', '10:00:00', 2, 2, 200),
            (13, '2023-01-03', '11:00:00', 3, 3, 300),
            (14, '2023-01-04', '12:00:00', 4, 4, 400),
            (15, '2023-01-05', '13:00:00', 5, 5, 500)
        ''',
        '''INSERT INTO products VALUES
            (1, 'Product A', 50, 1),
            (2, 'Product B', 100, 2),
            (3, 'Product C', 150, 3),
            (4, 'Product D', 200, 2),
            (5, 'Product E', 250, 1)
        ''',
        '''INSERT INTO customers VALUES
            (1, 'John Doe', 'johndoe@gmail.com', '9438268490'),
            (2, 'Jane Smith', 'janesmith@gmail.com', '9807651423'),
            (3, 'Mark Johnson', 'markjohnson@gmail.com', '8892348963'),
            (4, 'Sarah Lee', 'sarahlee@gmail.com', NULL)
        '''
    ]

    for query in insert_queries:
        try:
            cursor.execute(query)
        except Exception as e:
            print(f"Error executing query: {str(e)}")
    
    print("The values were successfully inserted!!!")

def main():
    try:
        with sqlite3.connect('Sales.db') as conn:
            cursor = conn.cursor()
            create_tables(cursor)
            insert_data(cursor)
            conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
