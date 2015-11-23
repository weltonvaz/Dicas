while 1:
    len_name = data.read(4)
    if not len_name:
        break
    names.append(data.read(len_name))
