"""
Approach
--------
Unsorted map/Dictionary implementation in Python using Array. Inefficient, because most of the methods to set an item by key value or get an item by key
take O(N) time

Complexity
---------
Space: O(N)
Time: O(N) 
"""
class UnsortedMap:

    def __init__(self):
        self._data = []

    class Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other.__key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < self._value

    def __contains__(self, key):
        for item in self._data:
            if item._key == key:
                return True

        return False

    def __iter__(self):
        for item in self._table:
            yield item

    def __getitem__(self, key, default=None):
        for item in self._data:
            if item._key == key:
                return item._value

        return default

    def __setitem__(self, key, value=None):
        for item in self._data:
            if item._key == key:
                item._data = value
                return
        self._data.append(self.Item(key, value))

    def __len__(self):
        return len(self._data)

    def __delitem__(self, key):
        for j in range(len(self._data)):
            if key == self._data[j]._key:
                self._data.pop(j)
                return
        raise KeyError("Invalid key %s" % str(key))


um = UnsortedMap()
um["Abhijit"] = "4214"
um["Ahaan"] = "4215"
um["Deepali"] = "4216"
print(um["Abhijit"])
del um["Abhijit"]
print(um["Abhijit"])