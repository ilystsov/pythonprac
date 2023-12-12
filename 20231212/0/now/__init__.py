import time
import atexit
import pathlib

s = pathlib.Path('date')
if s.exists():
    DATE = float(s.read_text())
else:
    DATE = time.time() # если файла нет, если есть то читать из файла. если в процессе работы питона date изменилось, оно записывается в файл
    s.touch()


@atexit.register
def f(): 
    s.write_text(DATE)
