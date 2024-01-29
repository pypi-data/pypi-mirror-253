'''
Functions that allows to read information for 
individual client.
'''
from .common_tools import (
    dict_reading_decorator, 
    sub_dict_reader
)


def read_latecount(laterange):
    """
    Read structure with type of 
    `CType-LateCount`.

    Parameters
    -----------
    laterange : (list) contains dicts with keys:
                'mindays' with min day of late;
                'maxdays' with max day of late;
                'count' value;
    
    Returns
    -----------
    (dict) flat dict with the same information.
    """
    return {
        (
            f"[{r['mindays']};{r['maxdays']}]"
            if ('maxdays' in r) else
            f">{r['mindays']}"
        ) : int(r["count"])
        for r in laterange
    }

@dict_reading_decorator
def read_client(client_dict, keys_separator="/"):
    '''
    Read bki information starting from the "client" field.
    
    Parameters
    -----------
        client_dict :    (dict) dictionary which can be created
                         from infromation between <client> tag
                         of bki.xml
        keys_separator : (str) describe symbols that will separate keys
                         of input dictionaries in the result dictionary.
    Returns
    ----------
        (dict) flat dictionary that contains 
        infromation between <clint> tag from bki.xml. 
    '''

    res = {
        # here are relatively simple fields that can be read just as
        # as dictionaries throw sub_dict_reader
        **{
            "client" + keys_separator + key:val
            for field_name in [
                "titul",
                "registrationplace",
                "range",
                "scoring",
                "RequestNumber7Days",
                "RequestNumber30Days"
            ]
            for key, val in sub_dict_reader(
                client_dict, field_name,
                keys_separator = keys_separator
            ).items()
        },
        # there are values that can't be encoded with
        # sub_dict_reader so we just take them.
        # we use it in three cases.
        # - Final value is under key;
        # - Some complex type that cannot be properly 
        #   encoded with sub_dict_reader;
        # - We didn't understand yet that this field can
        #   be encoded with sub_dict_reader ;).
        **{
            "client" + keys_separator + field_name : client_dict[field_name]
            for field_name in [
                "owner",
                "contracttype",
                "ContractList",
                "requestnumber",
                "TotalDebtSum"
            ]
            if field_name in client_dict
        }
    }

    return res


@dict_reading_decorator
def read_result(result_dict, keys_separator="/"):
    '''
    Read the response from bki starting from the "result" field.

    Parameters
    -----------
        result_dict :    (dict) dictionary which can be created
                         from infromation between <result> tag
                         of bki.xml
        keys_separator : (str) describe symbols that will separate keys
                         of input dictionaries in the result dictionary.
    Returns
    ----------
        (dict) flat dictionary that contains 
        infromation between <result> tag from bki.xml. 
    '''
    
    res = {
        **sub_dict_reader(
            result_dict, "completecode", 
            keys_separator = keys_separator
        ),
        **(
            read_client(result_dict["client"], keys_separator = keys_separator)
            if ("client" in result_dict.keys()) else {}
        )
    }

    return {"result" + keys_separator + key:val for key, val in res.items()}