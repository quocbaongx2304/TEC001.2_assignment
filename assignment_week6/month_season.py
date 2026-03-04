seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter the number of a month (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Season:", seasons[0])
elif month >= 3 and month <= 5:
    print("Season:", seasons[1])
elif month >= 6 and month <= 8:
    print("Season:", seasons[2])
elif month >= 9 and month <= 11:
    print("Season:", seasons[3])
else:
    print("Invalid month")