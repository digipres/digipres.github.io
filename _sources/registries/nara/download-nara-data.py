from urllib.request import urlretrieve
import os

# Download TRiD XML sigs:
url = "https://www.archives.gov/files/lod/dpframework/fileformats.ttl"
urlretrieve(url,"fileformats.ttl")

# Ensure Git picks them up:
command = "git add fileformats.ttl"
os.system(command)
