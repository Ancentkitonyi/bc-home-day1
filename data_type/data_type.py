def data_type(data):
  if type(data) == str:
   return len(data)
  elif data is None:
    return 'no value'
  elif type(data) == bool:
    return data
  elif type(data) == int:
    if data < 100:
      return 'less than 100'
    elif data > 100:
      return 'more than 100'
    else:
      return 'equal to 100'
#  elif isinstance(data,list):
  #    return data[2]
      
