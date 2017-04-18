def fizz_buzz(num):
    if not isinstance(num, int):
        raise ValueError('Parameter must be an integer')

    result = ''
    if num % 3 == 0:
        result += 'Fizz'
    if num % 5 == 0:
        result += 'Buzz'

    if result:
        return result
    return num
