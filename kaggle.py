import os
import shutil

source_dir = '/kaggle/input/12341234'
target_dir = '/opt/conda/'

for root, dirs, files in os.walk(source_dir):

  for filename in files:

    # Формирование путей
    relative_path = os.path.relpath(root, source_dir)
    source_path = os.path.join(root, filename)
    target_path = os.path.join(target_dir, relative_path, filename)

    # Копирование файла, если не существует    
    if not os.path.exists(target_path):
      os.makedirs(os.path.dirname(target_path), exist_ok=True)
      shutil.copy2(source_path, target_path)

  # Копирование папок
  for dir_name in dirs:
    
    source_path = os.path.join(root, dir_name)  
    relative_path = os.path.relpath(source_path, source_dir)
    target_path = os.path.join(target_dir, relative_path)

    if not os.path.exists(target_path):
      os.makedirs(target_path)