#Import os & shutil modules.

import os
import shutil

#Create two variables from_dir and to_dir
# to store source path and destination path, respectively.

from_dir  = 'C:/Users/Krishna Krupa/Downloads'
to_dir = 'F:/download moving'

#Create a variable, list_of_files , 
# to store the names of all the files from the source path using os.listdir()

listOFfiles = os.listdir(from_dir)

#Print the list_of_files 
# to check in the terminal by running the code.
print(listOFfiles)

#Create a for-in loop to traverse through the list_of_files

for file_name in listOFfiles:

    #Use os.path.splitext() on each file name 
    # to capture the name & extension of each file.

    n,ext = os.path.splitext(file_name)
    
    #an if condition 
    # to check if the extension is blank, if the condition is true then continue.
    if ext == '':
        continue
    if ext in [ '.txt', '.doc', '.docx', '.pdf']:
        #Create path1 as the name of the source path.
        p1 = from_dir + '/'+file_name
        #Create path2 ;new folder with that extension name and move the files to that folder.
        p2 = to_dir+ '/'+ "docs"
        #destination path
        p3 = to_dir+'/'+ "docs"+'/'+file_name

#check if the folder/directory path exists before moving
        if os.path.exists(p2):
            print("Moving "+file_name+"....")
            shutil.move(p1,p3)

        else:
            os.makedirs(p2)
            print("Moving "+file_name+"...")
            shutil.move(p1,p3)