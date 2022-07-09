import glob, os, asyncio
from cirrus.functions import extract_excel_to_csv

def convert_file_to_csv(call_func):
    def convert():
        files_path = call_func()    
        path_csv, file_csv = os.path.split(str(files_path).strip('.xlsx') + '.csv')
        extract_excel_to_csv(files_path, file_csv)      
        csv_file = os.path.abspath(os.path.join(os.getcwd(), file_csv))
        return csv_file
    
    return convert

@convert_file_to_csv
def download_file_from_sharepoint():
    path = os.path.abspath(os.path.join(os.getcwd(), 'excel_path'))
    file_type = r'\*xlsx'
    get_last_file = glob.glob(path + file_type)
    files = max(get_last_file, key=os.path.getctime)
        
    return files

# class async_func():
#     def __init__(self):
#         pass
    
#     def run_start(self):
#         loop = asyncio.get_event_loop()
#         loop.run_until_complete(self.main())
        
#     async def download_file_from_sharepoint(self):   
#         path = os.path.abspath(os.path.join(os.getcwd(), 'excel_path'))
#         file_type = r'\*xlsx'
#         get_last_file = glob.glob(path + file_type)
#         files = max(get_last_file, key=os.path.getctime)
        
#         return files

#     async def main(self):
#         task1  = asyncio.create_task(self.download_file_from_sharepoint())
#         await task1
#         print(task1.result())
    