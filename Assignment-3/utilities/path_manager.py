from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
def path_details():

    print("All Path Details")
    # 1. Current working directory
    current_path = Path.cwd()
    print("Current Working Directory:", current_path)
    # 2. Get primary path from .env
    primary_file = Path(os.getenv("PRIMARY_FILE"))
    print("Primary File:", primary_file)
    # 3. Get secondary path from .env
    secondary_file = Path(os.getenv("SECONDARY_FILE"))
    print("Secondary File:", secondary_file)
    # 4. Check primary file exists
    print("Primary File Exists:", primary_file.exists())
    # 5. Check secondary file exists
    print("Secondary File Exists:", secondary_file.exists())
    # 6. Absolute path
    print("Primary File Absolute Path:", primary_file.resolve())
    # 7. File name
    print("Primary File Name:", primary_file.name)
    # 8. File extension
    print("Primary Extension:", primary_file.suffix)
    # 9. Parent directory
    print("Data Folder:", primary_file.parent)


def get_primary_path():
    return Path(os.getenv("PRIMARY_FILE"))


def get_secondary_path():
    return Path(os.getenv("SECONDARY_FILE"))

