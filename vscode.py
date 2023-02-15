import os
import code
import sys

def vscode():
    if os.system("code --version > /dev/null") != 0:
        code()
    os.system("code --list-extensions > list-extensions.txt")

sys.modules[__name__] = vscode