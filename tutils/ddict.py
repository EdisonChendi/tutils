# coding: utf-8


class Ddict(dict):
    def __init__(self, *args, **kwargs):
        super(Ddict, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                self.update(arg)
        if kwargs:
            self.update(kwargs)

    def update(self, d=None, **kwargs):
        kwargs.update(d)
        for k, v in kwargs.items():
            self[k] = Ddict(v) if isinstance(v, dict) else v

    def __getitem__(self, k):
        try:
            return super(Ddict, self).__getitem__(k)
        except KeyError:
            return None
    __getattr__ = __getitem__

    def __setitem__(self, k, v):
        super(Ddict, self).__setitem__(k, v)
    __setattr__ = __setitem__