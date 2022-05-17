import os
import platform

if os.name == 'nt':
    if platform.release() == '10':
        print(1)