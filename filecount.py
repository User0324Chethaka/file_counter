import os

def get_files(path, ls):
    for element in os.scandir(path=path):
        if element.is_dir() and os.listdir(element.path) != []:
            get_files(element.path, ls)
        elif element.is_file():
            ls.append(element.name)

file_ls: list[os.DirEntry] = []
path_: str = input("path: ")

get_files(path=path_, ls=file_ls)

file_types: set = {a.split(".")[-1] for a in file_ls}

print('\n****************************\n')
print(f'file count: {len(file_ls)}')
print(f'types of files: {file_types}')
print('\n****************************\n')