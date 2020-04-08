import datetime

date  = input("sasir la date (DD/MM/YYYY) :")

try:
	(day, month, year) = map(int, date.split('/'))
	dateTest = datetime.datetime(year, month, day)
except ValueError:
	print("la date n'est pas valide !")

aujourdhui = datetime.datetime.now()
print ("la date du jour:" + format(aujourdhui))


