from source.manager.main_class.my_alto_cumulus import MyAltoCumulus
from cirrus.constants import ArgumentParams
from source.manager.main_function.manager1 import manager1

class Manager1(MyAltoCumulus):
    def __init__(self, method_args):
        pass

    @staticmethod
    def get_method_description():
        return '''
                Description.
               '''

    @staticmethod
    def get_args_list():
        return [
            {   
                ArgumentParams.SHORT_NAME : "-x",
                ArgumentParams.NAME : "--x",
                ArgumentParams.DESCRIPTION : "Example of a parameter",
                ArgumentParams.REQUIRED : False,
                # ArgumentParams.ISFLAG : True,
                # ArgumentParams.DEFAULT : True
            },
            {   
                ArgumentParams.SHORT_NAME : "-y",
                ArgumentParams.NAME : "--y",
                ArgumentParams.DESCRIPTION : "Example of a parameter",
                ArgumentParams.REQUIRED : False,
                # ArgumentParams.ISFLAG : True,
                # ArgumentParams.DEFAULT : True
            }
        ]
    
    def run(self):
        run = manager1()
