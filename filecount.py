import os
import json

def get_files(path, ls):
    elements = os.scandir(path=path)
    for element in elements:
        if element.is_dir():
            get_files(element.path, ls)
        else:
            ls.append(element.name)

file_ls = []
path_ = input("path: ")

get_files(path=path_, ls=file_ls)

file_types = {a.split(".")[-1] for a in file_ls}

print(f'file count: {len(file_ls)}')
print(f'types of files: {file_types}')
