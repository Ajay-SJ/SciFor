import datetime
import tkinter as tk
import winsound
import threading
import time

def thread_alarm(alarm_time):
    while True:
        now = datetime.datetime.now()
        if (now.hour == alarm_time.hour and now.minute == alarm_time.minute):
            winsound.Beep(2500, 1000)
            break
        time.sleep(1)

def set_alarm():
    alarm_time = entry.get()
    alarm_hour = int(alarm_time.split(':')[0])
    alarm_minute = int(alarm_time.split(':')[1])
    alarm_time = datetime.time(hour=alarm_hour, minute=alarm_minute)
    threading.Thread(target=thread_alarm, args=(alarm_time,)).start()

root = tk.Tk()
root.title("Python Alarm Clock")

tk.Label(root, text="Enter alarm time (format HH:MM)").grid(row=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

submit_button = tk.Button(root, text="Set Alarm", command=set_alarm)
submit_button.grid(columnspan=2)

root.mainloop()
