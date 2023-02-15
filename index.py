import os
import json
import code
import vscode

# Get the user name
user = os.environ["USER"]
# read the file config.json
with open("config.json", "r") as f:
    config = f.read()
config = json.loads(config)

folders_list = config["symbolic_links"]

# Create the symbolic links
for folder in folders_list:
    target = "/goinfre/" + user + "/" + folder["target"]
    if not os.path.exists(target):
        os.makedirs(target)
    source = folder["source"]
    if not os.path.exists(os.path.expanduser(source)):
        os.symlink(target, os.path.expanduser(source))

# Install the extensions
if os.system("code --version > /dev/null") != 0:
    code()
if not os.path.exists("list-extensions.txt"):
    vscode()
with open("list-extensions.txt", "r") as f:
    extensions = f.read().splitlines()
for extension in extensions:
    os.system("code --install-extension " + extension)