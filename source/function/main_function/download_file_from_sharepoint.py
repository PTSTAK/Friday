import glob, os, sys, asyncio, pandas as pd, numpy as np
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
        return  csv_file
    
    return convert

def format_data(call_func):
    def merge_data():
        excel_file = call_func()
        df1 = pd.read_excel(open(excel_file, 'rb'), nrows=1, usecols="A:B") # get site and business date
        df1 = pd.DataFrame(np.repeat(df1.values, 10, axis=0), columns=df1.columns) # repeat data to row
        df2 = pd.read_excel(open(excel_file, 'rb'), skiprows=4,  usecols="A:J") # get data     
        df_merge = pd.concat([df1, df2], axis=1)
        
        # update excel 
        path,  file = os.path.split(str(excel_file))    
        new_name = f'\merge_data_{file}'
        new_excel = os.path.abspath(path + new_name)
        with pd.ExcelWriter(new_excel) as writer:  
            df_merge.to_excel(writer, index=False)
        return new_excel
    
    return merge_data

@insert_to_bq
@convert_file_to_csv
@format_data
def download_file_from_sharepoint():
    path = os.path.abspath(os.path.join(os.getcwd(), 'excel_path'))
    file_type = r'\sharepoint_*xlsx'
    get_last_file = glob.glob(path + file_type)
    
    try:
        files = max(get_last_file, key=os.path.getctime)      
        # chk = check_template(files)
    except Exception as err: 
        print(f"ชื่อ file ใน path {path} ไม่ถูกต้อง!! โปรดตวจสอบอีกครั้ง", file=sys.stderr)
        sys.exit(0)
        
    return 'files'


def check_template(files):
    
    path = os.path.abspath(os.path.join(os.getcwd(), 'excel_path'))
    
    file_original  = os.path.abspath(os.path.join(os.getcwd(), 'template_sharepoint.xlsx'))
    file_new  = files
    
    df_file_original =  pd.read_excel(open(file_original, 'rb')).fillna("")
    df_file_new = pd.read_excel(open(file_new, 'rb')).fillna("")
    
    # value
    comparison_values = df_file_original.values == df_file_new.values
    rows,cols=np.where(comparison_values==False)
    for item in zip(rows,cols):
        df_file_original.iloc[item[0], item[1]] = '{} --> {}'.format(df_file_original.iloc[item[0], item[1]],df_file_new.iloc[item[0], item[1]])  
    err_path = os.path.abspath(os.path.join(os.getcwd(), 'err_template_sharepoint.xlsx'))
    err_file = df_file_original.to_excel(err_path ,index=False,header=True)
    
    return err_file



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
    