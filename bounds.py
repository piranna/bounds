'''
Created on 10/01/2012

@author: piranna
'''


class IntBounds:
    '''
    classdocs
    '''

    def __init__(self, low, high=None):
        '''
        Constructor
        '''
        if high == None:
            self._low = 0
            self._high = low
        else:
            self._low = low
            self._high = high

    def __iter__(self):
        return xrange(self._low, self._high)

    def __call__(self):


orig_range = range
def range(stop, *args, **vargs):
    if isinstance(stop, IntBounds):
        return stop
    else:
        orig_range(stop, *args, **vargs)