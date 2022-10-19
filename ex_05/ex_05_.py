#Write a program which repeatedly reads numbers until the user enters “done”.
#Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number,
#detect their mistake using try and except and
#print an error message and skip to the next number.
num=0
tot=0
while True:
    a = input('Enter a number: ')
    if a == 'done':
        break
    try:
        numbers=float(a)
    except:
        print ("Invalid input")
        continue
    #print(numbers)
    num=num+1
    tot=tot+numbers
#print('Done!')
print(tot, num, tot/num)
