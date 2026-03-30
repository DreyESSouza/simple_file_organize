from tkinter import filedialog
import os

def choose_folder():
    return filedialog.askdirectory()

def create_folders(extensions, selected_folder_files, selected_folder):
    for folder in extensions.keys():
        if folder not in selected_folder_files:
            os.mkdir(f"{selected_folder}/{folder}")

def check_file_existence(destination):
    # This function checks whether the new file to be organized already exists in the destination folder.
    # If it does, the new file name will be FileName_1.Extension
    if os.path.exists(destination):
        base_file_name, file_extension = os.path.splitext(destination)
        index = 1
        while os.path.exists(f"{base_file_name}_{index}{file_extension}"):
            index += 1
        return f"{base_file_name}_{index}{file_extension}"
    return destination

def move_file_to_folder(selected_folder, folder, file):
    # This function moves files according to their extension to folders
    # with names defined in the "extensions.py" file
    origin = os.path.join(selected_folder, file)
    destination = os.path.join(selected_folder, folder, file)
    destination = check_file_existence(destination)
    os.rename(origin, destination)

def organize_files(selected_folder, extensions):
    selected_folder_files = os.listdir(selected_folder)
    create_folders(extensions, selected_folder_files, selected_folder)
    for file in selected_folder_files:
        for folder, extension in extensions.items():
            if file.lower().endswith(extension):
                move_file_to_folder(selected_folder, folder, file)

def select_and_organize(selected_folder, extensions):
    if os.path.isdir(selected_folder):
        organize_files(selected_folder, extensions)