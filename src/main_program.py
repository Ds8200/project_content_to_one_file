import os
import json
from directory_processor import process_directory
from permissions_manager import grant_write_permission
from clear_console import clear_console
from select_directory import get_valid_directory_path

def main():
    # Print program name and description
    print("========== Create JSON from Directory Program ===========")
    print("\nThis program processes a directory,\ncreates or updates a JSON file,\nand grants write permission to the output JSON.\n")

    # Get and validate source directory path
    input("Press Enter to select source directory...")
    print("Select the folder...")
    source_directory = get_valid_directory_path("Enter source directory:")
    print("Source directory path: ", source_directory)

    # Get and validate JSON output path
    input("\nPress Enter to select JSON output path...")
    json_output_path = get_valid_directory_path("Enter JSON output path:")
    print("Json output_ path: ", json_output_path)

    # Set the output JSON path
    output_json_path = os.path.join(json_output_path, 'output.json')

    try:
        # Process the directory and update JSON
        process_directory(source_directory, output_json_path)
        
        # Grant write permission
        grant_write_permission(output_json_path)  

    except Exception as e:
        # Handle exceptions, such as no write permission
        print(f"Error: {e}")
        print("No write permission for the specified directory.")

    # Wait for Enter key press to exit
    input("\n\n------> Press enter to exit <------")

if __name__ == "__main__":
    main()