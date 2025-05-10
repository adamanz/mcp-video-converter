# MCP Video Converter Server

An MCP server that provides tools for checking FFmpeg installation and converting video files between various formats.

## Features

- **Check FFmpeg**: Verifies if FFmpeg is installed and accessible.
- **Convert Video**: Converts video, audio, and image files to various formats (e.g., MP4, WebM, MOV, MP3, PNG).
- **Format Info**: Get a list of supported file formats for conversion.

## Prerequisites

- Python 3.10+
- FFmpeg installed and available in your system's PATH
- [Optional] [uv](https://github.com/astral-sh/uv) for environment management

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mcp-video-converter.git
   cd mcp-video-converter
   ```

2. Create and activate a virtual environment:
   ```bash
   # Using venv (standard library)
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Or using uv (recommended if available)
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   # Using pip
   pip install -e .
   pip install fastmcp
   
   # Or using uv
   uv pip install -e .
   uv pip install fastmcp
   ```

## Running the Server Directly

You can run the server directly:

```bash
# Activate the virtual environment if not already activated
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Run the server
python -m mcp_video_converter.server
```

## Integrating with Claude Desktop

To add this MCP server to Claude Desktop:

1. Locate or create the Claude Desktop configuration file:
   ```bash
   # macOS
   mkdir -p ~/Library/Application\ Support/Claude/
   nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
   
   # Windows
   mkdir -p %APPDATA%\Claude\
   notepad %APPDATA%\Claude\claude_desktop_config.json
   ```

2. Add the MCP server configuration:
   ```json
   {
     "mcpServers": {
       "video-convert": {
         "command": "/bin/bash",
         "args": [
           "-c",
           "cd /absolute/path/to/mcp-video-converter && source .venv/bin/activate && python -m mcp_video_converter.server"
         ]
       }
     }
   }
   ```

   **Windows Alternative:**
   ```json
   {
     "mcpServers": {
       "video-convert": {
         "command": "cmd.exe",
         "args": [
           "/c",
           "cd /d C:\\absolute\\path\\to\\mcp-video-converter && .venv\\Scripts\\activate && python -m mcp_video_converter.server"
         ]
       }
     }
   }
   ```

   Replace `/absolute/path/to/mcp-video-converter` with the absolute path to your repository.

3. Restart Claude Desktop
   - The server will appear as "video-convert" in the MCP tools menu

4. Important notes:
   - Always use absolute paths in your configuration
   - Make sure FFmpeg is installed and in your PATH
   - If you encounter issues, check the Claude Desktop logs:
     ```bash
     # macOS
     tail -n 20 -F ~/Library/Logs/Claude/mcp*.log
     
     # Windows
     type %APPDATA%\Claude\logs\mcp*.log
     ```

## Integrating with Cursor

To add this MCP server to Cursor:

1. Locate or create the Cursor configuration file:
   ```bash
   # macOS
   mkdir -p ~/.cursor/
   nano ~/.cursor/config.json
   
   # Windows
   mkdir -p %USERPROFILE%\.cursor\
   notepad %USERPROFILE%\.cursor\config.json
   ```

2. Add the MCP server configuration:
   ```json
   {
     "ai": {
       "mcpServers": {
         "video-convert": {
           "command": "/bin/bash",
           "args": [
             "-c",
             "cd /absolute/path/to/mcp-video-converter && source .venv/bin/activate && python -m mcp_video_converter.server"
           ]
         }
       }
     }
   }
   ```

   **Windows Alternative:**
   ```json
   {
     "ai": {
       "mcpServers": {
         "video-convert": {
           "command": "cmd.exe",
           "args": [
             "/c",
             "cd /d C:\\absolute\\path\\to\\mcp-video-converter && .venv\\Scripts\\activate && python -m mcp_video_converter.server"
           ]
         }
       }
     }
   }
   ```

   Replace `/absolute/path/to/mcp-video-converter` with the absolute path to your repository.

3. Restart Cursor
   - The server will be available to Claude in Cursor

4. Important notes:
   - Always use absolute paths in your configuration
   - Make sure FFmpeg is installed and in your PATH
   - Logs may be accessed through Cursor's developer tools

## Troubleshooting Common Issues

### Server Not Found

If the MCP server is not being picked up:

1. Verify the paths in your configuration file are absolute and correct
2. Check that FFmpeg is installed and in your PATH
3. Ensure the virtual environment is activated in your command
4. Check the logs for specific error messages

### Python Module Not Found

If you see errors about missing modules:

1. Make sure you installed all dependencies with `pip install -e .` and `pip install fastmcp`
2. Verify the virtual environment is being activated correctly
3. Try reinstalling the package: `pip install -e .`

### FFmpeg Not Found

If FFmpeg cannot be found:

1. Verify FFmpeg is installed: `which ffmpeg` or `where ffmpeg` on Windows
2. Add the FFmpeg directory to your PATH
3. In the configuration, you can specify the full path to FFmpeg:
   ```json
   "env": {
     "PATH": "/usr/local/bin:/usr/bin:/bin:/path/to/ffmpeg/bin"
   }
   ```

## Example Usage (with Claude)

Once integrated, you can ask Claude to perform tasks like:

1. "Check if FFmpeg is installed on my system"
2. "Convert this video file: /path/to/video.webm to MP4 format with high quality"
3. "What video formats can I convert to?"

Claude will use the appropriate tools from the MCP server to accomplish these tasks.

## Advanced: Using with fastmcp client

For programmatic usage, you can use the fastmcp client:

```bash
# Check FFmpeg installation
fastmcp client call <SERVER_URL_OR_FILE_PATH> check_ffmpeg_installed '{}'

# Get supported formats
fastmcp client call <SERVER_URL_OR_FILE_PATH> get_supported_formats '{}'

# Convert a video
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
# Using pip
pip install pytest
pytest

# Using uv
uv pip install pytest
uv run pytest
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.