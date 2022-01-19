"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Brantley G. Gusler
Date: 1/19/2022
"""

import introcs
import currency

def test_before_space():
    """
    Test procedure for before_space
    """
    print('Testing before_space')

    #Test Case 1
    result = currency.before_space('ab  cd')
    introcs.assert_equals('ab',result)

    #Test Case 2
    result = currency.before_space('abc ')
    introcs.assert_equals('abc',result)

    #Test Case 3
    result = currency.before_space('ab cd ef')
    introcs.assert_equals('ab',result)

    #Test Case 4
    result = currency.before_space(' abc')
    introcs.assert_equals('',result)



def test_after_space():
    """
    Test procedure for after_space
    """
    print('Testing after_space')

    #Test Case 1
    result = currency.after_space('ab cd')
    introcs.assert_equals('cd',result)

    #Test Case 2
    result = currency.after_space('abc ')
    introcs.assert_equals('',result)

    #Test Case 3
    result = currency.after_space('ab  cd')
    introcs.assert_equals(' cd',result)

    #Test Case 4
    result = currency.after_space('ab cd ef')
    introcs.assert_equals('cd ef',result)


def test_first_inside_quotes():
    """
    Test procedure for first_inside_quotes
    """
    print('Testing first_inside_quotes')

    #Test Case 1
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',result)

    #Test Case 2
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C',result)

    #Test Case 3
    result = currency.first_inside_quotes('"A B C D"')
    introcs.assert_equals('A B C D',result)

    #Test Case 4
    result = currency.first_inside_quotes('A B "" C D')
    introcs.assert_equals('',result)

def test_get_src():
    """
    Test procedure for get_src
    """
    print('Testing get_src')

    #Test Case 1
    result = currency.get_src('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)

    #Test Case 2
    result = currency.get_src('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    #Test Case 3
    result = currency.get_src('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',result)

    #Test Case 4
    result = currency.get_src('{"success":false,"src": "","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_get_dst():
    """
    Test procedure for get_dst
    """
    print('Testing get_dst')


def test_has_error():
    """
    Test procedure for has_error
    """
    print('Testing has_error')


def test_service_response():
    """
    Test procedure for service_response
    """
    print('Testing service_response')


def test_iscurrency():
    """
    Test procedure for iscurrency
    """
    print('Testing iscurrency')


def test_exchange():
    """
    Test procedure for exchange
    """
    print('Testing exchange')


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully')
