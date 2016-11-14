import os, csv, shutil, glob

# thresholds = [50, 100, 150, 200, 250, 300, 350, 400]
colours = ["red", "blue", "green"]
thresholds = [150, 200, 250]

for colour in colours:
    for threshold in thresholds:
        filepath = "/Volumes/SAMSUNG/MOSI/graphs/" + colour + "/" + str(threshold) + "/"
        # filepath = "/Volumes/SAMSUNG/ESCOM/graphs/colorgraphs/" + str(threshold) + "/"
    
        filelist = "../" + colour + "_" + str(threshold) + ".txt"
        filepath = os.path.expanduser(filepath)
        filelist = os.path.expanduser(filelist)
    
        with open(filelist, 'ab') as csvfile:
            filewriter = csv.writer(csvfile, delimiter = ",",
                                    quotechar = '|', quoting = csv.QUOTE_MINIMAL)
            
            for files in sorted(glob.glob(filepath + "*.xml.gz")):
                filewriter.writerow([files])