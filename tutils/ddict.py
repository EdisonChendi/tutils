# coding: utf-8


class Ddict(dict):
    def __init__(self, *args, **kwargs):
        super(Ddict, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for t in arg.items():
                    self[t[0]] = (
                        Ddict(t[1]) if isinstance(t[1], dict) else t[1])
        if kwargs:
            for t in kwargs.items():
                self[t[0]] = Ddict(t[1]) if isinstance(t[1], dict) else t[1]

    def __getitem__(self, k):
        try:
            return super(Ddict, self).__getitem__(k)
        except KeyError:
            return None
    __getattr__ = __getitem__

    def __setitem__(self, k, v):
        super(Ddict, self).__setitem__(k, v)
    __setattr__ = __setitem__
