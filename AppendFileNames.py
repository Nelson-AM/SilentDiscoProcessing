import os, csv, shutil, glob

thresholds = [50, 100, 150, 200, 250, 300, 350, 400]

for threshold in thresholds:
    
    filepath = "/Volumes/SAMSUNG/ESCOM/graphs/colorgraphs/" + str(threshold) + "/"
    # filepath = "/Volumes/SAMSUNG/fullgraphs/" + str(threshold) + "/"
    filelist = "../" + str(threshold) + ".txt"
    filepath = os.path.expanduser(filepath)
    filelist = os.path.expanduser(filelist)
    
    for files in glob.glob(filepath + "*.xml.gz"):
        
        splitfiles = files.split("_")
        
        if len(splitfiles[2]) < 6:
            splitfiles[2] = "{0:0>6}".format(splitfiles[2])
            newfiles = "_".join(splitfiles)
            print files
            print newfiles
            os.rename(files, newfiles)