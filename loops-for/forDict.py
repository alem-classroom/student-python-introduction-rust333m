def reverse_dict(dic):
    # swap keys and values within dict and return dict
    dict1 = {}
    for key in dic:
        dict1[dic[key]] = key
        
    return dict1
