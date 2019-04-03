# Notes:

# Instead of manually making new separate folders for X amount of binary files you have,
# use this python script to automatically create folders based off of the binary file name

import glob, os, shutil

folder = 'V:/users/Edward/OFF' #Input the directory you want to make the folders in

for file_path in glob.glob(os.path.join(folder, '*.*')): #  *.* wildcard will match any file that has an extension
    new_dir = file_path.rsplit('.', 1)[0]  #  . is the delimiter, splits once, and grabs first item in list (which is the file name)
    os.mkdir(os.path.join(folder, new_dir)) #  Creates new directory with new given name from the file
    shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path))) #  Moves given file to the new directory that was created
