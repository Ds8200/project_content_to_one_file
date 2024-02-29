import os
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys

def get_directory_path(message="Select Folder"):
    app = QApplication(sys.argv)
    folder_path = QFileDialog.getExistingDirectory(None, message, options=QFileDialog.ShowDirsOnly)
    return folder_path

def get_valid_directory_path(prompt):
    # Prompts the user for a valid directory path and returns it
    while True:
        path = get_directory_path(prompt)
        if os.path.isdir(path):
            return path
        else:
            print("Invalid directory path. Please enter a valid directory.")