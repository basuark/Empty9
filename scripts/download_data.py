# This script downloads data from kaggle 
# The files are then saved to data/external folder

# Importing libraries
import os
import opendatasets as od

curr_dir =  os.path.dirname(__file__)
download_dir = os.path.join(curr_dir,"..\\data\\external")

# Setting path
os.chdir(download_dir)
# Here is the URL from where the data is being downloaded
download_link = "https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset"


# Downloading starts here
try:
    od.download(download_link)
except:
    print(" Some unexpected Eror")