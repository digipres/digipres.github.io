from __future__ import with_statement
from __future__ import print_function
from urllib.request import urlretrieve
import os

# Download TRiD XML sigs:
url = "https://www.loc.gov/preservation/digital/formats/fddXML.zip"
urlretrieve(url,"fddXML.zip")
print("Downloaded %s" % url )
print(os.system("ls -l fddXML.zip"))

# Remove the files that are there, in case FDDs get deleted:
command = "rm fddXML/*.*"
os.system(command)

# Unpack the new set:
command = "unzip -o fddXML.zip"
os.system(command)

# Ensure Git picks them up:
command = "git add fddXML"
os.system(command)
