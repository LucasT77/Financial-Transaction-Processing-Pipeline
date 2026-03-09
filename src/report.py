from analysis import (
	total_volume_by_currency,
	average_transaction_amount_by_currency,
	transaction_count_by_currency,
	largest_transaction_by_currency,
	smallest_transaction_by_currency,
	daily_transaction_volume)

def write_section(file, title, data):
	file.write(f"{title.upper()}:\n")
	file.write("-" * (len(title) + 1) + "\n")
	if not data:
		file.write("  No data available\n\n")
		return
	for key, value in data.items():
		file.write(f"  {key}: {value}\n")
	file.write("\n")

def generate_report(conn, output_file="transaction_report.txt"):
	"""Generate a report summarizing transaction data."""

	with open(output_file, "w") as out_file:
		out_file.write("Transaction Report\n")
		out_file.write("=================\n\n")

		write_section(out_file, "Total Transaction Volume by Currency", total_volume_by_currency(conn))
		write_section(out_file, "Average Transaction Amount by Currency", average_transaction_amount_by_currency(conn))
		write_section(out_file, "Transaction Count by Currency", transaction_count_by_currency(conn))
		write_section(out_file, "Largest Transaction by Currency", largest_transaction_by_currency(conn))
		write_section(out_file, "Smallest Transaction by Currency", smallest_transaction_by_currency(conn))
		write_section(out_file, "Daily Transaction Volume", daily_transaction_volume(conn))