


# friends = [ 'Joseph', 'Glenn', 'Sally' ]
# friends.sort()
# print(friends[0])


# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list 
# and if not append it to the list. When the program completes, 
# sort and print the resulting words in python sort() order as shown in the desired output.


# fname = input("Enter file name: ")
fname = "romeo.txt"
filehandler = open(fname)

word_list = list()

for line in filehandler:
    words_in_line = line.split(" ")
    for word in words_in_line:
        if word not in word_list:
            word_list.append(word.rstrip())
word_list.sort()
print(word_list)


   


    
