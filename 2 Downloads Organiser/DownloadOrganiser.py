# Modules
import os
import magic

# Variables
user_input = None
download = os.path.expanduser('~/Downloads')
mime_types = {
    "text/plain": "General Text Files",
    "text/html": "Web Pages",
    "text/css": "Style Sheets",
    "text/javascript": "JavaScript Code",
    "application/json": "JSON Data Files",
    "application/xml": "XML Data Files",
    "application/msword": "Microsoft Word Documents",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "Word Documents",
    "application/vnd.ms-excel": "Microsoft Excel Spreadsheets",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "Excel Spreadsheets",
    "application/vnd.ms-powerpoint": "Microsoft PowerPoint Presentations",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "PowerPoint Presentations",
    "application/pdf": "Portable Document Format (PDF)",
    "image/jpeg": "JPEG Images",
    "image/png": "Portable Network Graphics (PNG)",
    "image/gif": "Graphics Interchange Format (GIF)",
    "image/bmp": "Bitmap Images",
    "image/tiff": "Tagged Image File Format (TIFF)",
    "image/webp": "WebP Image File (WEBP)",
    "audio/mpeg": "MP3 Audio Files",
    "audio/wav": "Waveform Audio Files (WAV)",
    "audio/ogg": "Ogg Vorbis Audio Files",
    "audio/flac": "Free Lossless Audio Codec (FLAC)",
    "video/mp4": "MPEG-4 Video Files (MP4)",
    "video/webm": "WebM Video Files",
    "video/ogg": "Ogg Theora Video Files",
    "video/avi": "Audio Video Interleave (AVI)",
    "application/zip": "ZIP Archives",
    "application/x-rar-compressed": "RAR Archives",
    "application/gzip": "Gzip Compressed Files",
    "application/x-tar": "Tar Archives",
    "application/x-msdownload": "Windows Executables",
    "application/java-archive": "Java Archive Files (JAR)",
    "application/octet-stream": "Generic Binary Data",
    "application/x-dosexec": "Windows Executable Files",
    "message/rfc822": "Email Messages",
    "multipart/form-data": "Web Form Data"
}

# Feel free to add on to the extensions should the folder assignment not work.
# Since the MIME type 'inode/blockdevice' does not specifically state what the file is, 
# we need to make use of this secondary extensions to determine what they are.
secondary_extensions = {
    ".zip": "ZIP Archive (Compressed Files and Folders)",
    ".ova": "Open Virtual Appliance (Virtual Machine Template)",
    ".mp4": "MPEG-4 Video File (Common Video Format)",
    ".iso": "Disk Image File (CD/DVD Backup or Installation Media)",
}

# Functions
def display_menu():
    print("\nMenu Options")
    print("------------")
    print("[1] Organise download files")
    print("[2] Remove old files")
    print("[0] Exit")

def organise_folder():
    mime_format = magic.Magic(mime=True)

    for root, directories, files in os.walk(download):
        for directory in directories:
            directory_path = os.path.join(root, directory)
            print(f"Found folder: {directory_path}")

        for file in files:
            file_path = os.path.join(root, file)
            folder_name = "No format found"
            filetype = mime_format.from_file(file_path)

            for mimetype, description in mime_types.items():
                if filetype == mimetype:
                    folder_name = description
                    break
            if filetype == "inode/blockdevice":
                filename, file_extension = os.path.splitext(file)
                for extension, description2 in secondary_extensions.items():
                    if file_extension == extension:
                        folder_name = description2
            
            print(f"File name: {file}, File type: {filetype}, Folder name: {folder_name}")

        break
                
# Main Program
while user_input != "0":
    display_menu()
    user_input = input("\nEnter your option: ")

    match user_input:
        case "1":
            organise_folder()
        case "2":
            print("You chose option 2.")
        case "0":
            break
        case _:
            print("Invalid option! Please enter your option again!")