from pathlib import Path
import xml.etree.ElementTree as ET

FOLDER_PATH = Path(r"\\sab-az-sys01\Failure")


def find_first_by_local_name(root, tag_name):
    for elem in root.iter():
        local_name = elem.tag.split("}", 1)[-1]
        if local_name == tag_name:
            return elem
    return None


def main():
    if not FOLDER_PATH.exists():
        print(f"Error: The folder '{FOLDER_PATH}' does not exist.")
        return

    xml_files = [
        file for file in FOLDER_PATH.iterdir()
        if file.is_file() and file.suffix.lower() == ".xml"
    ]

    if not xml_files:
        print(f"No XML files found in '{FOLDER_PATH}'.")
        return

    records = []

    for file in xml_files:
        try:
            tree = ET.parse(file)
            root = tree.getroot()

            trading_partner = find_first_by_local_name(root, "TradingPartnerId")
            po_number = find_first_by_local_name(root, "PurchaseOrderNumber")

            record = {
                "file_name": file.name,
                "trading_partner_id": trading_partner.text.strip() if trading_partner is not None and trading_partner.text else "",
                "purchase_order_number": po_number.text.strip() if po_number is not None and po_number.text else "",
            }

            records.append(record)

        except Exception as e:
            print(f"Error reading {file.name}: {e}")

    print(f"Total records built: {len(records)}")
    print()

    for record in records:
        print(record)


if __name__ == "__main__":
    main()