import os
import sys

def code():
    if os.system("code --version > /dev/null") != 0:
        code = "export PATH=\"$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin\""
        with open(os.path.expanduser("~/.zshrc"), "a") as f:
            f.write(code)
        os.system("source ~/.zshrc")

sys.modules[__name__] = code