class Group(object):
    def __init__(self, *, g_id=None, g_title=None, **kwargs):
        self._id = g_id
        self._title = g_title

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title


class Book(object):
    def __init__(self, *, b_id=None, b_name=None, b_phone=None, b_address=None, b_gid=None, b_addtime=None):
        self._id = b_id
        self._name = b_name
        self._phone = b_phone
        self._address = b_address
        self._gid = b_gid
        self._addtime = b_addtime

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def gid(self):
        return self._gid

    @gid.setter
    def gid(self, gid):
        self._gid = gid

    @property
    def addtime(self):
        return self._addtime

    @addtime.setter
    def addtime(self, addtime):
        self._addtime = addtime