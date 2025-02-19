import subprocess
import os
import random

def trim_random_30s(file_path: str):
    output_path = file_path.replace('.wav', "_trimmed.wav")

    cmd_duration = [
        'ffprobe', '-i', file_path, "-show_entries", 'format=duration',
        '-v', "quiet", '-of', 'csv=p=0'
    ]
    result = subprocess.run(cmd_duration, capture_output=True, text=True)

    try:
        duration = float(result.stdout.strip())
    except ValueError:
        print(f'Error of getting duration: {file_path}')
        return

    if duration <= 30:
        print(f"The audio {file_path} is shorter than 30 seconds, deleting.")
        os.remove(file_path)
        return

    start_time = random.uniform(0, duration - 30)

    cmd_trim = [
        "ffmpeg", '-i', file_path, '-ss', str(start_time), '-t', '30',
        '-acodec', 'pcm_s16le', output_path, '-y'
    ]
    subprocess.run(cmd_trim, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(file_path)
    print(f'Trimmed file saved: {output_path}')

def process_files_in_directory(directory_path: str):
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)

        if os.path.isfile(file_path):
            print(f"Processing file: {file}")
            trim_random_30s(file_path)


process_files_in_directory("русский хайперпоп")