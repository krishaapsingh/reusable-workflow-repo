# File: .github/scripts/read_json.py
import sys
import json
import requests
from pathlib import Path

def download_json_file(json_url, download_path):
    try:
        # Use requests to get the JSON content from the URL
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404)

        # Check if the response content is JSON
        if 'application/json' in response.headers['content-type']:
            # Save the JSON content to a file
            with open(download_path, 'w') as file:
                file.write(response.text)
            return True
        else:
            print(f"The content at {json_url} is not a JSON file.")
            return False
    except Exception as e:
        print(f"Error downloading JSON content from URL: {e}")
        return False

def read_json_values(json_file_path):
    try:
        # Parse the JSON content
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def main():
    json_url = sys.argv[1] if len(sys.argv) > 1 else None

    if not json_url:
        print("Please provide the URL to the JSON file as a command-line argument.")
        sys.exit(1)

    # Extract the filename from the URL and append it with .json
    json_file_name = Path(json_url).name
    json_file_path = Path.cwd() / json_file_name

    if download_json_file(json_url, json_file_path):
        json_values = read_json_values(json_file_path)

        if json_values:
            print("JSON values:")
            for key, value in json_values.items():
                print(f"{key}: {value}")
        else:
            print("Failed to read JSON values.")
    else:
        print("Failed to download JSON file.")

if __name__ == "__main__":
    main()
