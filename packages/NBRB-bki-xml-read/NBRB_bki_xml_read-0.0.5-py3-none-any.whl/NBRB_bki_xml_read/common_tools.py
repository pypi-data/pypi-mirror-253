'''
Set of tools for data transformation.
'''

import xmltodict

def dict_from_xmlfile(filename):
    '''
    Get dictionary from filename.
    Arguments
    -------------
        filename : (str) path to the XML file to be read;
    Returns
    -------------
        (dict) with data;
    '''
    f = open(filename, "rb")
    data_dict = xmltodict.parse(f.read())
    f.close()
    return data_dict


def recursive_dict_reader(my_dict, prev_pef_names = [], keys_separator = "/"):
    '''
    Recursive deployer of nested dictionaries 
    dictionaries into a single-level dictionary.

    Arguments
    ----------
        my_dict : (dict) dictionary to be deployed;
        prev_pef_names: (str) key paths of higher level dictionaries
                        extremely important for recursion;
        keys_separator: (str) describe symbols that will separate keys
                        of input dictionaries in the result dictionary.
    
    Results
    ---------
        (dict) dictionary reduction of the input set of nested 
               dictionaries to a flat dictionary;
    '''
    res = {}
    
    for key, val in my_dict.items():
        curr_key_dict = prev_pef_names + [key]
        if type(val) == dict:
            res = {
                **res,
                **recursive_dict_reader(
                    val, curr_key_dict,
                    keys_separator = keys_separator
                )
            }
        else:
            res[keys_separator.join(curr_key_dict)] = val
    return res


def dict_reading_decorator(func):
    '''
    A decorator that checks if the searched key 
    is in the dictionary. Dictionary, if not, the 
    exception is triggered - an empty dictionary 
    is returned.
    '''
    def wrapper(dict, **kwargs):
        try:
            return func(dict, **kwargs)
        except KeyError:
            return {}
    
    return wrapper

def sub_dict_reader(my_dict, key_name, **kwargs):
    '''
    Arguments
    -----------
        my_dict : (dict) top-level dictionary;
        key_name : (str) sub-dictionary key in the top-level dictionary;
        kwargs : named arguments for recursive_dict_reader.
        
    Returns
    ----------
        (dict) Flat dictionary, created for the dictionary 
               under the key `key_name` in `my_dict`, 
               with all keys starting with `key_name`.
    '''
    return (
        recursive_dict_reader(my_dict[key_name], [key_name], **kwargs)
        if key_name in my_dict.keys() else {}
    )