def data_type(arg):
    valid_types = (str, int, bool, list)
    if not isinstance(arg, valid_types) and arg is not None:
        raise ValueError

    if arg is None:
        return 'no value'
    if isinstance(arg, str):
        return len(arg)
    if isinstance(arg, bool):
        return arg
    if isinstance(arg, int):
        return _compare_with_100(arg)
    if isinstance(arg, list):
        return arg[2] if len(arg) > 2 else None


def _compare_with_100(num):
    if num == 100:
        return 'equal to 100'
    if num < 100:
        return 'less than 100'
    if num > 100:
        return 'more than 100'
