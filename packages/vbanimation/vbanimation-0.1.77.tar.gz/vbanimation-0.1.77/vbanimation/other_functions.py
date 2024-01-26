from pydub.utils import mediainfo

def chunk_words(s, n):
    words = s.split()
    return [' '.join(words[i:i+n]) for i in range(0, len(words), n)]

def get_audio_duration(file_path):
    info = mediainfo(file_path)
    duration = round(float(info['duration']))
    return duration