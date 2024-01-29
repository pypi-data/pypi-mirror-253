'''

Abstract: The library is written for convenience when using JSON files.

Functions:
1) json_read: Reading data from a JSON file

2) json_write: Data dump to JSON file

3) json_initialize_parameters: 
        A function that adds variables stored in JSON files to a class. 
        Filename must store paths to JSON files, then the function will read each data from each file. 
        This will also add variables with the "path_" prefix that store file paths.
        This approach allows you to effectively use the methods of this library.

4) json_write_parameter: A function that allows you to change the value in a dictionary stored in a JSON file.

5) json_append_to: A function that adds elements to a list stored in a JSON file

'''


from json import load as __load
from json import dump as __dump


def json_read(filename: str):
    
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = __load(json_file)
        return data


def json_write(filename: str, data)-> None:
    
    with open(filename, 'w', encoding='utf-8') as json_file:
        __dump(
            data,
            json_file,
            sort_keys=False,
            ensure_ascii=False,
            indent=4,
            separators=(',', ': ')
            )

        
def json_initialize_parameters(filename: str, cls)-> None:

    variables_dict = json_read(filename)
    
    for k, v in variables_dict.items():
        setattr(cls, f'path_{k}', v)
        setattr(cls, k, json_read(v))
        
        
def json_write_parameter(filename: str, parameters_dict: dict, parameter: str, value)-> None:
        
    for k, _ in parameters_dict.items():
        
        if k == parameter:
            
            parameters_dict[k] = value
            json_write(filename, parameters_dict)
            return parameters_dict
        
        
def json_append_to(filename: str, items: list)-> None:
    
    data = json_read(filename)
    
    if type(data) != list:
        json_write(filename, [])
    
    if type(items) != list:
        return
    
    data += items
    json_write(filename, data)
        
    
    
    