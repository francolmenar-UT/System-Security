from random import randrange


class KeyObject:
    e = None
    n = None
    msg = None
    enc_time = None

    def __init__(self, e=None, n=None, msg=None, enc_time=None):
        if enc_time is not None:
            self.create_from_time(e, n, msg, enc_time)
        else:
            self.create_from_values(e, n, msg)

    def create_from_values(self, e, n, msg):
        """
        Used when it is called from loading the keys
        :param msg:
        :param e:
        :param n:
        :return:
        """
        self.e = e
        self.n = n
        self.msg = msg

    def create_from_time(self, e, n, msg, enc_time):
        """
        # TODO
        :param e:
        :param n:
        :param msg:
        :param enc_time:
        :return:
        """
        self.e = e
        self.n = n
        self.msg = msg
        self.enc_time = enc_time

    def add_time(self, new_enc_time):
        """
        # TODO
        :param new_enc_time:
        :return:
        """
        return KeyObject(e=self.e, n=self.n,
                         msg=self.msg, enc_time=new_enc_time)

    def toString(self):
        print(" e: {}\n n: {}\n  msg:{}\n enc_time: {}"
              .format(self.e, self.n, self.msg, self.enc_time))
