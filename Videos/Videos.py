import os
import yt_dlp

# Folder where videos will be saved
output_folder = r"A:\Downloader\Videos"
os.makedirs(output_folder, exist_ok=True)

# yt-dlp options for best video+audio merged in MP4
options = {
    'format': 'bestvideo+bestaudio/best',  # highest quality combo
    'outtmpl': os.path.join(output_folder, "%(title)s.%(ext)s"),
    'merge_output_format': 'mp4',
    'quiet': False,
    'noplaylist': True,
    'retries': 5,
    'fragment_retries': 10,
    'concurrent_fragment_downloads': 5,
    'http_chunk_size': 10485760,  # 10 MB chunks
    'no_warnings': True,
    'progress_hooks': [lambda d: print(f"⏬ {d.get('filename', '')}: {d.get('_percent_str', '').strip()}", end='\r') if d['status'] == 'downloading' else None],
}

print("🎬 YouTube Video Downloader (MP4)")
print("Paste YouTube links one by one.")
print("Type 'exit' to quit.\n")

# Loop for multiple downloads
while True:
    url = input("🔗 Enter YouTube link (or 'exit' to quit): ").strip()
    if url.lower() == "exit":
        print("\n👋 Exiting downloader. Enjoy your videos!")
        break
    if not url:
        continue  # skip empty input

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        print(f"\n✅ Download complete! Saved in {output_folder}\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
