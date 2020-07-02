class Sequence():

    def __init__(self):
        self._id = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def integers(self):
        return self._integers

    @integers.setter
    def integers(self, integers):
        self._integers = integers