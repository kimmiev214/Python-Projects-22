from datetime import datetime, date

now = datetime.now() # Gets current time
today = date.today() # Get current date
current_time = now.strftime("%H:%M:%S")

print("Today's date: ", today)
print("Current time: ", current_time)
