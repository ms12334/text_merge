#This script prints a file list whose extension is ext.
#Root directory: rootdir = 'C:\\Projects'
#Output file: logname = 'fileList.log'
#Extension: ext = '.txt'
#Written in Python 3.x

import os

# The top argument for walk
rootdir = 'C:\\Projects'
# The file extension to search for
ext = '.txt'
# Log file
fileListLog = 'fileList.log'
# Open log file for writing
out_flist= open(fileListLog, 'w')

for dirpath, dirnames, files in os.walk(rootdir):
    for name in files:
        if name.lower().endswith(ext):  # When there is a file with a specified extension
            # Write path and file name to a file list logfile
            out_flist.write("%s\n" % os.path.join(dirpath, name))
