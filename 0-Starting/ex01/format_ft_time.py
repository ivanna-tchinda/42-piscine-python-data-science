import datetime

start_date = datetime.datetime(1970, 1, 1)
now = datetime.datetime.now()
elapsed_time = (now - start_date).total_seconds()

start_date_month = start_date.strftime("%B")
start_date_day = start_date.day
start_date_year = start_date.year

elapsed_time_seconds = "{:,}".format(elapsed_time)
elapsed_time_scientific = "{:e}".format(elapsed_time)

print(f"Seconds since {start_date_month} {start_date_day}, {start_date_year}: {elapsed_time_seconds} or {elapsed_time_scientific} in scientific notation")
print(now.strftime("%b %d %Y"))