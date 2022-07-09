from source.function.main_class.my_cumulus import MyCumulus
from cirrus.constants import ArgumentParams
from source.function.main_function.download_file_from_sharepoint import download_file_from_sharepoint


class DownloadFileFromSharepoint(MyCumulus):
    def __init__(self, method_args):
        # pass
        self.x = method_args.get("x")
        self.y = method_args.get("y")

    @staticmethod
    def get_method_description():
        return '''
                Description.
            '''

    @staticmethod
    def get_args_list():
        return [
            {
                ArgumentParams.SHORT_NAME : '-x',
                ArgumentParams.NAME : '--x',
                #ArgumentParams.DESCRIPTION : 'Example of a parameter',
                # ArgumentParams.REQUIRED : False
                # ArgumentParams.ISFLAG : True,
                # ArgumentParams.DEFAULT : True
            },
            {
                ArgumentParams.SHORT_NAME : '-y',
                ArgumentParams.NAME : '--y',
                # ArgumentParams.DESCRIPTION : 'Example of a parameter',
                # ArgumentParams.REQUIRED : False
                # ArgumentParams.ISFLAG : True,
                # ArgumentParams.DEFAULT : True
            }
        ]
    
    def run(self):
        pass
        # app = async_func()
        # app.run_start()