"""
Automated download of the Finnish clay laboratory dataset.

Laboratory 3 - ING8100
Polytechnique Montreal
"""

from pathlib import Path
import requests

BASE_URL = "https://demo.borealisdata.ca"
DATASET_DOI = "doi:10.80240/FK2/DZGAMU"

API_FILENAME = "Laboratory_data.tab"
OUTPUT_FILENAME = "Laboratory_data.xlsx"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"


def download_data():
    """Download the original Excel dataset from Borealis."""

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Retrieve the published dataset metadata
    metadata_url = (
        f"{BASE_URL}/api/datasets/:persistentId/"
        "versions/:latest-published"
    )

    response = requests.get(
        metadata_url,
        params={"persistentId": DATASET_DOI},
        timeout=60
    )
    response.raise_for_status()

    dataset = response.json()["data"]

    # Identify the tabular file in Dataverse
    matches = [
        item for item in dataset["files"]
        if item["dataFile"]["filename"] == API_FILENAME
        and item.get("directoryLabel", "") == "data/raw"
    ]

    if not matches:
        raise FileNotFoundError(
            f"{API_FILENAME} not found in Borealis."
        )

    file_info = matches[0]

    if file_info.get("restricted", False):
        raise PermissionError("The dataset file is restricted.")

    file_id = file_info["dataFile"]["id"]

    # Download the original Excel format
    download_url = (
        f"{BASE_URL}/api/access/datafile/{file_id}"
    )

    response = requests.get(
        download_url,
        params={"format": "original"},
        timeout=120
    )
    response.raise_for_status()

    destination = RAW_DIR / OUTPUT_FILENAME

    destination.write_bytes(response.content)

    if destination.stat().st_size == 0:
        raise RuntimeError("The downloaded file is empty.")

    print("Download completed successfully.")
    print("File:", destination)
    print("Size:", destination.stat().st_size, "bytes")


if __name__ == "__main__":
    download_data()
