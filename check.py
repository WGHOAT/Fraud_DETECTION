import pandas as pd
import os
folderpath = "/home/ajay/Documents/sleeping_dog_don/FRAUD-DETECTION/dataset/data"
pklfiles = [a for a in os.listdir(folderpath) if a.endswith(".pkl")]
for f in pklfiles:
    path = os.path.join(folderpath,f)
    try:
        files = pd.read_pickle(path)
        print(f"{f}:type={type(files)}")
    except Exception as e:
        print(f"{f} Not loaded type={type(files)}")
        #########################################
