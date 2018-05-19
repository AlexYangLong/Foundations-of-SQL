class Dept(object):
    def __init__(self, *, dno=None, dname=None, dloc=None, **kwargs):
        self._dno = dno
        self._dname = dname
        self._loc = dloc

    @property
    def dno(self):
        return self._dno

    @property
    def dname(self):
        return self._dname

    @property
    def dloc(self):
        return self._dloc


if __name__ == '__main__':
    pass