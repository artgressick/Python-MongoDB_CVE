import os
import zipfile
import requests
import sys

def download_file(url, filename):
    """
    Downloads a file from a given URL and saves it.
    Returns True on success, False on failure.
    """
    print(f"Downloading {url}...")
    try:
        # Use stream=True for large files
        response = requests.get(url, stream=True)
        # Raise an exception for bad status codes (like 404)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            # Use a larger chunk size for faster downloads
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Successfully downloaded {filename}.")
        return True
    except requests.exceptions.RequestException as e:
        # This catches connection errors, timeouts, and bad HTTP responses
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        return False

def process_year(year, base_url):
    """
    Downloads, unzips, renames, and cleans up NVD data for a specific year.
    """
    zip_filename = f"nvdcve-2.0-{year}.json.zip"
    url = f"{base_url}{zip_filename}"
    original_json_name = f"nvdcve-2.0-{year}.json"
    target_json_name = f"{year}.json"

    # 1. Download the zip file
    if not download_file(url, zip_filename):
        print(f"Skipping year {year} due to download failure.")
        return # Move to the next year

    # 2. Unzip the file
    try:
        print(f"Unzipping {zip_filename}...")
        with zipfile.ZipFile(zip_filename) as zip_file:
            # Extract the specific JSON file to the current directory
            zip_file.extract(original_json_name, path=".")
        print(f"Successfully extracted {original_json_name}.")
    except zipfile.BadZipFile:
        print(f"Error: {zip_filename} is not a valid zip file. It may be a partial download.", file=sys.stderr)
        # Clean up the bad file before returning
        os.remove(zip_filename)
        return
    except KeyError:
        print(f"Error: {original_json_name} was not found inside {zip_filename}.", file=sys.stderr)
        os.remove(zip_filename)
        return
    except Exception as e:
        print(f"An error occurred during unzipping: {e}", file=sys.stderr)
        os.remove(zip_filename)
        return

    # 3. Rename the extracted file
    try:
        print(f"Renaming {original_json_name} to {target_json_name}...")
        os.rename(original_json_name, target_json_name)
        print(f"Successfully renamed to {target_json_name}.")
    except FileNotFoundError:
        print(f"Error: {original_json_name} not found for renaming.", file=sys.stderr)
    except FileExistsError:
        print(f"Warning: {target_json_name} already exists. Deleting the freshly extracted {original_json_name}.", file=sys.stderr)
        os.remove(original_json_name) # Clean up the extracted file
    except Exception as e:
        print(f"An error occurred during renaming: {e}", file=sys.stderr)

    # 4. Clean up the downloaded zip file
    try:
        print(f"Cleaning up {zip_filename}...")
        os.remove(zip_filename)
        print(f"Removed {zip_filename}.")
    except OSError as e:
        print(f"Error cleaning up {zip_filename}: {e}", file=sys.stderr)

def main():
    """
    Main function to loop through all specified years and process them.
    """
    BASE_URL = "https://nvd.nist.gov/feeds/json/cve/2.0/"
    # Process years 2014 through 2025 (inclusive)
    START_YEAR = 2014
    END_YEAR = 2025 

    for year in range(START_YEAR, END_YEAR + 1):
        print(f"\n--- Processing year {year} ---")
        process_year(year, BASE_URL)
        print(f"--- Finished processing year {year} ---")
    
    print("\nAll NVD file processing tasks are complete.")

if __name__ == "__main__":
    main()
