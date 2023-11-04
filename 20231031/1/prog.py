from collections import defaultdict


class Omnibus:
    attributes_number = defaultdict(int)

    def __init__(self):
        self.__dict__['attribute names'] = set()    

    def __setattr__(self, name, value):
        if name not in self.__dict__['attribute names']:
            self.__class__.attributes_number[name] += 1
            self.__dict__['attribute names'].add(name)
    
    def __delattr__(self, name):
        if name in self.__dict__['attribute names']:
            self.__class__.attributes_number[name] -= 1
            self.__dict__['attribute names'].remove(name)

    def __getattr__(self, name):
        return self.__class__.attributes_number[name]

import sys
exec(sys.stdin.read())