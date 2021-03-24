from eudplib import *

def EUDQueue(basetype=None):
    class _EUDQueue (EUDStruct):
        _fields_ = [
            ('data', EUDArray),
            'pos'
        ]

        def constructor(self, size):
            self.data = EUDArray(size)
            self.pos = 0

        def enqueue(self, x):
            self.data[self.pos] = x
            self.pos += 1

        def dequeue(self):
            data = self.data[0]
            if basetype:
                    data = basetype.cast(data)
            for k in EUDLoopRange(self.pos):
                self.data[k] = self.data[k+1]
            self.pos -= 1
            return data

    return _EUDQueue