import sys
import re

time_input = sys.argv[1]
time_array = re.split("[:.,]", time_input)

if len(time_array) < 2:
    print("\nPlease provide time in the following format: hh.mm.ss")
    print("seconds are optional because precision is a Swiss thing 🍰✨\n")
    exit()

hours = float(time_array[0])
minutes = float(time_array[1])
seconds = 0

if len(time_array) == 3:
    seconds = float(time_array[2])

converted_time = hours + minutes * (1 / 60) + seconds * (1 / 3600)
print("\nYour decimal time is: {}\n".format(float("%.4f" % (converted_time))))
