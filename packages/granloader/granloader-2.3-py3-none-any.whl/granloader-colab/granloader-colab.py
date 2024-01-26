!pip install yt-dlp
!pip install ffmpeg-python

import  os
import  subprocess
from    datetime        import  datetime
import  ipywidgets      as      widgets
import  urllib.parse    as      urlparse
from    IPython.display import  clear_output, display
import  time
import  re
import  json
import  threading
import  string

clear_output(wait=False)

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
    upload_date = video_info.get("upload_date")
    upload_time = video_info.get("timestamp")
    return upload_date, upload_time

def get_video_title(link):
    cmd = ["yt-dlp", "--get-title", link]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    return result.stdout.strip()

def get_video_info(link):
    cmd = ["yt-dlp", "-F", link]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    lines = result.stdout.split('\n')
    video_lines = [line for line in lines if "mp4" in line and "video" in line]
    max_resolution = 0
    for line in video_lines:
        match = re.search(r'(\d{3,4})x(\d{3,4})', line)
        if match:
            width, height = map(int, match.groups())
            max_resolution = max(max_resolution, height)
    return max_resolution

def sanitize_filename(title):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_filename = ''.join(c for c in title if c in valid_chars)
    return sanitized_filename

def get_bitrate(file_path):
    cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=bit_rate', '-of', 'json', file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    info = json.loads(result.stdout)
    bitrate = int(info['streams'][0]['bit_rate']) // 1000
    return bitrate

def get_total_size(files):
    return sum(os.path.getsize(file) for file in files if os.path.exists(file))

def split_and_convert_video(input_file, output_file, segment_duration, folder_path):
    segment_prefix = os.path.join(folder_path, "segment_")
    converted_prefix = os.path.join(folder_path, "converted_")

    cmd_split = ["ffmpeg", "-i", input_file, "-c", "copy", "-f", "segment", "-segment_time", str(segment_duration), "-reset_timestamps", "1", f"{segment_prefix}%03d.mp4"]
    subprocess.run(cmd_split)

    segments = sorted([file for file in os.listdir(folder_path) if file.startswith("segment_") and file.endswith(".mp4")])
    total_segments = len(segments)
    total_size_original = get_total_size([os.path.join(folder_path, s) for s in segments])

    converted_segments = []
    for i, segment in enumerate(segments, 1):
        segment_path = os.path.join(folder_path, segment)
        converted_segment = converted_prefix + segment[8:]
        cmd_convert = ["ffmpeg", "-hwaccel", "cuda", "-i", segment_path, "-c:v", "h264_nvenc", "-preset", "fast", "-c:a", "aac", converted_segment]

        conversion_thread = threading.Thread(target=lambda: subprocess.run(cmd_convert))
        conversion_thread.start()

        while conversion_thread.is_alive():
            total_size_converted = get_total_size([os.path.join(folder_path, s) for s in converted_segments + [converted_segment]])
            clear_output(wait=True)
            print(f"\rConvertendo arquivos: {i} / {total_segments}\nArquivo original:   {total_size_original / (1024**2):.2f} MB\nTamanho convertido: {total_size_converted / (1024**2):.2f} MB\n", end='')
            time.sleep(1)

        conversion_thread.join()
        converted_segments.append(converted_segment)

    with open(os.path.join(folder_path, "filelist.txt"), "w") as f:
        for segment in converted_segments:
            f.write(f"file '{segment}'\n")

    cmd_join = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", os.path.join(folder_path, "filelist.txt"), "-c", "copy", output_file]
    subprocess.run(cmd_join)

    for file in segments + converted_segments + ["filelist.txt"]:
        os.remove(os.path.join(folder_path, file))

def download_video(link, extension):
    video_id = get_video_id(link)
    if video_id is None:
        print("Link inválido.")
        return None, None

    video_title = get_video_title(link)
    max_resolution = get_video_info(link)
    final_resolution = "1080p" if max_resolution <= 1080 else f"{max_resolution}p"
    print(f"Resolução: {final_resolution}")

    date_folder = datetime.now().strftime("%Y-%m-%d")
    folder_id = "DOWNLOADER"
    folder_path = f"/content/{folder_id}/{date_folder}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    output_video = os.path.join(folder_path, "video.mp4")
    output_audio = os.path.join(folder_path, "audio.mp4")
    final_output = os.path.join(folder_path, sanitize_filename(video_title) + extension)
    output_converted = os.path.join(folder_path, sanitize_filename(video_title) + "_c" + extension)

    progress_pattern = re.compile(r'\[download\]\s+(\d+\.?\d*%)\s+of\s+(\d+\.?\d*\w+)')

    print("Iniciando download do vídeo...")
    cmd_video = ["yt-dlp", "-f", "bestvideo", "-o", output_video, link]
    process_video = subprocess.Popen(cmd_video, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    video_download_output = ""
    for line in iter(process_video.stdout.readline, ''):
        video_download_output += line
        match = progress_pattern.search(line)
        if match:
            progress, total_size = match.groups()
            clear_output(wait=True)
            print(f"Download do vídeo: {progress} de {total_size}")

    if not os.path.exists(output_video):
        print("Erro ao baixar o vídeo. Detalhes do erro:")
        print(video_download_output)
        return None, None

    print("Iniciando download do áudio...")
    cmd_audio = ["yt-dlp", "-f", "bestaudio", "-o", output_audio, link]
    process_audio = subprocess.Popen(cmd_audio, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    for line in iter(process_audio.stdout.readline, ''):
        match = progress_pattern.search(line)
        if match:
            progress, total_size = match.groups()
            clear_output(wait=True)
            print(f"Download do áudio: {progress} de {total_size}")

    if not os.path.exists(output_audio):
        print("Erro ao baixar o áudio.")
        return None, None

    clear_output(wait=True)
    print("Mesclando áudio e vídeo...\nSegmentando arquivo final para conversão em H.264")
    cmd_merge = ["ffmpeg", "-i", output_video, "-i", output_audio, "-c", "copy", final_output]
    merge_result = subprocess.run(cmd_merge)
    if merge_result.returncode != 0:
        print("Erro ao mesclar áudio e vídeo.")
        return None, None

    clear_output(wait=True)
    output_converted = os.path.join(folder_path, sanitize_filename(video_title) + "_converted.mp4")
    split_and_convert_video(final_output, output_converted, 900, folder_path)

    os.remove(output_video)
    os.remove(output_audio)
    os.remove(final_output)

    if os.path.exists(output_converted):
        print(f"Conversão concluída. Arquivo final: {output_converted}")
        return output_converted, video_title
    else:
        print("Erro na conversão do vídeo.")
        return None, None

def get_video_resolution(file_path):
    if not os.path.exists(file_path):
        return None, None
    cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'json', file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    info = json.loads(result.stdout)
    if 'streams' in info and len(info['streams']) > 0:
        width = info['streams'][0]['width']
        height = info['streams'][0]['height']
        return width, height
    else:
        return None, None

def convert_video_if_needed(input_file, original_title, extension):
    width, height = get_video_resolution(input_file)
    sanitized_title = sanitize_filename(original_title)
    output_file = os.path.join(os.path.dirname(input_file), sanitized_title + extension)

    if height is None or height < 1080:
        temp_output_file = os.path.join(os.path.dirname(input_file), "temp" + extension)
        cmd_convert = ["ffmpeg", "-hwaccel", "cuda", "-i", input_file, "-vf", "scale=1920:1080", "-c:a", "copy", temp_output_file]

        conversion_thread = threading.Thread(target=lambda: subprocess.run(cmd_convert))
        conversion_thread.start()
        while conversion_thread.is_alive():
            if os.path.exists(temp_output_file):
                converted_size = os.path.getsize(temp_output_file)
                original_size = os.path.getsize(input_file)
                progress = (converted_size / original_size) * 100
                print(f"Progresso: {progress:.2f}%", end='\r')
                time.sleep(0.5)

        conversion_thread.join()
        if os.path.exists(temp_output_file):
            os.rename(temp_output_file, output_file)
            os.remove(input_file)
            return output_file, "1080p"
        else:
            print("Erro na última etapa.")
            return None, "Erro na última etapa"
    else:
        os.rename(input_file, output_file)
        return output_file, f"{height}p"


def on_button_click(button, extension):
    clear_output(wait=True)
    link = link_input.value
    if link:
        final_output, video_title = download_video(link, extension)
        if final_output:
            final_output, final_height = convert_video_if_needed(final_output, video_title, extension)
            if final_output:
                clear_output(wait=True)
                print(f"Concluído!\nResolução: {final_height}\n\nLocalizado em:\n{final_output}")
            else:
                print("Erro ao salvar o vídeo.")
        else:
            print("Erro ao realizar o download.")
        display(widgets.HBox([yes_button, no_button]))

def on_mp4_click(button):
    on_button_click(button,'.mp4')

def on_mkv_click(button):
    on_button_click(button,'.mkv')

def on_mov_click(button):
    on_button_click(button,'.mov')

def on_yes_click():
    yes_button.layout.visibility  = 'hidden'
    no_button.layout.visibility   = 'hidden'
    link_input.value = ''
    clear_output(wait=True)
    display(link_input)
    display(mp4_button)
    display(mkv_button)
    display(mov_button)

def on_no_click():
    yes_button.layout.visibility  = 'hidden'
    no_button.layout.visibility   = 'hidden'
    link_input.close()
    mp4_button.close()
    mkv_button.close()
    mov_button.close()
    clear_output(wait=True)
    print("Processo encerrado. Para iniciar novamente, aperte o botão de início ou 'Shift+F9'.")

def on_cancel_click(button):
# falta aqui ainda
    print("Processo cancelado pelo usuário. Reinicie o ambiente de execução para começar novamente.")

cancel_button = widgets.Button(description="Cancelar")
cancel_button.on_click(on_cancel_click)

link_input  = widgets.Text  (description="Link da aula:")
yes_button  = widgets.Button(description="Baixar novo vídeo")
no_button   = widgets.Button(description="Encerrar")

mp4_button = widgets.Button(description=".MP4")
mkv_button = widgets.Button(description=".MKV [NÃO USAR]")
mov_button = widgets.Button(description=".MOV [NÃO USAR]")

mp4_button.on_click(on_mp4_click)
mkv_button.on_click(on_mkv_click)
mov_button.on_click(on_mov_click)

yes_button.on_click(lambda b: on_yes_click())
no_button.on_click(lambda b: on_no_click())

yes_button.layout.visibility = 'hidden'
no_button.layout.visibility  = 'hidden'

display(link_input)
display(mp4_button)
display(mkv_button)
display(mov_button)
display(widgets.HBox([yes_button, no_button]))