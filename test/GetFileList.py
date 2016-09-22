import os, csv, shutil, glob

thresholds = [50, 100, 150, 200, 250, 300, 350, 400]

for threshold in thresholds:
    filepath = "/Volumes/SAMSUNG/colorgraphs/" + str(threshold) + "/"
    # filepath = "/Volumes/SAMSUNG/ESCOM/graphs/colorgraphs/" + str(threshold) + "/"
    
    filelist = "../" + str(threshold) + ".txt"
    filepath = os.path.expanduser(filepath)
    filelist = os.path.expanduser(filelist)
    
    with open(filelist, 'ab') as csvfile:
        filewriter = csv.writer(csvfile, delimiter = ",",
                                quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        
        for files in sorted(glob.glob(filepath + "*.xml.gz")):
            filewriter.writerow([files])