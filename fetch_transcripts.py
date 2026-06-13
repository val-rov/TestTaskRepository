import re
import os
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, RequestBlocked

api = YouTubeTranscriptApi()

VIDEO_LIST = "research/youtube-transcripts/video-list.txt"
OUTPUT_DIR = "research/youtube-transcripts"


def get_video_id(url):
    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
    return match.group(1) if match else None


def get_video_title(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        match = re.search(r'<title>(.*?) - YouTube</title>', response.text)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return None


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:80]


def format_transcript(segments):
    # Join segments, inserting a blank line every ~60 seconds for readability
    lines = []
    block = []
    block_start = 0
    for seg in segments:
        block.append(seg['text'])
        if seg['start'] - block_start >= 60:
            lines.append(' '.join(block))
            block = []
            block_start = seg['start']
    if block:
        lines.append(' '.join(block))
    return '\n\n'.join(lines)


with open(VIDEO_LIST) as f:
    urls = [line.strip() for line in f if line.strip()]

for url in urls:
    video_id = get_video_id(url)
    if not video_id:
        print(f"Warning: could not parse video ID from: {url}")
        continue

    title = get_video_title(url)
    if not title:
        print(f"Warning: could not fetch title for {url}, using video ID")
        title = video_id

    try:
        fetched = api.fetch(video_id)
        segments = [{"text": s.text, "start": s.start} for s in fetched]
    except (NoTranscriptFound, TranscriptsDisabled):
        print(f"Warning: no transcript available for '{title}' ({url})")
        continue
    except Exception as e:
        print(f"Warning: failed to fetch transcript for '{title}' ({url}): {e}")
        continue

    slug = slugify(title)
    filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"**URL:** {url}\n\n")
        f.write("## Transcript\n\n")
        f.write(format_transcript(segments))
        f.write("\n")

    print(f"Saved: {filepath}")
