import shutil
import os

# Path of the file to be moved
with open('', 'r') as f:
    my_list = [line.strip() for line in f.readlines()]

list_item = []
list_file_name = []
for item in my_list:
    folder_name = item.split('\\')
    list_item.append(folder_name[-2])

for item in list_item:
    filename, extension = os.path.splitext(item)
    list_file_name.append(filename)
print(list_file_name)
