from __future__ import with_statement
from __future__ import print_function
import urllib.request
import shutil
import os

# Download TRiD XML sigs:
url = "https://www.loc.gov/preservation/digital/formats/fddXML.zip"
file_name = "fddXML.zip"

# Set a suitable user agent:
UA = os.environ.get('LOC_UA', 'Sentinel/1.0 (+https://www.digipres.org/)')

# Do the download:
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', UA)]
with opener.open(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

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
