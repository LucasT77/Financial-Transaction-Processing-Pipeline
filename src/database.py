import sqlite3

def create_connection(db_file = "transaction.db"):
	""" create a database connection to the SQLite database specified by db_file
	:param db_file: database file
	:return: Connection object or None
	"""
	try:
		conn = sqlite3.connect(db_file)
		conn.execute("PRAGMA foreign_keys = ON;")
		return conn
	except sqlite3.Error as e:
		raise RuntimeError(f"Database connection failed: {e}")

def create_table(conn):
	""" create a table from the create_table_sql statement
	:param conn: Connection object
	:param create_table_sql: a CREATE TABLE statement
	:return:
	"""
	try:
		sql_create_transactions_table = """CREATE TABLE IF NOT EXISTS transactions (
											id INTEGER PRIMARY KEY AUTOINCREMENT,
											transaction_id TEXT NOT NULL UNIQUE,
											timestamp TEXT NOT NULL,
											amount TEXT NOT NULL,
											currency TEXT NOT NULL
										);"""
		with conn:
			conn.execute(sql_create_transactions_table)
	except sqlite3.Error as e:
		raise RuntimeError(f"Table creation failed: {e}")
	

class DuplicateTransactionConflict(Exception):
    pass


def insert_transactions(conn, valid_rows):
    """Insert validated transactions into the database, handling duplicates."""

    sql_insert = '''
        INSERT INTO transactions(transaction_id, timestamp, amount, currency)
        VALUES (?, ?, ?, ?)
    '''

    sql_select = '''
        SELECT timestamp, amount, currency
        FROM transactions
        WHERE transaction_id = ?
    '''

    with conn:
        for row in valid_rows:
            ts = row["timestamp"].isoformat()
            amt = str(row["amount"])

            try:
                conn.execute(
                    sql_insert,
                    (row["transaction_id"], ts, amt, row["currency"])
                )

            except sqlite3.IntegrityError:
                cur = conn.execute(sql_select, (row["transaction_id"],))
                existing = cur.fetchone()

                if not existing:
                    raise RuntimeError(
                        f"Integrity error inserting transaction {row['transaction_id']}"
                    )

                existing_ts, existing_amt, existing_cur = existing

                if (
                    existing_ts == ts and
                    existing_amt == amt and
                    existing_cur == row["currency"]
                ):
                    continue  # harmless duplicate

                raise DuplicateTransactionConflict(
                    f"Transaction {row['transaction_id']} already exists with different data"
                )

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
