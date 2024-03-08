import os
import zipfile

def unzip_and_rename_files():
    """Unzips and renames the two files."""

    filename_2014 = "/home/artgressick/cve/nvdcve-1.1-2014.json.zip"
    filename_2015 = "/home/artgressick/cve/nvdcve-1.1-2015.json.zip"
    filename_2016 = "/home/artgressick/cve/nvdcve-1.1-2016.json.zip"
    filename_2017 = "/home/artgressick/cve/nvdcve-1.1-2017.json.zip"
    filename_2018 = "/home/artgressick/cve/nvdcve-1.1-2018.json.zip"
    filename_2019 = "/home/artgressick/cve/nvdcve-1.1-2019.json.zip"
    filename_2020 = "/home/artgressick/cve/nvdcve-1.1-2020.json.zip"
    filename_2021 = "/home/artgressick/cve/nvdcve-1.1-2021.json.zip"
    filename_2022 = "/home/artgressick/cve/nvdcve-1.1-2022.json.zip"
    filename_2023 = "/home/artgressick/cve/nvdcve-1.1-2023.json.zip"
    filename_2024 = "/home/artgressick/cve/nvdcve-1.1-2024.json.zip"

    # Unzip the files
    zipfile_2014 = zipfile.ZipFile(filename_2014)
    zipfile_2015 = zipfile.ZipFile(filename_2015)
    zipfile_2016 = zipfile.ZipFile(filename_2016)
    zipfile_2017 = zipfile.ZipFile(filename_2017)
    zipfile_2018 = zipfile.ZipFile(filename_2018)
    zipfile_2019 = zipfile.ZipFile(filename_2019)
    zipfile_2020 = zipfile.ZipFile(filename_2020)
    zipfile_2021 = zipfile.ZipFile(filename_2021)
    zipfile_2022 = zipfile.ZipFile(filename_2022)
    zipfile_2023 = zipfile.ZipFile(filename_2023)
    zipfile_2024 = zipfile.ZipFile(filename_2024)
    zipfile_2014.extractall("/home/artgressick/cve")
    zipfile_2015.extractall("/home/artgressick/cve")
    zipfile_2016.extractall("/home/artgressick/cve")
    zipfile_2017.extractall("/home/artgressick/cve")
    zipfile_2018.extractall("/home/artgressick/cve")
    zipfile_2019.extractall("/home/artgressick/cve")
    zipfile_2020.extractall("/home/artgressick/cve")
    zipfile_2021.extractall("/home/artgressick/cve")
    zipfile_2022.extractall("/home/artgressick/cve")
    zipfile_2023.extractall("/home/artgressick/cve")
    zipfile_2024.extractall("/home/artgressick/cve")


    # Rename the files
    os.rename("/home/artgressick/cve/nvdcve-1.1-2014.json", "2014.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2015.json", "2015.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2016.json", "2016.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2017.json", "2017.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2018.json", "2018.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2019.json", "2019.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2020.json", "2020.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2021.json", "2021.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2022.json", "2022.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2023.json", "2023.json")
    os.rename("/home/artgressick/cve/nvdcve-1.1-2024.json", "2024.json")

if __name__ == "__main__":
    unzip_and_rename_files()
