# FIRST
def batting_avg(lst):
	hits = sum([el[0] for el in lst])
	at_bats = sum([el[1] for el in lst])
	res = str(round(hits / at_bats, 3))[1:5].ljust(4, "0")
	return res
	
	
	
# SECOND
def weekly_salary(hours):
	res = 0
	for i in range(len(hours)):
		hourPay = 10 if (i < 5) else (10 * 2)
		hourPayOvertime = 15 if (i < 5) else (15 * 2)
		if hours[i] > 8:
			res += (8 * hourPay)
			res += ((hours[i] - 8) * hourPayOvertime)
		else:
			res += (hours[i] * hourPay)
	return res