import pytest
from source.manager.main_function.manager1 import manager1

class TestManager1():

    def setup_class(self):
        self.__STRING = 'STRING'

    def test_validate_all_types(self, mocker):
        pass        
        # example
        # validate_string = mocker.patch('source.function.main_functions.scan_validate_csv.validate_string')
        # validate_all_types(self.__STRING, self.__string)
        # validate_string.assert_called_once_with(self.__string)
        
        # with pytest.raises(ValueError):
        #     validate_all_types(self.__OTHERS, self.__string)