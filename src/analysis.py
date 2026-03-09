from decimal import Decimal

def total_volume_by_currency(conn):
	"""Calculate total transaction volume by currency."""

	sql = '''
		SELECT currency, SUM(amount)
		FROM transactions
		GROUP BY currency
	'''
	cur = conn.cursor()
	cur.execute(sql)
	return {currency: Decimal(amount).quantize(Decimal('0.01')) for currency, amount in cur.fetchall()}

def average_transaction_amount_by_currency(conn):
	"""Calculate average transaction amount by currency."""

	sql = '''
		SELECT currency, AVG(amount)
		FROM transactions
		GROUP BY currency
	'''
	cur = conn.cursor()
	cur.execute(sql)
	return {currency: Decimal(str(avg_amount)).quantize(Decimal('0.01')) for currency, avg_amount in cur.fetchall()}

def transaction_count_by_currency(conn):
	"""Calculate transaction count by currency."""

	sql = '''
		SELECT currency, COUNT(*)
		FROM transactions
		GROUP BY currency
	'''
	cur = conn.cursor()
	cur.execute(sql)
	return {currency: count for currency, count in cur.fetchall()}

def largest_transaction_by_currency(conn):
	"""Find the largest transaction amount by currency."""

	sql = '''
		SELECT currency, MAX(amount)
		FROM transactions
		GROUP BY currency
	'''
	cur = conn.cursor()
	cur.execute(sql)
	return {currency: Decimal(str(max_amount)).quantize(Decimal('0.01')) for currency, max_amount in cur.fetchall()}

def smallest_transaction_by_currency(conn):
	"""Find the smallest transaction amount by currency."""

	sql = '''
		SELECT currency, MIN(amount)
		FROM transactions
		GROUP BY currency
	'''
	cur = conn.cursor()
	cur.execute(sql)
	return {currency: Decimal(str(min_amount)).quantize(Decimal('0.01')) for currency, min_amount in cur.fetchall()}

def daily_transaction_volume(conn):
	"""Calculate daily transaction volume."""

	sql = '''
		SELECT DATE(timestamp), SUM(amount)
		FROM transactions
		GROUP BY DATE(timestamp)
		ORDER BY DATE(timestamp)
	'''
	cur = conn.cursor()
	cur.execute(sql)
	return {date: Decimal(str(amount)).quantize(Decimal('0.01')) for date, amount in cur.fetchall()}