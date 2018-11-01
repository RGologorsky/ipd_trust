class Sim_Data:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return str(self.data)

    from test_global_3 import f1

    def f(self):
        self.data.append(0)
