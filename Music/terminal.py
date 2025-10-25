import os
import yt_dlp

# Folder where MP3s will be saved
output_folder = r"A:\Downloader\Music"
os.makedirs(output_folder, exist_ok=True)

# yt-dlp settings
options = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, "%(title)s.%(ext)s"),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'noplaylist': True
}

print("🎶 YouTube to MP3 Downloader")
print("Paste YouTube links one by one.")
print("Type 'exit' to quit.\n")

# Loop for multiple downloads
while True:
    url = input("🎵 Enter YouTube link (or 'exit' to quit): ").strip()
    if url.lower() == "exit":
        print("\n👋 Exiting downloader. Enjoy your music!")
        break
    if not url:
        continue  # skip empty input

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        print(f"✅ Download complete! Saved in {output_folder}\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")
