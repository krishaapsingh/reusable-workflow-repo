# File: .github/scripts/read_json.py
import sys
import json
import requests

def read_json_values(json_url):
    try:
        # Use requests to get the JSON content from the URL
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404)

        # Parse the JSON content
        data = response.json()
        return data
    except Exception as e:
        print(f"Error reading JSON content from URL: {e}")
        return None

def main():
    json_url = sys.argv[1] if len(sys.argv) > 1 else None

    if not json_url:
        print("Please provide the URL to the JSON file as a command-line argument.")
        sys.exit(1)

    json_values = read_json_values(json_url)

    if json_values:
        print("JSON values:")
        for key, value in json_values.items():
            print(f"{key}: {value}")
    else:
        print("Failed to read JSON values.")

if __name__ == "__main__":
    main()
