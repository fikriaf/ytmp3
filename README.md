# YouTube to MP3 Downloader

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A simple and efficient command-line tool to download YouTube videos and convert them to MP3 format with high audio quality.

## Features

- Download YouTube videos as MP3 files
- High-quality audio extraction (192 kbps)
- Automatic library updates on download failures
- Interactive loading animation
- Continuous download mode for multiple files
- Automatic format conversion using FFmpeg

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7 or higher
- FFmpeg (required for audio conversion)

### Installing FFmpeg

**Windows:**
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the archive and add the `bin` folder to your system PATH
3. Verify installation: `ffmpeg -version`

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ytmp3.git
cd ytmp3
```

2. Install required Python packages:
```bash
pip install yt-dlp pytube
```

3. Configure the download destination in `ytmp3.py`:
```python
destination = r"C:\Users\YourUsername\Music"
```

## Usage

### Method 1: Run with Python

```bash
python ytmp3.py
```

### Method 2: Run with Batch File (Windows)

1. Edit `ytmp3.bat` and update the path to your `ytmp3.py` file
2. Double-click `ytmp3.bat` to run

### Interactive Mode

Once started, the program will prompt you to enter a YouTube URL:

```
Masukkan Link Youtube:
>> https://www.youtube.com/watch?v=example
```

The download will begin automatically, and the MP3 file will be saved to your configured destination folder.

## Configuration

Edit the following variables in `ytmp3.py` to customize behavior:

- `destination`: Output directory for downloaded MP3 files
- `preferredquality`: Audio quality (default: 192 kbps)
- `outtmpl`: Output filename template

## Dependencies

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube video downloader
- [pytube](https://github.com/pytube/pytube) - YouTube video metadata extraction
- FFmpeg - Audio/video processing

## Error Handling

The application includes automatic error recovery:
- If a download fails, it automatically updates the yt-dlp library
- Retries the download after library update
- Displays clear status messages throughout the process

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download content you have permission to download.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Fikri Armia Fahmi

## Acknowledgments

- Built with yt-dlp for reliable YouTube downloads
- Uses FFmpeg for high-quality audio conversion
