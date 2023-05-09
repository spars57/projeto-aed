from abc import ABC
from model.List.Iterator import *

class Iterador(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection)

    def get_next(self):
        if not self.has_next():
            return None
        value = self._collection[self._index]
        self._index += 1
        return value

    def rewind(self):
        self._index = 0