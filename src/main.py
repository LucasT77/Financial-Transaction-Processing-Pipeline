import sys
from ingest import ingest
from validate import validate
from database import insert_transactions, create_connection, create_table
from report import generate_report

def main():
	if len(sys.argv) < 2 or len(sys.argv) > 4:
		print("Usage: python main.py <data_path> [database_path] [report_path]")
		sys.exit(1)

	data_path = sys.argv[1]
	if not data_path.lower().endswith(".csv"):
		print("Error: data_path must end with .csv")
		sys.exit(1)
	if len(sys.argv) == 3:
		database_path = sys.argv[2]
		if not database_path.lower().endswith(".db"):
			print("Warning: database_path must end with .db; using default 'transaction.db'")
			database_path = "transaction.db"
	else:
		database_path = "transaction.db"
	if len(sys.argv) == 4:
		report_path = sys.argv[3]
		if not report_path.lower().endswith(".txt"):
			print("Warning: report_path must end with .txt; using default 'transaction_report.txt'")
			report_path = "transaction_report.txt"
	else:
		report_path = "transaction_report.txt"

	rows, ingest_errors = ingest(data_path)
	if ingest_errors:
		print("Ingestion errors:")
		for error in ingest_errors:
			print(error)
		sys.exit(1)

	valid_rows, validation_errors = validate(rows)
	if validation_errors:
		print("Validation errors:")
		for row_number, error in validation_errors.items():
			print(f"Row {row_number}: {error}")
		sys.exit(1)

	conn = create_connection(database_path)
	if conn is None:
		print("Failed to connect to database")
		sys.exit(1)
	create_table(conn)
	insert_transactions(conn, valid_rows)
	print(f"Successfully ingested and validated {len(valid_rows)} transactions into {database_path}")
	generate_report(conn, report_path)
	print(f"Report successfully generated at {report_path}")
	conn.close()


if __name__ == "__main__":
    main()
