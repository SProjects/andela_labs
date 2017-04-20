def find_missing(list_one, list_two):
    diff = list(set(list_two).difference(set(list_one)))
    return len(diff) if len(diff) == 0 else diff[0]

