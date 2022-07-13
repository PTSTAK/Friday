from source.function.main_class.my_cumulus import MyCumulus
from cirrus.constants import ArgumentParams
from source.function.main_function.get_file_from_sharepoint import get_file_from_sharepoint

class GetFileFromSharepoint(MyCumulus):
    def __init__(self, method_args):
        self.months = method_args.get("m")
        self.years = method_args.get("y")

    @staticmethod
    def get_method_description():
        return '''
                Description.
               '''

    @staticmethod
    def get_args_list():
        return [
            {
                ArgumentParams.SHORT_NAME : '-m',
                ArgumentParams.NAME : '--m',
                ArgumentParams.DESCRIPTION : 'months',
                ArgumentParams.REQUIRED : False,
                # ArgumentParams.ISFLAG : True,
                # ArgumentParams.DEFAULT : True
            },
            {
                ArgumentParams.SHORT_NAME : '-y',
                ArgumentParams.NAME : '--y',
                ArgumentParams.DESCRIPTION : 'years',
                ArgumentParams.REQUIRED : False,
                # ArgumentParams.ISFLAG : True,
                # ArgumentParams.DEFAULT : True
            },
            
        ]
    
    def run(self):
        get_file_from_sharepoint(self.months, self.years)
