import os, sys, glob, pandas as pd , json, argparse
from tkinter import S
from source.function.const.get_file_from_sharepoint import *

from cirrus.helpers import *


# path =  os.path.abspath(os.path.join(os.getcwd(), 'credentials\secret.json'))   
# data = json.load(open(path))




def get_file_from_sharepoint(m, y):
    

    file_name = "output.xlsx"
        
    a = download_file_from_sharepoint(
            SERCRET,
            rel_path,
            file_name,
            server_url=server_url)
    print(a)
    
    # if (m is None) and (y is None) :
    #     path = os.path.abspath(os.path.join(os.getcwd(), 'excel_path'))
    #     file_type = r'\Digital_PMO_Test_Data.xlsx'
    #     get_last_file = glob.glob(path + file_type)
    
    #     try:
    #         files = max(get_last_file, key=os.path.getctime)
    #     except Exception as err: 
    #         print(f"ชื่อ file ใน path {path} ไม่ถูกต้อง!! โปรดตวจสอบอีกครั้ง", file=sys.stderr)
    #         sys.exit(1)
            
    return 'files'



