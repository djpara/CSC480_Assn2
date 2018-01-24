# Majority of the following class is borrowed from
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
class stack:
        def __init__(self):
                self.items = []

        def __str__(self):
                stringFromTop = self.items.copy()
                stringFromTop.reverse()
                return ' '.join(stringFromTop).replace(' ', '')

        def isEmpty(self):
                return self.items == []

        def push(self, item):
                self.items.append(item)

        def pop(self):
                return self.items.pop()

        def size(self):
                return len(self.items)

        def clear(self):
                self.items = []
