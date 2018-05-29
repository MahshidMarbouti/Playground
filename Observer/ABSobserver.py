import abc

class abs_observer(object):
    __metaclass__= abc.ABCMeta

    @abc.abstractclassmethod
    def update(self, value):
        pass
    

