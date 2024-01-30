import os
import inspect
def port(module_name: str = None, file_name: str = None) -> bool:
    if file_name == None:
        file_name = inspect.currentframe().f_back.f_code.co_filename
        file_name = os.path.basename(file_name).strip()
    if module_name == None:
        return None
    if not file_name.endswith('.py'):
        file_name = file_name + '.py'
    file_read = open(file_name,'r')
    file_lines = file_read.readlines()
    module_name = 'time'
    found_value = False
    for found1 in file_lines:
        if 'import' in found1:
            if found1.startswith('import'):
                if module_name in found1:
                    start_index = found1.index(module_name)
                    end_index = start_index + 3
                    before_index = start_index - 1
                    after_index = end_index + 1
                    if found1[before_index] == ' ':
                        if found1[after_index] == ' ' or found1[after_index] == '\n' or found1[after_index] == ',':
                            found_value = True
                            break
                    elif found1[before_index] == ',':
                        if found1[after_index] == ' ' or found1[after_index] == ',' or found1[after_index] == '\n':
                            found_value = True
                            break
            elif found1.startswith('from'):
                if module_name in found1:
                    start_index = found1.index(module_name)
                    end_index = start_index + 3
                    before_index = start_index - 1
                    after_index = end_index + 1
                    if found1[before_index] == ' ':
                        if found1[after_index] == ' ' or found1[after_index] == '\n' or found1[after_index] == ',':
                            found_value = True
                            break
                    elif found1[before_index] == ',':
                        if found1[after_index] == ' ' or found1[after_index] == ',' or found1[after_index] == '\n':
                            found_value = True
                            break
    if found_value == False:
        return False
    elif found_value == True:
        return True