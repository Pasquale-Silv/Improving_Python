import datetime

east = {'date': datetime.datetime(2007, 4, 20, 0, 0), 'price': 1232443}

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

today = datetime.datetime.now()
print(today)
print(f"Data odierna: {today:%d-%m-%Y}")