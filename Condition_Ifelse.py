import datetime
now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("It's Spring.")
elif 6 <= month <= 8:
    print("It's Summer.")
elif 9 <= month <= 11:
    print("It's Fall.")
else:
    print("It's Winter.")