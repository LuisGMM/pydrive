

class superFather:

    def __init__(self, arg1):
        self.arg1 = arg1


class Father(superFather):

    def __init__(self, arg1, arg2):
        super().__init__(arg1)

        self.arg2 = arg2


class other:

    def __init__(self, arg1_parellel):
        self.arg1_parellel = arg1_parellel


class child(Father, other):

    def __init__(self, arg1, arg2, arg1_parellel):

        Father.__init__(self, arg1, arg2)
        other.__init__(self, arg1_parellel)


ins = child(1, 2, 3)

print(ins.__dict__)
