# rename every file in the current directory that starts with 'X2Download.com - ' to the name of the file without the prefix
# example: X2Download.com - file.txt -> file.txt


import os

for filename in os.listdir('.'):
    if filename.startswith('X2Download.com - '):
        os.rename(filename, filename[17:])

# and check if the file has '(128 kbps)' in the name, if so, remove it
for filename in os.listdir('.'):
    if ' (128 kbps)' in filename:
        os.rename(filename, filename.replace(' (128 kbps)', ''))
