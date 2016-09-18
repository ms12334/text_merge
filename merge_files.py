# This script merges multiple text based files into one log file.
# The log file can includes file names and directory informations, too.  
# Place files you want to merge under the root directory.  Then, run this script.
# Root directory: rootdir = 'C:\\Projects'
# Output file: fileContentLog = 'fileContent.log'
# Extension: ext = '.txt'
# Written in Python 3.x

import os

# The top argument for walk
rootdir = 'C:\\Projects'
# The extension to search for
ext = '.txt'
# log file
fileContentLog = 'fileContent.log'
# Open log files for writing
with open(fileContentLog, 'a') as outfile:
    for dirpath, dirnames, files in os.walk(rootdir):
        for name in files:
            with open(os.path.join(dirpath, name)) as infile:
                if name.lower().endswith(ext):  # When there is a file with a specified extension
                    outfile.write('\n-----------\n')  # Separator
                    outfile.write(os.path.join(dirpath, name) + '\n')  # File path and file name
                    outfile.write(infile.read())  # File content