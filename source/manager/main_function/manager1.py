import os
import datetime

from source.function.main_function.download_file_from_sharepoint import download_file_from_sharepoint
from cirrus.functions import extract_excel_to_csv


def manager1():
    out_csv = download_file_from_sharepoint()

    return out_csv
