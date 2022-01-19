"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Brantley G. Gusler
Date:   1/19/2022
"""
import introcs
APIKEY = 'j3mgT7zZhEaL0gKVtOHSpX1J9x1LspFwTvp4cizJ0ZIe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.count_str(s,' ') >= 1, 'The string '+repr(s)+' does not have enough spaces.'

    a = introcs.find_str(s,' ')
    slice = s[0:a]
    return slice


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.count_str(s,' ') >= 1, 'The string '+repr(s)+' does not have enough spaces.'

    a = introcs.find_str(s,' ')+1
    slice = s[a:]
    return slice


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert introcs.count_str(s,'"') >= 2, 'The string '+repr(s)+' does not have enough double quotes.'

    a = introcs.find_str(s,'"')+1
    b = introcs.find_str(s,'"',a)
    slice = s[a:b]
    return slice


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    a = introcs.find_str(json,'"')+1
    b = json[a:]
    c = introcs.find_str(b,'"')+1
    d = b[c:]
    e = introcs.find_str(d,'"')+1
    f = d[e:]
    g = introcs.find_str(f,'"')+1
    h = f[g:]
    result = first_inside_quotes(h)
    return result
