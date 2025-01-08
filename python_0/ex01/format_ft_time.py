from datetime import datetime

now = datetime.now()
then = datetime(1970, 1, 1)

seconds = (now - then).total_seconds()
scientific_notation = f"{seconds:.2e}"

today = {"day": now.day, "year": now.year, "month": now.strftime("%b")}

print(
    f"Seconds since January 1, 1970: {seconds} or \
    {scientific_notation} in scientific notation"
)
print(f"{today["month"]} {today["day"]} {today["year"]}")
