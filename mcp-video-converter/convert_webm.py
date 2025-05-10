#!/usr/bin/env python3
import asyncio
from mcp_video_converter.tools import convert_video_impl

# Path to the test webm file
TEST_WEBM_FILE = "/Users/adamanzuoni/video-convert/testing/474efcb5-6054-4ccd-942a-4657afacc74e.webm"
OUTPUT_FILE = "/Users/adamanzuoni/video-convert/testing/converted.mp4"

async def main():
    print(f"Converting {TEST_WEBM_FILE} to MP4...")
    
    # Call the convert_video_impl function directly
    result = await convert_video_impl(
        input_file_path_str=TEST_WEBM_FILE,
        output_format="mp4",
        quality="high"
    )
    
    print(f"Conversion result: {result}")
    
    if result["success"]:
        print(f"Successfully converted to: {result['output_file_path']}")
    else:
        print(f"Conversion failed: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    asyncio.run(main())