from source.function.main_class.my_cumulus import MyCumulus
from cirrus.constants import ArgumentParams
from source.function.main_function.read_file_from_sharepoint import read_file_from_sharepoint

class ReadFileFromSharepoint(MyCumulus):
    def __init__(self, method_args):
        self.param = method_args.get("param")

    @staticmethod
    def get_method_description():
        return '''
                Description.
               '''

    @staticmethod
    def get_args_list():
        return [
            {
                ArgumentParams.SHORT_NAME : '-p',
                ArgumentParams.NAME : '--param_example',
                ArgumentParams.DESCRIPTION : 'Example of a parameter',
                # ArgumentParams.REQUIRED : False,
                # ArgumentParams.ISFLAG : True,
                # ArgumentParams.DEFAULT : True
            }
        ]
    
    def run(self):
        read_file_from_sharepoint()
