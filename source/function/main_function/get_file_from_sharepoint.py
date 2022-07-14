import os, sys, glob, pandas as pd
from source.function.const.get_file_from_sharepoint import *
from cirrus.common.helper.sharepoint_helper import download_file_from_sharepoint

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File 


def test_conn_sharepoint():
    
    # app_principal = {
    #     "client_id": "zThanakitJ@pttep.com",
    #     "client_secret": "!ZP8NQ85uaZV4JT",
    # }
    client_id =  "zThanakitJ@pttep.com"
    client_secret = "!ZP8NQ85uaZV4JT"
    
    url_shrpt = "https://pttep.sharepoint.com/teams/SoftwareDevelopmentwithExternalParty"
    
    ctx_auth = AuthenticationContext(url_shrpt)
    
    try:
        if ctx_auth.acquire_token_for_app(client_id=client_id, client_secret=client_secret):
            ctx = ClientContext(url_shrpt, ctx_auth)
            web = ctx.web
            ctx.load(web)
            ctx.execute_query()
            print('Authenticated into sharepoint app for: ',web.properties['Title'])
        else:
            print(ctx_auth.get_last_error())
            sys.exit()
    except Exception as err:
        print(err)


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

