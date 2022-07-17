import sys, os, glob
from cirrus.common.const import Tmp


def get_last_file():
    # path = Tmp.EXCEL
    path = os.path.abspath(os.path.join(os.getcwd(), 'excel'))
    file_type = r'\Digital_PMO_Test_*.xlsx'
    try:
        files = max(glob.glob(path + file_type), key=os.path.getctime)      
    except Exception as err: 
        print(f"ชื่อ file ใน path {path} ไม่ถูกต้อง!! โปรดตวจสอบอีกครั้ง", file=sys.stderr)
        sys.exit(0)
    return files
