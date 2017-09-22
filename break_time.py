import time
import webbrowser

breaks = 3
break_count = 0

print "This program started on " + time.ctime()
while break_count < breaks:
    time.sleep(10)
    webbrowser.open("https://www.andreferreira.me")
    break_count = break_count + 1
