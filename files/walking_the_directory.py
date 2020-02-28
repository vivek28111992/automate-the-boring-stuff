import os

for folderName, subFolders, fileNames in os.walk('/home/administrator/automate_the_boring_stuff'):
    print('The folder is ' + folderName)
    print('The subFolders in ' + folderName + ' are:' + str(subFolders))
    print('The filenames in ' + folderName + ' are:' + str(fileNames))
    print()

