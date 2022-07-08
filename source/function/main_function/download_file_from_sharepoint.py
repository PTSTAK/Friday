import glob
import os
import asyncio

def download_file_from_sharepoint(x, y):
    print(x)
    print(y)
    return x + y

class async_func():
    def __init__(self):
        pass
    
    def run_start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        
    async def download_file_from_sharepoint(self):   
        path = os.path.abspath(os.path.join(os.getcwd(), 'excel_path'))
        file_type = r'\*xlsx'
        get_last_file = glob.glob(path + file_type)
        files = max(get_last_file, key=os.path.getctime)
        
        return files

    async def main(self):
        task1  = asyncio.create_task(self.download_file_from_sharepoint())
        await task1
        print(task1.result())
    