# Modules
import os
import shutil

# Variables
user_input = None
download = os.path.expanduser('~/Downloads')


# Feel free to add on to the extensions should the folder assignment not work.
# Since the MIME type 'inode/blockdevice' does not specifically state what the file is, 
# we need to make use of this secondary extensions to determine what they are.
extensions = {
    ".zip": "ZIP Archive (Compressed Files and Folders)",
    ".ova": "Open Virtual Appliance (Virtual Machine Template)",
    ".mp4": "MPEG-4 Video File (Common Video Format)",
    ".iso": "Disk Image File (CD/DVD Backup or Installation Media)",
    ".txt": "General Text Files",
    ".html": "Web Pages",
    ".css": "Style Sheets",
    ".csv": "Comma-Separated Values (CSV) Files",
    ".js": "JavaScript Code",
    ".json": "JSON Data Files",
    ".xml": "XML Data Files",
    ".doc": "Microsoft Word Documents",
    ".docx": "Word Documents",
    ".xlsm": "Microsoft Excel Macro-Enabled Spreadsheets",
    ".xlsx": "Microsoft Excel Spreadsheets",
    ".xls": "Microsoft Excel 97-2003 Worksheet",
    ".ppt": "Microsoft PowerPoint Presentations",
    ".pptx": "PowerPoint Presentations",
    ".pdf": "Portable Document Format (PDF)",
    ".jpg": "JPEG Images",
    ".jpeg": "JPEG Images",
    ".png": "Portable Network Graphics (PNG)",
    ".gif": "Graphics Interchange Format (GIF)",
    ".bmp": "Bitmap Images",
    ".tiff": "Tagged Image File Format (TIFF)",
    ".webp": "WebP Image File (WEBP)",
    ".mp3": "MP3 Audio Files",
    ".wav": "Waveform Audio Files (WAV)",
    ".ogg": "Ogg Vorbis Audio Files",
    ".flac": "Free Lossless Audio Codec (FLAC)",
    ".webm": "WebM Video Files",
    ".ogv": "Ogg Theora Video Files",
    ".avi": "Audio Video Interleave (AVI)",
    ".rar": "RAR Archives",
    ".gz": "Gzip Compressed Files",
    ".tar": "Tar Archives",
    ".exe": "Windows Executables",
    ".jar": "Java Archive Files (JAR)",
    ".bin": "Generic Binary Data",
    ".msi": "Windows Installer Package",
    ".crt": "Certificate Files",
    ".pem": "Certificate Files",
    ".ovpn": "OpenVPN Files",
    ".eml": "Email Messages",
}

# Functions
def display_menu():
    print("\nMenu Options")
    print("------------")
    print("[1] Organise download files")
    print("[2] Remove old files")
    print("[0] Exit")

def organise_folder():
    for root, directories, files in os.walk(download):
        for directory in directories:
            directory_path = os.path.join(root, directory)
            folder_of_folders = os.path.join(root, "Folders")
            
            if os.path.isdir(folder_of_folders):
                shutil.move(directory_path, folder_of_folders)
            else:
                os.mkdir(folder_of_folders)

        for file in files:
            file_path = os.path.join(root, file)
            folder_name = "No format found"

            filename, file_extension = os.path.splitext(file)
            for extension, description in extensions.items():
                if file_extension == extension:
                    folder_path = os.path.join(root, description)
                    folder_name = description
                    break
            
            '''
            if os.path.isdir(folder_path):
                shutil.move(file_path, folder_path)
            else:
                os.mkdir(folder_path)
                shutil.move(file_path, folder_path)
            '''

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