import os
import json
import mimetypes
import threading
from permissions_manager import grant_write_permission
from clear_console import clear_console
from loading import loading
from toggle import toggle_running

def read_existing_json(output_json_path):
    # Reads existing JSON data from a specified file path
    existing_files_data = []
    if os.path.exists(output_json_path):
        try:
            with open(output_json_path, 'r', encoding='utf-8') as existing_json:
                existing_files_data = json.load(existing_json)
        except UnicodeDecodeError:
            try:
                with open(output_json_path, 'r', encoding='latin-1') as existing_json:
                    existing_files_data = json.load(existing_json)
            except (UnicodeDecodeError, json.JSONDecodeError):
                try:
                    with open(output_json_path, 'rb') as existing_json:
                        existing_files_data = json.load(existing_json, encoding='latin-1')
                except Exception as e:
                    print(f"Error reading existing JSON file: {e}")
    return existing_files_data

def update_files_data(existing_files_data, directory_path):
    # Updates files data based on the content of files in the specified directory
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        file_content = file.read()
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

            file_exists_in_json = False
            for file_data in existing_files_data:
                if file_data['filename'] == file_name:
                    file_data['content'] = file_content
                    file_data['full_path'] = file_path
                    file_exists_in_json = True

            if not file_exists_in_json:
                mime_type, _ = mimetypes.guess_type(file_path)
                file_type = mime_type if mime_type else "unknown"

                new_file_data = {
                    'filename': file_name,
                    'content': file_content,
                    'full_path': file_path,
                    'file_type': file_type
                }
                existing_files_data.append(new_file_data)

        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            update_files_data(existing_files_data, subdir_path)

    return existing_files_data

def write_json(files_data, output_json_path):
    # Writes JSON data to a specified file path
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(files_data, json_file, ensure_ascii=False, indent=2)

def process_directory(directory_path, output_json_path):
    print("\nChecks whether the json file exists...")
    existing_files_data = read_existing_json(output_json_path)

    if not toggle_running.get_toggle_status():
        print("Loading is already running. Please wait...")
        return

    print("Updating...\n")
    toggle_running.set_toggle_status(True)  # Set toggle to True before starting loading
    loading_thread = threading.Thread(target=loading)
    loading_thread.start()

    try:
        updated_files_data = update_files_data(existing_files_data, directory_path)
    finally:
        toggle_running.set_toggle_status(False)  # Set toggle back to False on completion or error
        loading_thread.join()  # Wait for the loading thread to finish

    print("\n\nWrite in json file...")
    write_json(updated_files_data, output_json_path)
    print("Content cleared and updated successfully!")
