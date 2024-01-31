import os
import subprocess
from datetime import datetime
import ipywidgets as widgets
from IPython.display import clear_output, display
import re
import json
import string
import threading
import time

def get_video_id(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|live/|.*&v=)?([^&=%\?]{11})')
    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(6)
    return None

def get_upload_date_and_time(link):
    cmd = ["yt-dlp", "-j", link]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    video_info = json.loads(result.stdout)
    return video_info.get("upload_date"), video_info.get("timestamp")

def get_video_title(link):
    cmd = ["yt-dlp", "--get-title", link]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    return result.stdout.strip()

def get_video_info(link):
    cmd = ["yt-dlp", "-F", link]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    lines = result.stdout.split('\n')
    max_resolution = 0
    for line in lines:
        if "mp4" in line and "video" in line:
            match = re.search(r'(\d{3,4})x(\d{3,4})', line)
            if match:
                width, height = map(int, match.groups())
                max_resolution = max(max_resolution, height)
    return max_resolution

def sanitize_filename(title):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_filename = ''.join(c for c in title if c in valid_chars)
    return sanitized_filename

def download_video(link, extension):
    video_id = get_video_id(link)
    if not video_id:
        print("Link inválido.")
        return None, None

    video_title = get_video_title(link)
    max_resolution = get_video_info(link)
    final_resolution = "1080p" if max_resolution <= 1080 else f"{max_resolution}p"

    date_folder = datetime.now().strftime("%Y-%m-%d")
    folder_id = "DOWNLOADER"
    folder_path = f"/content/{folder_id}/{date_folder}"
    os.makedirs(folder_path, exist_ok=True)

    output_video = os.path.join(folder_path, "video.mp4")
    output_audio = os.path.join(folder_path, "audio.mp4")
    final_output = os.path.join(folder_path, sanitize_filename(video_title) + extension)


    def show_progress(process, file_type):
        progress_pattern = re.compile(r'\[download\]\s+(\d+\.?\d*%)\s+of\s+(\d+\.?\d*\w+)')
        while True:
            line = process.stdout.readline()
            if not line:
                break
            match = progress_pattern.search(line)
            if match:
                progress, total_size = match.groups()
                clear_output(wait=True)
                print(f"Download {file_type}: {progress} de {total_size}", end="")

    process_video = subprocess.Popen(["yt-dlp", "-f", "bestvideo[vcodec^=avc][ext=mp4]", "-o", output_video, link], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    show_progress(process_video, "do vídeo")

    process_audio = subprocess.Popen(["yt-dlp", "-f", "bestaudio", "-o", output_audio, link], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    show_progress(process_audio, "do áudio")

    merge_result = subprocess.run(["ffmpeg", "-i", output_video, "-i", output_audio, "-c", "copy", final_output], stderr=subprocess.PIPE)

    try:
        os.remove(output_video)
        os.remove(output_audio)
    except OSError as e:
        print("Erro ao excluir arquivos temporários:", e)

    if merge_result.returncode != 0:
        print("Erro ao mesclar áudio e vídeo.")
        return None, None

    if os.path.exists(final_output):
        clear_output(wait=True)
        print(f"Concluído com sucesso!\n\nArquivo final:\n{final_output}\n\n")
        print("------------------------------------------")
        return final_output, video_title
    else:
        print("\nErro na criação do arquivo final.")
        return None, None

def play_all():
    link_input = widgets.Text(description="Link da aula:")
    mp4_button = widgets.Button(description=".MP4")
    def on_button_click(button, extension):
        clear_output(wait=True)
        url = link_input.value
        if url:
            download_video(url, extension)
        display(link_input, mp4_button)
    mp4_button.on_click(lambda b: on_button_click(b, '.mp4'))
    display(link_input, mp4_button)
    print("\n\n2.4.3")
play_all()