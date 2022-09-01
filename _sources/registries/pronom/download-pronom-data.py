from __future__ import with_statement
from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlparse, urljoin, urlsplit
from urllib.request import urlretrieve, urlopen
import re
import os
import os.path

def downloadSigFiles():
    # Lists to store all sig file names:
    binsigs = []
    contsigs = []
    # Get the release notes:
    urlretrieve("http://www.nationalarchives.gov.uk/aboutapps/pronom/release-notes.xml","release-notes.xml");
    # Now the actual files:
    url = "http://www.nationalarchives.gov.uk/aboutapps/pronom/droid-signature-files.htm"
    html_page = urlopen( url )
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a', attrs={'href': re.compile("\.xml$")}):
        xurl = urljoin(url,link.get('href'))
        path = urlsplit(xurl).path
        name = os.path.split(path)[1]
        print(xurl, name)
        # Switch folders based on the name:
        if "DROID" in name:
            out = "binsigs/"+name
            binsigs.append(name)
        elif "container" in name:
            out = "contsigs/"+name
            contsigs.append(name)
        else:
            out = name
        # Download if we don't have it already:
        if not os.path.isfile(out):
            urlretrieve(xurl,out)

    # Now update main files with latest versions:
    def extract_number(f):
        s = re.findall("\d+",f)
        return (int(s[0]) if s else -1,f)

    latest_binsig = max(binsigs, key=extract_number)
    latest_contsig = max(contsigs, key=extract_number)
    print(latest_binsig, latest_contsig)
    os.system(f"mv binsigs/{latest_binsig} droid-signature-file.xml") 
    os.system(f"mv contsigs/{latest_contsig} container-signature.xml") 


def getUrlForPuid(puid):
    return "http://www.nationalarchives.gov.uk/PRONOM/%s.xml" % puid

def downloadPronomRecords():
    puids = set()
    # Get PUIDs from BinSigs:
    with open("droid-signature-file.xml", "r") as f:
        soup = BeautifulSoup(f.read())
        for ff in soup.findAll('fileformat'):
            name = ff.get('puid')
            puids.add(name)
    # Get PUIDs from ContSigs:
    with open("container-signature.xml", "r") as f:
        soup = BeautifulSoup(f.read())
        for ff in soup.findAll('fileformatmapping'):
            name = ff.get('puid')
            puids.add(name)

    # Download all PUID records:
    for puid in sorted(puids):
        print("Downloading %s..." % puid)
        # Download it:
        urlretrieve(getUrlForPuid(puid),"%s.xml" % puid)

downloadSigFiles()
downloadPronomRecords()

# Ensure Git picks them up:
command = "git add binsigs contsigs fmt x-fmt *.xml"
os.system(command)
