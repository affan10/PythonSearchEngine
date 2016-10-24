import sys
import os
import os.path
import shutil
import glob
import ntpath

dict = {}
dict2 = {}
check = 1
check1 = 0
counter = 0

while(check):
    file_in= raw_input('Enter keyword: ')
    #temp_str = file.split('.')

    for root, dirs, files in os.walk("E:\\"):
        for file in files:
            if file.endswith(".txt"):
                counter += 1
                print(os.path.join(root, file))
                file_paths = os.path.join(root, file)
                dict[counter] = file_paths
                file_name = ntpath.basename(file_paths)
                print file_name

                if file_in in open(file_paths).read():
                    print "Keyword found in: "+ file_in
                    check1 += 1
                    dict2[file_name] = file_paths

    print "Keyword available in these files:\n"
    print dict2
    print "\n"
