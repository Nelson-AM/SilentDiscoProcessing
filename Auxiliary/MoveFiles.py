import os
import shutil


# sourcepath = "/Volumes/SAMSUNG/fullgraphs20160623/250/"
sourcepath = "~/Desktop/colorgraphs/400/"
# filepath = "~/Desktop/fullgraphs/"
filepath = "/Volumes/SAMSUNG/colorgraphs/400/"
# filepath = "/Volumes/SAMSUNG/ESCOM/Graphs/20160602/"
# thresholds = [50, 100, 150] #, 200, 250, 300, 350, 400]
# thresholds = [150, 200, 250]

sourcepath = os.path.expanduser(sourcepath)
filepath = os.path.expanduser(filepath)

if not os.path.isdir(filepath):
    os.mkdir(filepath)

# for threshold in thresholds:
#    if not os.path.isdir(filepath + str(threshold) + "/"):
#        os.mkdir(filepath + str(threshold))

for file in os.listdir(sourcepath):
    
    if not os.path.isfile(filepath + file):
        shutil.move(sourcepath + file, filepath + file)
    else:
        # Prevent files from being erroneously overwritten.
        print file
        print "exists"

"""
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