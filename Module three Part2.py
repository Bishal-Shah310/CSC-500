# Ask the user for input on the current time in hours
while True:
    time_now = int(input("Please enter the time now in hours (0-23): "))
    # Input validation between 0-23
    if 0 <= time_now <= 23:
        break
    else:
        print("Invalid input. Please enter a number between 0 and 23.")

# Ask the user for input on number of hours to wait for the alarm
while True:
    try:
        alarm_hours_to_wait = int(input("Please enter the number of hours to wait for the alarm: "))
        if alarm_hours_to_wait >= 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Alarm time logic using 24-hour clock
alarm_time = (time_now + alarm_hours_to_wait) % 24

# Output the time when the alarm will go off using 24-hour clock
print("The alarm will go off at:", alarm_time)
