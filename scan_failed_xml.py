from pathlib import Path

FOLDER_PATH = Path(r"\\sab-az-sys01\Failure")
                   
def main():
    if not FOLDER_PATH.exists():
        print(f"Error: The folder '{FOLDER_PATH}' does not exist.")
        return
    
    xml_files = [
        file for file in FOLDER_PATH.iterdir()
        if file.is_file() and file.suffix.lower() == '.xml'
    ]

    if not xml_files:
        print(f"No XML files found in '{FOLDER_PATH}'.")
        return

    print(f"Found {len(xml_files)} XML file(s) in '{FOLDER_PATH}':")
    for file in xml_files:
        print(file)


if __name__ == "__main__":
    main()

