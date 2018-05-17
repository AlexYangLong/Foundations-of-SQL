class Dept(object):

    def __init__(self, no=None, name=None, loc=None, **kwargs):
        self._no = no
        self._name = name
        self._loc = loc

    @property
    def no(self):
        return self._no

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._loc
