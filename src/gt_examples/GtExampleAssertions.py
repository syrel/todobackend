class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class Assertion(Error):
    """Exception raised for errors in the input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, actual, expected):
        self.actual = actual
        self.expected = expected


class Assert:

    @classmethod
    def equals(cls,actual, expected):
        if (actual == expected) != True:
            raise AssertionError(actual, expected)

    @classmethod
    def not_equals(cls, actual, expected):
        if (actual != expected) != True:
            raise AssertionError(actual, expected)

    @classmethod
    def should(cls, a_boolean):
        if a_boolean != True:
            raise AssertionError(a_boolean, True)

    @classmethod
    def deny(cls,a_boolean):
        cls.should(not a_boolean)