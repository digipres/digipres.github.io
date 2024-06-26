from __future__ import with_statement
from __future__ import print_function
from urllib.request import urlretrieve
import os

# Download TRiD XML sigs:
url = "http://mark0.net/download/triddefs_xml.7z"
urlretrieve(url,"triddefs_xml.7z")

# Unpack them:
command = "7z x -otriddefs_xml -y triddefs_xml.7z"
os.system(command)

# Ensure Git picks them up:
command = "git add triddefs_xml"
os.system(command)
