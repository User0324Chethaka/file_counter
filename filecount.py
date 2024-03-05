import os

def get_files(path, ls):
    for element in os.scandir(path=path):
        if element.is_dir():
            get_files(element.path, ls)
        else:
            ls.append(element.name)

file_ls: list[os.DirEntry] = []
path_: str = input("path: ")

get_files(path=path_, ls=file_ls)

file_types: set = {a.split(".")[-1] for a in file_ls}

print('\n\n****************************\n\n')

print(f'file count: {len(file_ls)}')
print(f'types of files: {file_types}')
