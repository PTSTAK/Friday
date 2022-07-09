import glob, os, asyncio
from source.function.const.download_file_from_sharepoint import *
from cirrus.functions import extract_excel_to_csv, local_csv_to_bq

def insert_to_bq(call_func):
    def insert_row():       
        csv_file = call_func()
        inserted_row = local_csv_to_bq(
                                file_path=csv_file,
                                project_id=project_id, 
                                dataset_id=dataset_id, 
                                table_id=table_id, 
                                service_acc=SERVICE_ACCOUNT,
                                skip_rows=1,
                                write_mode="append"
                            )
        return inserted_row
    return insert_row

def convert_file_to_csv(call_func):
    def convert():
        files_path = call_func()    
        path_csv, file_csv = os.path.split(str(files_path).strip('.xlsx') + '.csv')
        extract_excel_to_csv(files_path, file_csv)      
        csv_file = os.path.abspath(os.path.join(os.getcwd(), file_csv))
        return csv_file 
    return convert

@insert_to_bq
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
    