"""RGB To Hex Conversion

https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

The rgb() method is incomplete. Complete the method so that passing in RGB
decimal values will result in a hexadecimal representation being returned.
The valid decimal values for RGB are 0 - 255.
Any (r,g,b) argument values that fall out of that range should be rounded
to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")

"""
import doctest


def normal(x):
    if x < 0:
        return 0
    elif x < 256:
        return x
    return 255


def rgb(r, g, b):
    """
    >>> rgb(0,0,0)
    '000000'
    >>> rgb(1,2,3)
    '010203'
    >>> rgb(255,255,255)
    'FFFFFF'
    >>> rgb(254,253,252)
    'FEFDFC'
    >>> rgb(-20,275,125)
    '00FF7D'

    :param r:
    :param g:
    :param b:
    :return:
    """
    r, g, b = [normal(x) for x in [r, g, b]]

    return "{0:06X}".format(r << 16 | g << 8 | b)


def rgb2(r, g, b):
    """
    
    >>> rgb(0,0,0)
    '000000'
    >>> rgb(1,2,3)
    '010203'
    >>> rgb(255,255,255)
    'FFFFFF'
    >>> rgb(254,253,252)
    'FEFDFC'
    >>> rgb(-20,275,125)
    '00FF7D'

    :param r:
    :param g:
    :param b:
    :return:
    """
    r, g, b = [min(255, max(x, 0)) for x in [r, g, b]]
    return "{0:06X}".format(r << 16 | g << 8 | b)


if __name__ == '__main__':
    doctest.testmod()
