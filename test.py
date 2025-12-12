#!/usr/bin/env python3

from gofilepy import GofileClient

# Initialize (Token optional for guest upload)
client = GofileClient(token="NGMOYEz1IhRcmJernxOljppYWZw5DXO6")

# Simple Callback for progress
def my_progress(bytes_read):
    print(f"Read: {bytes_read} bytes")

# Upload (Streaming)
try:
    response = client.upload_file(
        file_path="/tmp/tests/ouput/cpva-11-12-2025-no-ads-audio.mp3", 
        folder_id="cb3614e9-ddcb-4ec2-9016-2d4276868363",
        callback=my_progress
    )
    print(f"Uploaded! Download here: {response['downloadPage']}")
except Exception as e:
    print(f"Error: {e}")

