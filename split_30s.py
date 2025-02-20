from pydub import AudioSegment
import os
import random


def trim_random_30s(file_path: str):
    output_path = file_path.replace('.wav', '_trimmed.wav')

    try:
        audio = AudioSegment.from_wav(file_path)
    except Exception as e:
        print(f'Error loading file {file_path}: {e}')
        return

    duration = len(audio) / 1000

    if duration <= 30:
        print(f'The audio {file_path} is shorter than 30 seconds, deleting.')
        os.remove(file_path)
        return


    for i in range(n): # если хотим один видос порезать n раз по 30 секунд (надо закоменить предыдущие пять строк и добавить в функцию n)
        start_time = random.uniform(0, duration - 30) * 1000  # Перевод в миллисекунды
        trimmed_audio = audio[start_time:start_time + 30 * 1000]

        output_path = file_path.replace('.wav', f'_trimmed_{i + 1}.wav')
        trimmed_audio.export(output_path, format='wav')
        print(f'Trimmed file saved: {output_path}')

    os.remove(file_path)

def process_files_in_directory(directory_path: str):
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)#

        if os.path.isfile(file_path) and file.lower().endswith('.wav'):
            print(f'Processing file: {file}')
            trim_random_30s(file_path)


process_files_in_directory("BEST PHONK MIX PLAYLIST - Phonk Music 2025")