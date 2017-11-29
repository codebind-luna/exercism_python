def transform(legacy_data):
    return dict((char.lower(), k) for k,v in legacy_data.items() for char in v)
