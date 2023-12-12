import atexit
def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))
atexit.register(goodbye, 'Donny', 'nice')
