import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time)

    if current_time == alarm_time:
        print("ALARM! Wake Up!")
        break

    time.sleep(1)
