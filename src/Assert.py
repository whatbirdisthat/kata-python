from TestFailed import TestFailed

class Assert:
    @staticmethod
    def Equal(expected, actual):
        if expected != actual:
            raise TestFailed("Expected {}, Actual {}".format(expected, actual))
