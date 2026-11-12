import time

current_time = time.localtime()
# fetch the current hour 
current_hour = current_time.tm_hour

if current_hour <= 12:
    print("Good Morning")
elif current_hour >= 12 and current_hour <= 18:
    print("Good Afternoon")
elif current_hour >= 18:
    print("Good Evening")