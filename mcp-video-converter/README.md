# MCP Video Converter Server

An MCP server that provides tools for checking FFmpeg installation and converting video files.

## Features

- **Check FFmpeg**: Verifies if FFmpeg is installed and accessible.
- **Convert Video**: Converts video, audio, and image files to various formats (e.g., MP4, WebM, MOV, MP3, PNG).
- **Format Info**: Get a list of supported file formats for conversion.

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended for environment management)
- FFmpeg installed and available in your system's PATH

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mcp-video-converter.git
   cd mcp-video-converter
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   uv pip install -e .
   ```

## Running the Server

You can run the server directly using its CLI entry point:

```bash
mcp-video-converter
```

Or via `fastmcp`:

```bash
fastmcp run src/mcp_video_converter/server.py
```

## Example Usage (with `fastmcp client`)

Assuming the server is running:

**Check FFmpeg installation:**

```bash
fastmcp client call <SERVER_URL_OR_FILE_PATH> check_ffmpeg_installed '{}'
```

**Get supported formats:**

```bash
fastmcp client call <SERVER_URL_OR_FILE_PATH> get_supported_formats '{}'
```

**Convert a video:**

```bash
fastmcp client call <SERVER_URL_OR_FILE_PATH> convert_video '{
  "input_file_path": "/path/to/your/video.webm", 
  "output_format": "mp4", 
  "quality": "high"
}'
```
Replace `/path/to/your/video.webm` with an actual video file path.

## Supported Formats

- **Video**: MP4, WebM, MOV, AVI, MKV, FLV, GIF
- **Audio**: MP3, WAV, OGG, AAC, M4A
- **Image**: WebP, JPG, PNG, BMP, TIFF

## Running Tests

```bash
uv run pytest
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.