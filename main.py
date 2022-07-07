from cirrus.constants import Option, SOURCE, Folder
from cirrus.utils import setup_log, setup_folder, setup_parser, clear_tmp_files
from cirrus.utils import detect_classes, get_method_arguments, call_method

def setup_project():
    # Setup project
    # 1. Detect all classes from function, manager and factory
    # 2. Setup parser
    # return option, method and method arguments
    setup_folder()
    setup_log()
    functions, managers = detect_classes(Folder.FUNCTION_FOLDER, Folder.MANAGER_FOLDER)
    args = setup_parser(SOURCE, functions, managers)
    return args.option, args.method, get_method_arguments(args)

def cirrus():
    option, method, method_args = setup_project()
    
    if option == Option.FUNCTION:
        call_method(SOURCE, Option.FUNCTION, method, method_args)
    elif option == Option.MANAGER:
        call_method(SOURCE, Option.MANAGER, method, method_args)
    # elif option == Option.FACTORY_ABBREVATION:
        # Factory(method, method_args).call_method()
    clear_tmp_files()

if __name__ == "__main__":
    cirrus()
