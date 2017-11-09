"""
:author: atul 
"""

import os
import sys
import shutil

APP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app')

def startproject(name, dest=None):
    if dest:
        path = os.path.join(dest, name, 'app')
    else:
        path = os.path.join(name, 'app')
    if not os.path.exists(path):
        shutil.copytree(APP_DIR, path)


       
        
    

    
    