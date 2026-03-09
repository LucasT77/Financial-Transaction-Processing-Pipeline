from decimal import Decimal, InvalidOperation
import datetime

def validate(rows):
	"""Validate ingested data."""

	valid_rows = []
	errors = {}
	for row_number, row in enumerate(rows, start=2):
		cleaned_row = {}
		row_errors = {}

		# Validate transaction_id
		tx_raw = row.get("transaction_id")
		tx_id = str(tx_raw).strip() if tx_raw else None
		if not tx_id:
			row_errors.setdefault("transaction_id", []).append("transaction_id cannot be empty")
		else:
			cleaned_row["transaction_id"] = tx_id

		# Validate timestamp
		ts_raw = row.get("timestamp")
		if not ts_raw:
			row_errors.setdefault("timestamp", []).append("timestamp cannot be empty")
		else:
			try:
				dt = datetime.datetime.fromisoformat(ts_raw.strip())
				if dt.tzinfo is None:
					row_errors.setdefault("timestamp", []).append("timestamp must include timezone offset")
				else:
					cleaned_row["timestamp"] = dt.astimezone(datetime.timezone.utc)
			except ValueError:
				row_errors.setdefault("timestamp", []).append("timestamp must be in ISO 8601 format")

		# Validate amount
		amount_raw = row.get("amount")
		amount_str = str(amount_raw).strip() if amount_raw else ""
		if not amount_str:
			row_errors.setdefault("amount", []).append("amount cannot be empty")
		else:
			try:
				amount = Decimal(amount_str)
				if amount <= 0:
					row_errors.setdefault("amount", []).append("amount must be a positive number")
				else:
					cleaned_row["amount"] = amount
			except (InvalidOperation, ValueError):
				row_errors.setdefault("amount", []).append("amount must be a valid decimal number")

		# Validate currency
		currency = str(row.get("currency", "")).strip().upper()
		if not (len(currency) == 3 and currency.isalpha()):
			row_errors.setdefault("currency", []).append("currency must be a 3-letter uppercase code")
		else:
			cleaned_row["currency"] = currency

		# Collect errors or add valid row
		if row_errors:
			errors[row_number] = {
				"type": "validation_error",
				"errors": row_errors
			}
		else:
			valid_rows.append(cleaned_row)
	return valid_rows, errors