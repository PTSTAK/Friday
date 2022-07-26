import os, sys, glob, pandas as pd
from source.function.const.get_file_from_sharepoint import *
from cirrus.common.helper.sharepoint_helper import download_file_from_sharepoint


from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File 

# def test_auth_sharepoint():
#     app_settings = {
#         'url': 'https://mfeconcloud.sharepoint.com/sites/TrainingVideo/',
#         'client_id': 'aaaa-bbb-473a-a1b2-zzzzzfadfd',
#         'client_secret': 'Tteadsfdafdfasdff444gadfd=',
#     }
    
#     context_auth = AuthenticationContext(url=app_settings['url'])
#     context_auth.acquire_token_for_app(client_id=app_settings['client_id'], client_secret=app_settings['client_secret'])
#     try:
#         if  context_auth.acquire_token_for_app(client_id=app_settings['client_id'], client_secret=app_settings['client_secret']):
#             ctx = ClientContext(app_settings['url'], context_auth)
#             web = ctx.web
#             ctx.load(web)
#             ctx.execute_query()
#             print('Authenticated into sharepoint app for: ',web.properties['Title'])
#         else:    
#             print(context_auth.get_last_error())
#     except Exception as err:
#         print(err)

def test_conn_sharepoint(): 
    url_shrpt = "https://pttep.sharepoint.com/sites/0200SBD/SCS/SSP/"
    username_shrpt = "zThanakitJ@pttep.com"
    password_shrpt = "!ZP8NQ85uaZV4JT"
    # username_shrpt = "PTTEP\HQ.SVC-Automate"
    # password_shrpt = "@t8t6%&85!R$@5v*!eMAFHH2&QQGd6"
    try:
        ctx_auth = AuthenticationContext(url_shrpt)
        if ctx_auth.acquire_token_for_user(username_shrpt, password_shrpt):
            ctx = ClientContext(url_shrpt, ctx_auth)
            web = ctx.web
            ctx.load(web)
            ctx.execute_query()
            print('Authenticated into sharepoint as: ',web.properties['Title'])
        else:
            print(ctx_auth.get_last_error())
    except Exception as err:
        err


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
        err
    
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

