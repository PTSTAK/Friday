from source.function.main_function.download_file_from_sharepoint import download_file_from_sharepoint
from source.manager.const.manager1 import SERVICE_ACCOUNT

def manager1():
    out_csv = download_file_from_sharepoint()

    return out_csv
