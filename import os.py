import os
import shutil

from_dir = "C:/Users/Swara/Downloads"
to_dir = "C:/Users/Swara/OneDrive/Desktop/HELLO"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for files_name in list_of_files :
 name,extension=os.path.splitext(files_name)
 print(name)
 print(extension)