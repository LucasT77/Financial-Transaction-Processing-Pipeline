import csv

REQUIRED_FIELDS = {"transaction_id", "timestamp", "amount", "currency"}

def ingest(data_path: str) -> tuple[list[dict], list[dict]]:
	"""Ingesgt data from the specified path."""

	ingested_data = []
	errors = []
	try:
		with open(data_path, mode='r', encoding='utf-8') as file:
			csv_reader = csv.DictReader(file)
			if not csv_reader.fieldnames:
				errors.append({
					"type": "schema_error",
					"message": "File is empty or invalid CSV format."
				})
				return ingested_data, errors
			missing_fields = REQUIRED_FIELDS - set(csv_reader.fieldnames)
			if missing_fields:
				errors.append({
					"type": "schema_error",
					"message": f"Missing required fields: {missing_fields}"
				})
				return ingested_data, errors	
			for row_number, row in enumerate(csv_reader, start=2):
				if any(not row[field] for field in REQUIRED_FIELDS):
					errors.append({
						"type": "row_error",
						"row": row_number,
						"message": "Missing required column value"
					})
					continue
				ingested_data.append(row)
	except FileNotFoundError:
		errors.append({
			"type": "file_error",
			"message": f"File not found: {data_path}"
		})
	except csv.Error:
		errors.append({
			"type": "file_error",
			"message": f"Error reading CSV file: {data_path}"
		})
	except Exception as e:
		errors.append({
			"type": "unknown_error",
			"message": str(e)
		})
	return ingested_data, errors