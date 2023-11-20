from string import ascii_lowercase
class Alpha:
    __slots__ = tuple(ascii_lowercase)
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
            
    def __str__(self):
        out = []
        for field in ascii_lowercase:
            if hasattr(self, field):
                out.append(f'{field}: {getattr(self, field)}')
        return ', '. join(out)

class AlphaQ:
    fields = {}
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            if name not in ascii_lowercase:
                raise AttributeError
            self.fields[name] = value
    
    def __getattr__(self, name):
        if name not in self.fields:
            raise AttributeError
        return self.fields[name]
    
    def __setattr__(self, name, value):
        if name not in ascii_lowercase:
            raise AttributeError
        self.fields[name] = value 

    def __str__(self):
        out = []
        for field in ascii_lowercase:
            if field in self.fields:
                out.append(f'{field}: {self.fields[field]}')
        return ', '. join(out)
        

import sys
exec(sys.stdin.read())
