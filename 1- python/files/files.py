import os
# files in python

# types of files
# text files (eg. .txt, .csv, .log, .json, .xml)
# binary files (eg. .jpg, .png, .mp3, .mp4, .zip)

# opening a file
# Python has an open() function for opening files. It takes 2 parameters: filename and mode.
file = open('example.txt', 'r')  # 'r' for read mode
text = file.read()
print(text)
file.close()

# other method to read file
# readline() - reads a single line from the file
file = open('example.txt', 'r')
line = file.readline()
print(line)
file.close()

# modes of opening a file
# 'r' - read (default) - opens a file for reading, error if the file does not exist
# 'w' - write - opens a file for writing, creates the file if it does not exist, truncates the file if it exists
# 'a' - append - opens a file for appending, creates the file if it does not exist
# 'b' - binary - opens a file in binary mode
# 't' - text (default) - opens a file in text mode
# '+' - read and write - opens a file for both reading and writing
# 'x' - create - creates a file, returns an error if the file exists
# 'r+' - read and write - opens a file for both reading and writing, error if the file does not exist
# 'w+' - write and read - opens a file for both writing and reading, creates
# 'a+' - append and read - opens a file for both appending and reading, creates
# 'xb' - create binary - creates a binary file, returns an error if the file exists
# 'rb' - read binary - opens a binary file for reading, error if the file
# 'wb' - write binary - opens a binary file for writing, creates the file if it does not exist, truncates the file if it exists
# 'ab' - append binary - opens a binary file for appending, creates the file if it does not exist
# 'r+b' - read and write binary - opens a binary file for both reading and writing, error if the file does not exist
# 'w+b' - write and read binary - opens a binary file for both writing and reading, creates
# 'a+b' - append and read binary - opens a binary file for both appending
# 'rt' - read text (default) - opens a text file for reading, error if the file does not exist
# 'wt' - write text - opens a text file for writing, creates the file if it does not exist, truncates the file if it exists
# 'at' - append text - opens a text file for appending, creates the file if it does not exist
# 'r+t' - read and write text - opens a text file for both reading and writing, error if the file does not exist
# 'w+t' - write and read text - opens a text file for both writing and reading, creates
# 'a+t' - append and read text - opens a text file for both appending and reading, creates
# 'x+t' - create text - creates a text file, returns an error if the file exists
# 'x+b' - create binary - creates a binary file, returns an error if the file exists
# 'r+b' - read and write binary - opens a binary file for both reading and writing, error if the file does not exist
# 'w+b' - write and read binary - opens a binary file for both writing and reading, creates
# 'a+b' - append and read binary - opens a binary file for both appending

# writing to a file
file = open('example.txt', 'a')  # 'a' for append mode
file.write('\nThis is a new line added to the file.')
file.close()

# using 'with' statement to open a file
# it automatically closes the file after the block of code is executed
with open('example.txt', 'r') as file:
    text = file.read()

print(text)

# examples
print('--- Examples ---')

# find the index of a substring in each line of a file
print('finding the index of a substring ? ')
with open('example.txt', 'r') as file:
    findedIndex = line.find('python')

print(findedIndex)  # prints the index of the first occurrence of 'python' in each line, -1 if not found


# find a score in a file and update it if the new score is higher than the best score
def findScoreAndUpdate(filename, new_score):
    print('Finding and updating score?')
    with open(filename, 'r+') as file:
        lines = file.readlines()
        best_score = lines[1]
        best_score = int(best_score.split('=')[1].strip())
        print(f'Current best score is {best_score}')

        for i, line in enumerate(lines):
            if 'Score' in line:
                score = int(line.split('=')[1].strip())
                if new_score > best_score:
                    best_score = new_score
                    file.write(f'Score = {best_score}\n')
                    print(f'New best score updated to {best_score}')
    return best_score
best_score = findScoreAndUpdate('example.txt', 95)
print(f'Best score is {best_score}')


# write multiplication table to a folder for 13 year old students
def writeTable(from_num, to_num, foldername):
    # Make sure the folder exists
    os.makedirs(foldername, exist_ok=True)

    filepath = os.path.join(foldername, 'multiplication_table.txt')

    print('Writing multiplication tables...')

    with open(filepath, 'w') as folderFile:
        for i in range(from_num, to_num + 1):
            folderFile.write(f'--- Multiplication Table of {i} ---\n')
            for j in range(1, 11):
                folderFile.write(f'{i} x {j} = {i * j}\n')
            folderFile.write('\n')  # Add space after each table

    print(f'Multiplication tables from {from_num} to {to_num} written to {filepath}')

writeTable(2, 20, 'multiplication_tables')
