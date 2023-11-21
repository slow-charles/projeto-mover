import os
import shutil

from_dir = "/home/charles/Downloads"
to_dir = "/home/charles/Documentos"

list_of_files = os.listdir(from_dir)

print("Lista de arquivos no diretório de origem:")
print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    file_path = os.path.join(from_dir, file_name)
    destination_path = os.path.join(to_dir, file_name)
    shutil.move(file_path, destination_path)

print("Movimento de arquivos concluído!")
