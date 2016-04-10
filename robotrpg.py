import sys
import os
sys.path.append(os.path.abspath('./lib/pygcurse'))

import pygcurse
from lib.Object import Object

print(Object('wall'))

win = pygcurse.PygcurseWindow(40, 25, 'Hello World')
win.pygprint('Hello!!')
pygcurse.waitforkeypress()
