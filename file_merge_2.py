import os
rootdir = 'C:\\Myplace'  # Change this location
with open('Merged.log','a') as fout:

    for root, subFolders, files in os.walk(rootdir):
        for name in files:
            fout.write("\n---------------------\n")
            fout.write("%s" % os.path.join(root, name))
            fout.write("\n---------------------\n")
            with open(os.path.join(root,name),'r') as fin:
                for line in fin:
                    fout.write(line)