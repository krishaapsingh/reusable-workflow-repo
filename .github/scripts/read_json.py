# File: .github/scripts/read_json.py
import sys
import json

def read_json_values(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def main():
    json_file_path = sys.argv[1] if len(sys.argv) > 1 else None

    if not json_file_path:
        print("Please provide the path to the JSON file as a command-line argument.")
        sys.exit(1)

    json_values = read_json_values(json_file_path)

    if json_values:
        print("JSON values:")
        for key, value in json_values.items():
            print(f"{key}: {value}")
    else:
        print("Failed to read JSON values.")

if __name__ == "__main__":
    main()
