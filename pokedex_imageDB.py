import os
import shutil

root_folder = 'D:/VS Code Files/Projects/PowerBI Projects/Datasets/PokedexDB/Pokemon Images DB'
destination_folder = 'D:/VS Code Files/Projects/PowerBI Projects/Datasets/PokedexDB/ConsolidatedImageDB'

os.makedirs(destination_folder, exist_ok = True)

for subdir, _, files in os.walk(root_folder):
    pokemon_name = os.path.basename(subdir)
    for file in files:
        if file == f'{pokemon_name}.png':
            file_path = os.path.join(subdir, file)
            new_file_path = os.path.join(destination_folder, file)
            shutil.copy(file_path, new_file_path)

print("Images have been consolidated successfully.")

