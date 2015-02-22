from __future__ import with_statement
from __future__ import print_function
from BeautifulSoup import BeautifulSoup
import urllib
import urllib2
import urlparse
import re
import os
import os.path

def downloadSigFiles():
    # Get the release notes:
    urllib.urlretrieve("http://www.nationalarchives.gov.uk/aboutapps/pronom/release-notes.xml","release-notes.xml");
    # Now the actual files:
    url = "http://www.nationalarchives.gov.uk/aboutapps/pronom/droid-signature-files.htm"
    html_page = urllib2.urlopen( url )
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a', attrs={'href': re.compile("\.xml$")}):
        xurl = urlparse.urljoin(url,link.get('href'))
        path = urlparse.urlsplit(xurl).path
        name = os.path.split(path)[1]
        print(xurl, name)
        # Switch folders based on the name:
        if "DROID" in name:
            out = "binsigs/"+name
        elif "container" in name:
            out = "contsigs/"+name
        else:
            out = name
        # Download if we don't have it already:
        if not os.path.isfile(out):
            urllib.urlretrieve(xurl,out)


def getMostRecentSigFiles():
    pass

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
        urllib.urlretrieve(getUrlForPuid(puid),"%s.xml" % puid)

downloadSigFiles()
downloadPronomRecords()

# Ensure Git picks them up:
command = "git add binsigs contsigs fmt x-fmt *.xml"
os.system(command)
