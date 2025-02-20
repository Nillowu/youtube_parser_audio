import yt_dlp


COOKIES_PATH = "cookies.txt"

def download_audio(playlist_url: str, output_path: str = '.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(playlist_title)s/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }],
        'ffmpeg_location': r'C:\Users\oles9\Downloads\ffmpeg-2025-01-13-git-851a84650e-essentials_build\ffmpeg-2025-01-13-git-851a84650e-essentials_build\bin\ffmpeg.exe',
        'http_headers': {'User-Agent': 'Mozilla/5.0'},  # Избегаем SSL-ошибки
        'nocheckcertificate': True,  # Игнорируем SSL-ошибки
        'geo_bypass': True,  # Обход региональных ограничений
        'ignoreerrors': True,  # Пропускаем удалённые видео
        'cookiefile': COOKIES_PATH,  # Путь к файлу с куки
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"Playlist has been successfully downloaded to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


video_url = "https://www.youtube.com/watch?v=TMmv29SloFw&list=PLNj9MGbh_4S_PU38V9wli-Mr28Vt8FtS1&ab_channel=MELOMANMUSIC" #сюда ссылку на плейлист
download_audio(video_url)
