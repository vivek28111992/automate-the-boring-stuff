import os

os.path.join('folder1', 'folder2', 'folder3', 'file.png')
# 'folder1/folder2/folder3/file.png'

os.sep # seperator

os.getcwd() # get current working directory

os.chdir() # change directory

os.path.abspath() # absolute path

os.path.isabs('../../spam.png') # for checking absolute path, to determine something begins with root folder

os.path.relpath() # gives the relative path between two paths

os.path.dirname() # gives the directory name

os.path.basename() # gives the lastname of path

os.path.exists()

os.path.isfile()

os.path.isdir()

os.path.getsize() # size of file in bytes

os.listdir() # return list of files and folder in list

os.makedirs()


