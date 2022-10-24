# 10.2 Write a program to read through the mbox-short.txt 
# and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time 
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"

name = f"{current_dir}/mbox-short.txt"

handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From "):
        split_line = line.split()
        time = split_line[5]
        hour=time.split(":")
        time=hour[0]
        counts[time] = counts.get(time,0) +1
        # list = (sorted([ (k,v) for k, v in counts.items()]))
        lst= list()
x = list(counts.items())
x.sort()
for hour, count in x:
    print(hour,count)

            

