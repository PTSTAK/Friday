import pandas as pd
from sqlalchemy import table
from source.function.const.read_file_from_sharepoint import get_last_file


def read_file_from_sharepoint():
    files = get_last_file()
    
    df = pd.read_excel(files, sheet_name=0, skiprows=4, header=[0,1]).transpose().reset_index()
    data = df.iloc[[0,4] , 0:].reset_index().drop(['index','level_0', 'level_1'], axis=1) # get column 0 => Target Fields, 4=> Example Data
    
    
    # for rows in data.itertuples(index=False):
    #     data.to_excel(rows)