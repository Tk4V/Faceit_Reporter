import dropbox

#read the acces token
with open("token.txt", "r") as f:
    token = f.read().strip()

# Initialize the Dropbox client
dbx = dropbox.Dropbox(token)

#Folder path
folder_path = ""

def list_files_in_folder(folder_path):
    try:
        #files lists
        result = dbx.files_list_folder(folder_path)

        #save in file
        with open("file_metadata.txt", "w", encoding="utf-8") as metadata_file:
            for entry in result.entries:
                metadata_file.write(f"File Name: {entry.name}\n")
                metadata_file.write(f"File Path: {entry.path_display}\n")
                metadata_file.write(f"File Metadata: {entry}\n\n")
                print(entry)

        print("File metadata saved to 'file_metadata.txt'")

    except dropbox.exceptions.HttpError as err:
        print(f"Error listing files: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


        


list_files_in_folder(folder_path)
