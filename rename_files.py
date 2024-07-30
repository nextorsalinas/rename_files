import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        # Check if it's a file (not a directory)
        if os.path.isfile(os.path.join(directory, filename)):
            # Use a regular expression to remove everything before the first underscore including the underscore
            new_name = re.sub(r'^\d+_', '', filename)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f'Renamed: {filename} -> {new_name}')

if __name__ == "__main__":
    directory = r'ruta/al/directorio'  # Reemplaza con la ruta al directorio con tus archivos
    rename_files(directory)


