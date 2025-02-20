import soundfile as sf
import os
import numpy as np


def compare_audio_files(file1, file2):
    try:
        audio1, sr1 = sf.read(file1)
        audio2, sr2 = sf.read(file2)

        if sr1 != sr2:
            print(f"Частоты дискретизации не совпадают: {file1} ({sr1}Hz) и {file2} ({sr2}Hz)")
            return False

        if len(audio1) != len(audio2):
            print(f"Длины аудиофайлов не совпадают: {file1} ({len(audio1)} samples) и {file2} ({len(audio2)} samples)")
            return False
        if np.array_equal(audio1, audio2):
            print(f"Файлы одинаковые: {file1} и {file2}")
            return True
        else:
            print(f"Файлы разные: {file1} и {file2}")
            return False
    except Exception as e:
        print(f"Ошибка при сравнении {file1} и {file2}: {e}")
        return False


def find_and_remove_duplicates(directory_path):
    files = os.listdir(directory_path)
    files = [f for f in files if f.endswith(('.wav', '.flac', '.ogg', '.mp3'))]  # Фильтруем аудиофайлы
    for i, file1 in enumerate(files):
        for file2 in files[i + 1:]:
            file1_path = os.path.join(directory_path, file1)
            file2_path = os.path.join(directory_path, file2)
            if compare_audio_files(file1_path, file2_path):#
                try:
                    os.remove(file2_path)
                    print(f"Удалён дублирующийся файл: {file2_path}")
                except Exception as e:
                    print(f"Ошибка при удалении {file2_path}: {e}")



playlist_dir = "BEST PHONK MIX PLAYLIST - Phonk Music 2025" # сюда путь к плейлисту где все песни

find_and_remove_duplicates(playlist_dir)


