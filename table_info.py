table_definitions = [
        {
            "name": "sales",
            "definition": """
                CREATE TABLE sales (
                    sales_id INTEGER PRIMARY KEY,
                    sales_date DATE,
                    sales_time TIME, 
                    customer_id INTEGER,
                    product_id INTEGER,
                    sales_amount DECIMAL,
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                    FOREIGN KEY (product_id) REFERENCES products(product_id)
                )
            """
        },
        {
            "name": "products",
            "definition": """
                CREATE TABLE products (
                    product_id INTEGER PRIMARY KEY, 
                    product_name VARCHAR(20),
                    price DECIMAL,
                    category_id INTEGER,
                    FOREIGN KEY (category_id) REFERENCES categories(category_id)
                )
            """
        },
        {
            "name": "customers",
            "definition": """
                CREATE TABLE customers (
                    customer_id INTEGER PRIMARY KEY,
                    customer_name VARCHAR(20),
                    email VARCHAR(40),
                    phone VARCHAR(10)
                )
            """
        }
    ]