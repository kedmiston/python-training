
def compact(iterable):
    temp_list = []
    idx = 0
    last_item = None
    for item in iter(iterable):
        idx += 1
        if idx == 1 or item != last_item:
            temp_list.append(item)
        last_item = item
    return (item for item in temp_list)
