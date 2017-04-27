from __future__ import with_statement
from __future__ import print_function
import urllib
import os

# Download TRiD XML sigs:
url = "https://www.loc.gov/preservation/digital/formats/fddXML.zip"
urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
urllib.urlretrieve(url,"fddXML.zip")
print("Downloaded %s" % url )
print(os.system("ls -l fddXML.zip"))

# Unpack them:
command = "unzip -o fddXML.zip"
os.system(command)

# Ensure Git picks them up:
command = "git add fddXML"
os.system(command)
