import os, csv, shutil, glob

threshold = 50

filepath = "/Volumes/SAMSUNG/ESCOM/graphs/colorgraphs/" + str(threshold) + "/"
    # filepath = "/Volumes/SAMSUNG/fullgraphs/" + str(threshold) + "/"
filelist = "../" + str(threshold) + ".txt"
filepath = os.path.expanduser(filepath)
filelist = os.path.expanduser(filelist)
    
for files in glob.glob(filepath + "*.xml.gz"):
    
    splitfiles = files.split("_")
    
    if splitfiles[1].startswith("0"):
        splitfiles[1] = splitfiles[1][1:]
        newfiles = "_".join(splitfiles)
        print(files)
        print(newfiles)
        os.rename(files, newfiles)