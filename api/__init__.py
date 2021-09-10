import os

try:
    # print('Checking for packages')
    import pandas as pd
    import numpy as np
    import datetime as dt
    import typing
    import django
    import rest_framework
    import seaborn
    import matplotlib
    import time
    import os
    import subprocess
    import sys

except Exception as e:
    import subprocess
    import sys

    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    try:
        install('pandas')
        install('numpy')
        install('matplotlib')
        install('django')
        install('djangorestframework')
        install('seaborn')
        install('json')
    except:
        _=0
    
