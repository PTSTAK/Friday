import os, sys, glob, pandas as pd
from source.function.const.get_file_from_sharepoint import *
from cirrus.common.helper.sharepoint_helper import download_file_from_sharepoint


def get_file_from_sharepoint(m, y):
    
    path_file = os.path.abspath(os.path.join(os.getcwd(), 'excel_path'))
    file_name = '\Digital_PMO_Test_Data.xlsx'
    try:
        download_file_from_sharepoint(
                secret_path=SERCRET,
                rel_path=rel_path,
                file_name=file_name,
                output_dir=path_file,
                server_url=server_url
                )
    except Exception as err:
        print(err)
    
    """
    if (m is None) and (y is None) :
        path = os.path.abspath(os.path.join(os.getcwd(), 'excel_path'))
        file_type = r'\Digital_PMO_Test_Data.xlsx'
        get_last_file = glob.glob(path + file_type)
    
        try:
            files = max(get_last_file, key=os.path.getctime)
        except Exception as err: 
            print(f"ชื่อ file ใน path {path} ไม่ถูกต้อง!! โปรดตวจสอบอีกครั้ง", file=sys.stderr)
            sys.exit(1)
    """

