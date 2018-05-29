import abc
import set 

class ABSsubject(object):
    __metaclass__= abc.ABCMeta
    _observers = set()

    @abc.abstractclassmethod
    def attach(self, observer):
        _observers |= observer

    @abc.abstractclassmethod
    def detach(self, observer):
        _observers -= observer

    