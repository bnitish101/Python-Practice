# File Handling
# read a text file
try:
    f = open('myData', 'r')
    print(f.read())  # read all
except Exception as e:
    print('Something went wrong, ', e)
finally:
    print('Exit')

print('------ cb+ 1 ------')
f = open('myData', 'r')
print(f.readline(), end='')  # read first line
print(f.readline(4))  # read second line and parameter will execute the no. of characters

print('----- cb+ 2 ------')
for data in f:
    print(data, end='')  # read all line one by one

print('----- cb+ 3 -----')
f1 = open('textfile1', 'w')  # clear file then write
f1.write('Test')
f1.write('Laptop')
f1 = open('textfile1', 'a')  # append data in the end of line
f1.write('Mobile')  # new content

print('----- cb+ 4 -----')
# copy text file to another file
f2 = open('myData', 'r')
f3 = open('textfile2', 'w')
for data in f2:  # get all line
    f3.write(data)  # write all lines to the file

f3 = open('textfile2', 'r')  # execute the copied content's file
print(f3.read())

print('----- cb+ 5 -----')
# copy image file (binary file)
bf = open('pic.jpg', 'rb')  # rb => read binary
bf1 = open('pic1.jpg', 'wb')  # wb => write binary
for data in bf:
    bf1.write(data)

print('Copy image/binary/none-text file')
