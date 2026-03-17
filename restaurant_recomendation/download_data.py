import os
import requests
import zipfile
from urllib.parse import urlparse
import sys

def download_file(url, filename):
    """Download file from URL with progress bar"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        sys.stdout.write(f"\rDownloading: {percent:.1f}%")
                        sys.stdout.flush()
        
        print(f"\nDownloaded {filename} successfully!")
        return True
        
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False

def extract_zip(zip_filename, extract_to='.'):
    """Extract zip file"""
    try:
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted {zip_filename} successfully!")
        return True
    except Exception as e:
        print(f"Error extracting file: {e}")
        return False

def main():
    """Download and prepare the Yelp dataset"""
    print("Yelp Dataset Downloader")
    print("=" * 40)
    
    # Dataset URL (using a more reliable source)
    dataset_url = "https://www.dropbox.com/s/3x1w789mmuae3ao/yelp_academic_dataset_business.zip?dl=1"
    zip_filename = "yelp_academic_dataset_business.zip"
    json_filename = "yelp_academic_dataset_business.json"
    
    # Check if dataset already exists
    if os.path.exists(json_filename):
        print(f"Dataset {json_filename} already exists!")
        return
    
    # Download the dataset
    print(f"Downloading dataset from: {dataset_url}")
    if not download_file(dataset_url, zip_filename):
        print("Failed to download dataset!")
        return
    
    # Extract the dataset
    print("Extracting dataset...")
    if extract_zip(zip_filename):
        # Clean up zip file
        os.remove(zip_filename)
        print(f"Dataset ready: {json_filename}")
    else:
        print("Failed to extract dataset!")

if __name__ == "__main__":
    main()
