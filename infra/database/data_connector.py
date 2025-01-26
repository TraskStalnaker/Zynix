import psycopg2
from psycopg2.extras import RealDictCursor

# Database connection configuration
DB_CONFIG = {
    "dbname": "zynix_db",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": 5432,
}

def get_db_connection():
    """
    Establish a connection to the PostgreSQL database.
    Returns:
        psycopg2.extensions.connection: A connection object.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def fetch_all(query, params=None):
    """
    Execute a SELECT query and fetch all results.
    Args:
        query (str): SQL SELECT query to execute.
        params (tuple): Optional parameters for the query.
    Returns:
        list: A list of records as dictionaries.
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def execute_query(query, params=None):
    """
    Execute an INSERT/UPDATE/DELETE query.
    Args:
        query (str): SQL query to execute.
        params (tuple): Optional parameters for the query.
    """
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit
