import os
import shutil


def merge_audio_folders(source_folder, target_folder):
    for file_name in os.listdir(source_folder):
        source_file = os.path.join(source_folder, file_name)
        target_file = os.path.join(target_folder, file_name)

        if os.path.isfile(source_file):
            if os.path.exists(target_file):
                print(f"Файл {file_name} уже существует в целевой папке, пропускаем.")
            else:
                shutil.copy2(source_file, target_folder)
                print(f"Файл {file_name} скопирован в целевую папку")


source_directory = 'Гиперпоп 2025 - Лучший Гиперпоп Песни 2025 (Russian Hyperpop 2025)'  # Папки с плейлистами которые надо объединить
target_directory = 'русский хайперпоп'

merge_audio_folders(source_directory, target_directory)
