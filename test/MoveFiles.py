import os
import shutil

sourcepath = "/Volumes/SAMSUNG/ESCOM/graphs/color/"
thresholds = [50, 100, 150, 200, 250, 300, 350, 400]

sourcepath = os.path.expanduser(sourcepath)
filepath = sourcepath.rsplit("/", 2)[0]
filepath = os.path.expanduser(filepath)

redpath = filepath + "/red"
greenpath = filepath + "/green"

for path in [redpath, greenpath]:
    if not os.path.isdir(path):
        os.mkdir(path)

for path in [redpath, greenpath]:
    for threshold in thresholds:
        if not os.path.isdir(path + "/" + str(threshold) + "/"):
            os.mkdir(path + "/" + str(threshold))

for threshold in thresholds:
    print("Moving files with threshold %s" % str(threshold))
    for filename in os.listdir(sourcepath + str(threshold)):
        if "red" in filename:
            if not os.path.isfile(redpath + "/" + str(threshold) + "/" + filename):
                shutil.move(sourcepath + str(threshold) + "/" + filename,
                            redpath + "/" + str(threshold) + "/" + filename)
            else:
                print "File already exists: "
                print redpath + "/" + str(threshold) + "/" + filename
        elif "green" in filename:
            if not os.path.isfile(greenpath + "/" + str(threshold) + "/" + filename):
                shutil.move(sourcepath + str(threshold) + "/" + filename,
                            greenpath + "/" + str(threshold) + "/" + filename)
            else:
                print "File already exists:"
                print greenpath + "/" + str(threshold) + "/" + filename
                
"""
if not os.path.isfile(filepath + filename):
        shutil.move(sourcepath + filename, filepath + filename)
    else:
        # Prevent files from being erroneously overwritten.
        print file
        print "exists"

for file in os.listdir(sourcepath):
    
    print file
    
    for threshold in thresholds:
        if (file.endswith("_" + str(threshold) + ".xml.gz") or 
            file.endswith("_" + str(threshold) + ".png")):
            
            if not os.path.isfile(filepath + str(threshold) + "/" + file):
                shutil.move(sourcepath + file, filepath + str(threshold) + "/" + file)
            else:
                # Prevent files from being erroneously overwritten.
                print "exists"
"""