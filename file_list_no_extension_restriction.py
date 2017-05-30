import os
rootdir = 'C:\\Myplace'
with open('FileList.log','a') as fout:
    for root, subFolders, files in os.walk(rootdir):
        for name in files:
            fout.write("%s" % os.path.join(root, name) + "\n")
