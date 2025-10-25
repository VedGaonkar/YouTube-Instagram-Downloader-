import os
import yt_dlp

# Folder where Instagram Reels will be saved
output_folder = r"A:\Downloader\Reels"
os.makedirs(output_folder, exist_ok=True)

# yt-dlp settings for high-quality Instagram video
options = {
    'format': 'bestvideo+bestaudio/best',  # highest quality available
    'outtmpl': os.path.join(output_folder, "%(title)s.%(ext)s"),
    'merge_output_format': 'mp4',  # output format
    'quiet': False,
    'noplaylist': True,
    'retries': 5,
    'fragment_retries': 10,
    'concurrent_fragment_downloads': 5,  # faster
    'http_chunk_size': 10485760,  # 10MB chunks to avoid timeouts
    'no_warnings': True,
}

print("📸 Instagram Reels Downloader")
print("Paste Instagram Reel links one by one.")
print("Type 'exit' to quit.\n")

# Loop for multiple downloads
while True:
    url = input("🎬 Enter Instagram Reel link (or 'exit' to quit): ").strip()
    if url.lower() == "exit":
        print("\n👋 Exiting downloader. Enjoy your Reels!")
        break
    if not url:
        continue  # skip empty input

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        print(f"✅ Download complete! Saved in {output_folder}\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")
