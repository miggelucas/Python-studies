import os
import shutil
import re


path = r"\Users\Marta Migge\Desktop\test_folder"
files = os.listdir(path)
# make dirs

folder_name = []

for file in files:
    if "." in file:     # espero que não tenha nenhuma pasta com . no nome
        file_split = re.split("\.", str(file))
        file_type = file_split[1]
        if file_type not in folder_name:
            folder_name.append(file_type)        # verifica e coloca numa lista as terminações dos arquivos


for x in range(0, len(folder_name)):
    if not os.path.exists(path + r"\\" + folder_name[x]):
        os.makedirs(path + r"\\" + folder_name[x])      # cria pastas com os nomes na lista

# move files

for file in files:

    if "." in file:
        file_split = re.split("\.", str(file))
        file_type = file_split[1]

        for folder in folder_name:
            if file_type == folder:
                shutil.move(path + r"\\" + file, path + r"\\" + folder) # move os arquivos para as pastas de sua terminação
