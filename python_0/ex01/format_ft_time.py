from datetime import datetime
import time

now = datetime.now()

seconds = time.time()
scientific_notation = f"{seconds:.2e}"

today = {"day": now.day, "year": now.year, "month": now.strftime("%b")}

print(
    f"Seconds since January 1, 1970: {seconds:,.4f} or \
{scientific_notation} in scientific notation"
)
print(f"{today["month"]} {today["day"]} {today["year"]}")
