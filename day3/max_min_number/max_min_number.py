def find_max_min(numbers):
    if not isinstance(numbers, list):
        raise ValueError('Parameter must be a list')

    minimum, maximum = min(numbers), max(numbers)
    return [len(numbers)] if minimum == maximum else [minimum, maximum]

