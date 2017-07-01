'''
IV. File I/O
----------
Predix Python Learning Series
GE Digital Shanghai
'''

### Basics ###

# Simple output: Print Statement
print("This is a print statement.")

# Escape Sequences:
print("This \t is a \nprint statement.")
print("\"This is a \'print statement.\\")

# input()
i = input("Input Statement Here: ")
print("This is the input statement: ", i)

# Write and print your own input statement
i = input(___)
print(___)


### Opening, reading, writing, closing text files (traditional) ###

# 1. Open file
# 2. Read/write file
# 3. Close file

# Add current directory to sys.path list. More about this in V. Modules.
import sys
sys.path.append('/Users/jie01pd2016/Documents/Interns/GE Digital/Python Training/IV. File I:O')
print(sys.path)

# Open 'test.txt' as f to be a read-only file
# Open 'text_copy.txt' as f2 to be written file
f = open('test.txt','r')
f2 = open('test_copy.txt','w')

# read the first line of the f file
f.___()

# read the next 10 characters of the f file
f.___(___)

# read the rest of the f file
f.___(___)

# reset pointer of f back to beginning of file
f.___(___)

# loop through each line of f, reading it and writing it to f2.
for ___ in ___:
    ___.___()

# Close the files
f.___()
f2.____(_)


### Opening, reading, writing, closing text files (with) ###

# We can do the above in a simple nested loop, without having to close the file,
# as it will automatically do so when the system goes out of the loop.

# Outer loop: open 'test2.txt' file as rf
with open(___, ___) as __:
    # Middle loop: open 'test2_copy.txt' file as wf
    with open(___, ___) as ___:
        # Inner loop: Loop through each line of rf, reading it and writing it to wf
        for ___ in ___:
            ___.___(___)


### Opening, reading, writing, closing binary files (with) ###

# We have to open files differently with binary files, as compared to text (ASCII) files.

# Outer loop: open 'dog.jpg' file as rf
with open(___, ___) as __:
    # Middle loop: open 'dog_copy.jpg' file as wf
    with open(___, ___) as ___:
        # Inner loop: Loop through each line of rf, reading it and writing it to wf
        for ___ in ___:
            ___.___(___)
