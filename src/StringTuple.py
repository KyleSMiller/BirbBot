

class StringTuple:
    """
    Class to allow .json files to take tuples as keys
    """
    def __init__(self, string, delimiter=","):
        self.__string = string
        self.__delimiter = delimiter
        self.__tuple = self.__stringToTuple(string)

    def getString(self):
        return self.__string

    def getTuple(self):
        return self.__tuple

    def __stringToTuple(self, string):
        """
        convert a string into a tuple, splitting elements along a specified delimiter
        :param string:  the string to convert
        :return:
        """
        listKey = string.strip().split(self.__delimiter)
        return tuple(listKey)