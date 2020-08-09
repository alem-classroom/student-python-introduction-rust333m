def reverse_dict(dict):
    # swap keys and values within dict and return dict
    dict1 = dict{}
    for key in dict:
        dict1[dict[key]] = key
        
    return dict1
