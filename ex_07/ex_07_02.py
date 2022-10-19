#Write a program that prompts for a file name, 
# then opens that file and reads through the file, looking for lines of the form:
#    ---- X-DSPAM-Confidence:    0.8475 ----
#Count these lines 
# and extract the floating point values from each of the lines 
# and compute the average of those values 
# and produce an output as shown below(# resul expected:  Average spam confidence: 0.7507185185185187). 
# Do not use the sum() function 
# or a variable named sum in your solution.


#fname = "/Users/isoldaliborio/Documents/Isolda/Programming/Python_begner_coursera_Universit Michigan/py4e/ex_07/mbox-short.txt"
fname = input("Enter file name: ")
content = open(fname)
count = 0
numerator = 0

for line in content:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count+1
        split_values=line.split(":")
        float_values=float(split_values[1])
        numerator += float_values
average = numerator / count 
print("Average spam confidence: " + str(average))

"""
Outra forma de responder: 
 --- the answer was distinct probably for some aproximation in one of the two answer ----
from statistics import mean 
fname = "/Users/isoldaliborio/Documents/Isolda/Programming/Python_begner_coursera_Universit Michigan/py4e/ex_07/mbox-short.txt"
content = open(fname)
count = 0
values = []
for line in content:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count+1
        split_values=line.split(":")
        float_values=float(split_values[1])
        values.append(float_values)
average = mean(values)
print("Average spam confidence: " + str(average))
"""

