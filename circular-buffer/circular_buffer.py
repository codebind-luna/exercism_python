class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self._data = []

    def read(self):
        try:
            return self._data.pop(0)
        except IndexError:
            raise BufferEmptyException

    def write(self, new_item):
        if len(self._data) == self.capacity:
            raise BufferFullException
        self._data.append(new_item)

    def clear(self):
        self._data = []

    def overwrite(self, new_item):
        self._data.append(new_item)
        if len(self._data) > self.capacity:
            self._data.pop(0)
  
