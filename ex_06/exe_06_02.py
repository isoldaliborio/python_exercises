#Install Python and a programming text editor and write a program that prints one line other than 'hello world',
# then take two screen shots and upload them below. You should use the command line to execute the Python program you wrote in the text editor. Please do *not* use the IDLE Python Shell, the Python Interpreter (>>>), or a shortcut in your text editor to run the code. Later in the class when we start reading files, 
# we will need to be able to run Python programs from particular directories. See the videos for details. This assignment is not graded. 

word = 'borocoxo'
count = 0 
for letter in word:
    if letter == 'o':
        count = count + 1
print (count)
