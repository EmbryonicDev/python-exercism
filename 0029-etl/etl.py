def transform(legacy_data):
    data = {}
    for key, value_list in legacy_data.items():
        for values in value_list:
            for value in values:
                data[value.lower()] = key 
    return data

