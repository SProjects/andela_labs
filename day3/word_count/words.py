# -*- coding: utf-8 -*-


def words(string):
    tokens = [word for word in string.split()]
    return reduce(lambda result, token: update_result(result, token), tokens, {})


def update_result(current_result, token):
    token = int(token) if token.isdigit() else token
    current_result[token] = current_result.get(token, 0) + 1
    return current_result
