def data_type(data):
    if isinstance(data, str):
        return len(data)
    elif n is None:
        return 'no value'
    elif isinstance(data, bool):
        return data
    elif isinstance(data, int):
        if data < 100:
            return 'less than 100'
        elif data == 100:
            return 'equal to 100'
        elif data > 100:
            return 'more than 100'
    elif isinstance(data, list):
        if 3 <= len(data):
            return data[2]
        else:
          return None
