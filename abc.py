class UnknownAtom:
    def __init__(self, m, v, fn):
        self.__m = m
        self.__v = v
        self.__func_name = fn

    def get(self):
        return f'{self.__m} out of range {self.__v} - {self.__func_name}'

    def get_value(self):
        return self.__v


class Atom:
    def __init__(self, name):
        self.name = name

    def C(self):
        pass

    def N(self):
        pass

    def H(self):
        pass

    def O(self):
        pass

    def P(self):
        pass


