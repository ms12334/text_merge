import os
rootdir = 'C:\\Myplace'  # Change this location
ext = '.txt'  # File extension
outflist= open('FileList.log', 'w')

for root, sufFolders, files in os.walk(rootdir):
    for name in files:
        if name.lower().endswith(ext):  # When there is a file with a specified extension
            outflist.write("%s" % os.path.join(root, name) + "\n")
