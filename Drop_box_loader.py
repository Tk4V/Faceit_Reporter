import dropbox
import os

with open("token.txt", "r") as f:
    token = f.read()

dbx = dropbox.Dropbox(token)

def download_all_cloud_files(folder_path="", local_path=""):
    for entry in dbx.files_list_folder(folder_path).entries:
        # Check if the entry is a file
        if isinstance(entry, dropbox.files.FileMetadata):
            # Download the file
            download_path = os.path.join("Files/", entry.name)
            dbx.files_download_to_file(download_path, entry.path_display)
        elif isinstance(entry, dropbox.files.FolderMetadata):
            # If it's a folder, download its contents recursively
            new_local_path = os.path.join(local_path, entry.name)
            os.makedirs(new_local_path, exist_ok=True)
            download_all_cloud_files(new_folder_path, new_local_path)


download_all_cloud_files()



