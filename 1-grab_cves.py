import requests
import os

def download_file(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

if __name__ == "__main__":
    filename_2014 = "nvdcve-1.1-2014.json.zip"
    filename_2015 = "nvdcve-1.1-2015.json.zip"
    filename_2016 = "nvdcve-1.1-2016.json.zip"
    filename_2017 = "nvdcve-1.1-2017.json.zip"
    filename_2018 = "nvdcve-1.1-2018.json.zip"
    filename_2019 = "nvdcve-1.1-2019.json.zip"
    filename_2020 = "nvdcve-1.1-2020.json.zip"
    filename_2021 = "nvdcve-1.1-2021.json.zip"
    filename_2022 = "nvdcve-1.1-2022.json.zip"
    filename_2023 = "nvdcve-1.1-2023.json.zip"
    filename_2024 = "nvdcve-1.1-2024.json.zip"

    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2014.json.zip", filename_2014)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2015.json.zip", filename_2015)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2016.json.zip", filename_2016)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2017.json.zip", filename_2017)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2018.json.zip", filename_2018)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2019.json.zip", filename_2019)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2020.json.zip", filename_2020)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2021.json.zip", filename_2021)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2022.json.zip", filename_2022)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2023.json.zip", filename_2023)
    download_file("https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2024.json.zip", filename_2024)

    print("The files have been downloaded successfully.")
