# TYPE MOVER: copies all the specified filetypes found in one directory to another

import os
import shutil


types = ['pdf']
ignoreKeywords = ['readme']
storageFolder = 'documents'
searchFolder = '/'

if not os.path.isdir(storageFolder):
    os.mkdir(storageFolder)

fileTypes = []  # adds . extension to file type
for t in types:
    fileTypes.append('.' + t)


count = 0
size = 0

for folderName, subfolders, files in os.walk(searchFolder):
    for file in files:
        path = folderName + '/' + file  # builds the path string
        for ext in fileTypes:  # loops through the file types
            if ext in path:
                for key in ignoreKeywords:
                    if key not in path.lower():  # ignores readme files
                        print('Moved ' + path)
                        count += 1
                        size += os.path.getsize(path)
                        shutil.copy(path, storageFolder)  # copy command - be sure to comment out when debugging


# formats a large byte size into KB, MB, etc
def humanreadable(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)

print('\nCopy complete. Copied ' + str(count) + ' files totaling ' + humanreadable(size))
