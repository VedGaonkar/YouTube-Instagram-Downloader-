# 🎵 YouTube & Instagram Downloader

A simple, all-in-one tool to download **YouTube videos, music (MP3), and Instagram reels** using Python and `yt-dlp`.

---

## 🚀 Features
- 🎬 YouTube Video Downloader (`YT Video Down.bat`)
- 🎧 YouTube Music Downloader (`YT Music Down.bat`)
- 📱 Instagram Reels Downloader (`Insta Reels Down.bat`)
- Automatically saves to folders: `Videos`, `Music`, `Reels`
- Runs directly from terminal or double-click `.bat` file — no setup needed

---

## 🧰 Requirements
- **Python 3.8+**
- **yt-dlp**
- **ffmpeg** (for audio extraction)

### 📦 Install Dependencies
Open Command Prompt and run:
```bash
pip install yt-dlp
```

### ⚙️ FFmpeg Setup

FFmpeg is required for audio extraction.

**Windows:**
1. Download from [ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract → move to `C:\Program Files\ffmpeg`
3. Add `C:\Program Files\ffmpeg\bin` to system **PATH**
4. Verify installation:
   ```bash
   ffmpeg -version
