from datetime import date

# 13.1
today = date.today()

# 13.2
with open("today.txt", "w") as file:
    file.write(str(today))
with open("today.txt", "r") as file:
    today_string = file.read()

print(today_string)  

# 13.3
from datetime import datetime
parsed_date = datetime.strptime(today_string, "%Y-%m-%d").date()
print(parsed_date)
