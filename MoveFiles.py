import os
import shutil

sourcepath = "/Volumes/SAMSUNG/colorgraphs/"
filepath = "/Volumes/SAMSUNG/ESCOM/Graphs/20160602/"
thresholds = [50, 100, 150, 200, 250, 300, 350, 400] # [500, 600, 700, 800, 900]


if not os.path.isdir(filepath):
    os.mkdir(filepath)

for threshold in thresholds:
    if not os.path.isdir(filepath + str(threshold) + "/"):
        os.mkdir(filepath + str(threshold))

for file in os.listdir(sourcepath):
    for threshold in thresholds:
        if (file.endswith("_" + str(threshold) + ".xml.gz") or 
            file.endswith("_" + str(threshold) + ".png")):
            shutil.move(sourcepath + file, filepath + str(threshold) + "/" + file)