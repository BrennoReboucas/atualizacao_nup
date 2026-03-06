import schedule, time
from sheets import execute

# Force execute the first time now
execute()

# Config Schedule to execute function of sheets.py in 07h-am and 12h30-pm
schedule.every().day.at("07:00").do(execute)
schedule.every().day.at("12:30").do(execute)

# Simple loop
while True:
    schedule.run_pending()
    time.sleep(30)