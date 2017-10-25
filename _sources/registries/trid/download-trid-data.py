from __future__ import with_statement
from __future__ import print_function
import urllib
import os

# Download TRiD XML sigs:
url = "http://mark0.net/download/triddefs_xml.zip"
urllib.urlretrieve(url,"triddefs_xml.zip")

# Unpack them:
command = "unzip triddefs_xml.zip -d triddefs_xml"
os.system(command)

# Ensure Git picks them up:
command = "git add triddefs_xml"
os.system(command)
