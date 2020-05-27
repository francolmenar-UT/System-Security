class KeyObject:

    def __init__(self, key=None, e=None, d=None, n=None, key_size=None):
        self.e = None
        self.d = None
        self.n = None
        self.key_size = None
        if key is not None:
            self.create_from_key(key, key_size)
        else:
            self.create_from_values(e, d, n, key_size)

    def create_from_key(self, key, key_size):
        """
        Used when it is called from crypto
        :param key:
        :param key_size:
        :return:
        """
        self.e = key.public_key().public_numbers().e
        self.d = key.private_numbers().d
        self.n = key.public_key().public_numbers().n
        self.key_size = key_size

    def create_from_values(self, e, d, n, key_size):
        """
        Used when it is called from loading the keys
        :param e:
        :param d:
        :param n:
        :param key_size:
        :return:
        """
        self.e = e
        self.d = d
        self.n = n
        self.key_size = key_size

    def toString(self):
        print("e: {}\n d: {}\n n: {}\n key_size: {}".format(self.e, self.d, self.n, self.key_size))
