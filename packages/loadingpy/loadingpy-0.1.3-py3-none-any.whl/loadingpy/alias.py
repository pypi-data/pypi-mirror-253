import sys


def aliases(*pseudonyms):
    def aliaser(cls):
        namespace = sys._getframe(1).f_globals
        namespace.update({alias: cls for alias in pseudonyms})
        cls.aliases = pseudonyms
        return cls

    return aliaser
