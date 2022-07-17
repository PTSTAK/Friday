import pytest
from source.function.main_function.read_file_from_sharepoint import read_file_from_sharepoint

class TestReadFileFromSharepoint():

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
